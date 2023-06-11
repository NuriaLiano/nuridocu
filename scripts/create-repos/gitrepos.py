import sys, gitlab, os, git, shutil, json, datetime, requests, subprocess

############ TODO ############
###############################

#TODO: - hace mirror pero no aplica los cambios una vez hecho el primer mirror.

############ COMMON FUNCTIONS ############
##########################################

def check_config_exits():
    if os.path.exists(os.getcwd()):
        return True
    else:
        return False
    
def open_config_data(config_path):
    try:
        # Leer el archivo JSON
        with open(config_path) as file:
            return json.load(file)
    except FileNotFoundError:
        print(Fore.RED + '[ERROR]' + f'File "{config_path}" does not exist')

def check_define_config(config_path):
    #validar si el path que pasamos tiene la palabra config
    if config_path.find('.config.json') == -1:
        return os.path.join(config_path, '.config.json')
    else:
        return config_path

def add_data_config(tagname, value, config_path):
    #primero hay que abrir el fichero
    data = open_config_data(config_path)
    # Agrega la nueva palabra al diccionario
    data['DEFAULT'][tagname] = value
    try:
        # Guarda el diccionario en el fichero .config.json
        with open(config_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(Fore.RED + '[ERROR]' + f'Error al guardar los cambios en {config_path}')

def load_config():

    #global vars
    global GL_TK, URL_GL, INSTANCE_GL, USERNAME_GL, CONFIG_PATH

    #comprueba que el fichero .config.json existe en el directorio actual
    if check_config_exits() is False:
        #si no existe, se lo pide al usuario
        config_path = input('Enter the absolute path to the .config.json: ')

        #chequear si en el path está puesto .config.json
        CONFIG_PATH = check_define_config(config_path)
        
        #lo almacena para no tener que volver a preguntar
        add_data_config('CONFIG_PATH', CONFIG_PATH, CONFIG_PATH)

    else:
        #recoger el path actual
        config_path = os.path.dirname(os.path.abspath(__file__))
        #chequear si en el path está puesto .config.json
        CONFIG_PATH = check_define_config(config_path)

    #open config file
    data = open_config_data(CONFIG_PATH)

    # Extraer los valores del JSON
    GL_TK = data['DEFAULT']['GL_TOKEN']
    URL_GL = data['DEFAULT']['URL_GL']

    INSTANCE_GL = gitlab.Gitlab(URL_GL, private_token=GL_TK)

############ GETTERS ############
#################################

def get_repo_name():
    #global vars
    global REPO_NAME

    #read repo_name from parameter
    if len (sys.argv) > 1:
        REPO_NAME = sys.argv[1].replace(' ', '-')
    else:
        while True:
            repo_name_input = input(Fore.CYAN + 'Enter the repos name: ').lower()
            if repo_name_input != '':
                REPO_NAME = repo_name_input.replace(' ', '-')
                break

def get_local_dir():
    #global vars
    global LOCAL_PATH_REPO

    local_dir_input = input(Fore.CYAN + 'Enter the local path: ').lower()
    if local_dir_input != '':
        LOCAL_PATH_REPO = local_dir_input
        LOCAL_PATH_REPO = LOCAL_PATH_REPO + "\\" + REPO_NAME
    else:
        LOCAL_PATH_REPO = ""

############ LOCAL FUNCTIONS ############
#########################################

def remove_local_directory():
    try:
        if os.path.exists(LOCAL_PATH_REPO):
            shutil.rmtree(LOCAL_PATH_REPO)
            print(Fore.GREEN + '[SUCCESS]' + f'Directory "{LOCAL_PATH_REPO}" has been deleted')
    except Exception as e:
        print(Fore.RED + '[ERROR]' + f'Directory "{LOCAL_PATH_REPO}" does not exist')
        print("Error:", str(e))

def create_local_directory(LOCAL_PATH_REPO):
    if LOCAL_PATH_REPO == "":
        LOCAL_PATH_REPO = os.path.dirname(os.path.abspath(__file__))
        add_data_config("LOCAL_PATH_REPO", LOCAL_PATH_REPO, CONFIG_PATH)
    try:
        os.mkdir(LOCAL_PATH_REPO)
        print(Fore.GREEN + '[SUCCESS]' + f'Local folder "{LOCAL_PATH_REPO}" created successfully')
    except FileExistsError:
        print(Fore.RED + '[ERROR]' + f'Directory "{LOCAL_PATH_REPO}" already exists')

def create_README():
    global README_PATH
    try:
        README_PATH = LOCAL_PATH_REPO + "\\" + "README.md"
        add_data_config('README_PATH', README_PATH, CONFIG_PATH)
        # Crea el archivo en el directorio especificado
        with open(README_PATH, "w") as file:
            # Realiza operaciones de escritura en el archivo si es necesario
            file.write("# " + REPO_NAME)
        # Verificación de la creación exitosa
        print("[SUCCESS]" + f'File created successfully')
    except IOError as e:
        print(Fore.RED + '[ERROR]' + f'Error creating file "{README_PATH}"')
        print(e)

############ GITLAB REMOTE FUNCTIONS ############
#################################################

def create_gitlab_repo():
    global GL_PROJECT_URL
    #create object with token
    gl = INSTANCE_GL
    #create new repo
    project = gl.projects.create({'name': REPO_NAME, 'visibility': 'public'})
    #print url
    GL_PROJECT_URL = project.http_url_to_repo
    add_data_config('GL_PROJECT_URL', GL_PROJECT_URL, CONFIG_PATH)
    print(Fore.YELLOW + '[CHECK]' + 'Check the new repo: ', project.web_url)
    return project

def search_gitlab_repo():
    global ID_REPO_GL
    ID_REPO_GL = None
    #search project by name
    gl = INSTANCE_GL
    try:
        projects = gl.projects.list(search=REPO_NAME, owned=True)
        for repo in projects:
            ID_REPO_GL = repo.id
    except gitlab.exceptions.GitlabError as e:
        print("GitLab API returned an error:", e)

def remove_gitlab_repo():
    remove_prompt = input ('Are you sure you want to delete the repository? (y/n)')
    if remove_prompt.lower() == 'y':
        search_gitlab_repo()
        if ID_REPO_GL is None:
            print(Fore.RED + '[ERROR]' + f'No project found with name "{REPO_NAME}"')
            return
        else:
            gl = INSTANCE_GL
            gl.projects.delete(ID_REPO_GL)
            print(Fore.GREEN + '[SUCCESS]' + 'The repo ' + REPO_NAME + ' has been deleted')
    else:
        print(Fore.RED + '[ERROR]' + 'The repo ' + REPO_NAME + ' has not been deleted')

def git_add_commit_push():
    commit_message = "[COMMIT GENERATED BY GITREPOS]"
    repo_branch = "origin"
    try:
        repo = git.Repo(LOCAL_PATH_REPO)  # Inicializa el repositorio en el directorio actual
        repo.index.add(README_PATH)  # Agrega el archivo al área de preparación (staging)
        repo.index.commit("probando")  # Realiza el commit con el mensaje especificado
        origin = repo.remote(name=repo_branch)  # Obtiene la referencia al repositorio remoto
        origin.push()  # Realiza el push al repositorio remoto
        
        print(Fore.GREEN + f"[SUCCESS] Changes pushed to remote repository successfully")

    except Exception as e:
        # Manejar errores en caso de fallo en las operaciones de Git
        print('[ERROR] GIT ADD COMMIT PUSH Failed to perform Git operation')
        print(str(e))

def clone_repo():
    try:
        gitlab_repo = git.Repo.clone_from(GL_PROJECT_URL, LOCAL_PATH_REPO)
        create_README()
        git_add_commit_push()
        print(f'Repository cloned to local folder "{LOCAL_PATH_REPO}" successfully')
        return gitlab_repo
    except Exception as e:
        print('[ERROR] CLONE REPO Failed to perform Git operation')
        print(str(e))

############ GITHUB REMOTE FUNCTIONS ############
#################################################
def create_github_repo():
    global GH_TK, URL_GH, GH_PROJECT_URL, URL_REMOVE_GH, GH_USERNAME

    data = open_config_data(CONFIG_PATH)
    URL_GH = data['DEFAULT']['URL_GH']
    GH_TK = data['DEFAULT']['GH_TOKEN']
    URL_REMOVE_GH =data['DEFAULT']['URL_REMOVE_GH']
    GH_USERNAME = data['DEFAULT']['GH_USERNAME']  
    # Build the API URL to remove the repository
    GH_PROJECT_URL = URL_REMOVE_GH+GH_USERNAME+"/"+REPO_NAME

    headers = {
        "Authorization": f"Bearer {GH_TK}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(URL_GH, headers=headers, json=data)
    if response.status_code == 201:
        add_data_config('GH_PROJECT_URL', GH_PROJECT_URL, CONFIG_PATH)
        print(Fore.GREEN + '[SUCCESS]' + "GitHub repository created successfully")
    else:
        print(Fore.RED + '[ERROR]' + f"Failed to create GitHub repository")
        print(Fore.RED + '[ERROR]' + f"Response:", response.json())

def remove_github_repo():
    global GH_TOKEN,GH_PROJECT_URL, URL_REMOVE_GH, GH_USERNAME

    data = open_config_data(CONFIG_PATH)
    GH_TOKEN = data['DEFAULT']['GH_TOKEN']
    URL_REMOVE_GH =data['DEFAULT']['URL_REMOVE_GH']
    GH_USERNAME = data['DEFAULT']['GH_USERNAME']
    GH_PROJECT_URL = ""    
    # Set authentication headers
    headers = {
        "Authorization": f"Token " + GH_TOKEN
    }
    print(GH_PROJECT_URL)
    if GH_PROJECT_URL == "":
        # Build the API URL to remove the repository
        GH_PROJECT_URL = URL_REMOVE_GH+GH_USERNAME+"/"+REPO_NAME
    # Send the DELETE request to remove the repository
    response = requests.delete(GH_PROJECT_URL, headers=headers)

    # Check the response
    if response.status_code == 204:
        print(Fore.GREEN + '[SUCCESS]' + 'The repo ' + REPO_NAME + ' has been deleted')
    else:
        print(Fore.RED + '[ERROR]' +":", response.json())

def configure_mirror():
    # gl = INSTANCE_GL
    # search_gitlab_repo() #return id GL repo
    # print(ID_REPO_GL)
    # project = gl.projects.get(ID_REPO_GL)
    
# Clonar el repositorio de GitLab
    repo_url = 'https://gitlab.com/Nuria_Liano/gitrepos.git'
    # subprocess.run(['git', 'clone', '--mirror', repo_url])

    # Cambiar al directorio clonado
    # repo_name = repo_url.split('/')[-1].split('.')[0]
    # print(repo_name)
    os.chdir("C:\\Users\\nuria-msi\\gitlab\\gitrepos")
    # subprocess.run(['cwd', "C:\\Users\\nuria-msi\\gitlab\\nuridocu\\scripts\\create-repos"])

    # Agregar el repositorio de GitHub como remoto
    github_repo_url = 'https://github.com/NuriaLiano/gitrepos.git'  # URL del repositorio de GitHub
    subprocess.run(['git', 'remote', 'add', 'github', github_repo_url])

    # Sincronizar los cambios de GitLab a GitHub
    subprocess.run(['git', 'fetch', '--all'])
    subprocess.run(['git', 'push', '--mirror', 'github'])

    print(f"El espejo del repositorio {repo_url} ha sido creado en {github_repo_url}")

    # repo_url = "https://gitlab.com/Nuria_Liano/gitrepos.git"
    # username = "NuriaLiano"
    # reponame = "gitrepos"
    # # Crea una instancia de Github
    # github = Github("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")

    # # Obtén el nombre de usuario y el nombre del repositorio desde la URL
    # # parts = repo_url.split('/')
    # # username = parts[-2]
    # # reponame = parts[-1].split('.')[0]

    # # Obtiene el repositorio de origen de GitLab
    # gitlab_repo = github.get_repo(f'{username}/{reponame}')

    # # Crea un nuevo repositorio en GitHub
    # github_user = github.get_user()
    # new_repo = github_user.create_fork(gitlab_repo)

    # print(f"El espejo del repositorio {repo_url} ha sido creado en {new_repo.html_url}")

    # GITHUB_REPO_URL = "https://nurialiano@github.com/NuriaLiano/gitrepos.git"  # URL del repositorio de GitHub

    # headers = {
    #     "PRIVATE-TOKEN": GL_TK,
    #     "Content-Type": "application/json"
    # }

    # data = {
    #     "id": ID_REPO_GL,
    #     "enabled": True,
    #     "url": GITHUB_REPO_URL,
    #     "mirror_trigger_builds": True,
    #     "mirror_overwrites_diverged_branches": True
    # }

    # # Realizar la solicitud a la API de GitLab para configurar el push mirror
    # response = requests.put(f"https://gitlab.com/api/v4/projects/{ID_REPO_GL}", headers=headers, json=data)

    # if response.status_code == 200:
    #     print("El proyecto se ha configurado correctamente como un push mirror en GitLab.")
    # else:
    #     print(f"Error al configurar el push mirror: {response.text}")

    

############ MAIN FUNCTION ###############
##########################################

if __name__ == '__main__':

    #colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

    main_prompt = input('Do you want remove or create new repo (r/c)')
    
    #load all vars and config
    load_config()

    get_repo_name()
    get_local_dir()

    if main_prompt.lower() == 'r':
        print('\u26A0\ufe0f YOU HAVE CHOSEN TO REMOVE THE REPO AND DIRECTORY. ¡¡¡¡THIS ACTION CANNOT BE UNDONE \u26A0\ufe0f !!!!')
        confirm_prompt = input('Are you sure? (y/n)')
        if confirm_prompt == 'y':
            remove_gitlab_repo()
            remove_local_directory()
            remove_github_repo()
        else:
            print('Oh my god you almost messed up')
    elif main_prompt.lower() == 'c':
        print('YOU HAVE CHOSEN TO CREATE NEW REPO.')
        
        create_gitlab_repo()
        create_local_directory(LOCAL_PATH_REPO)
        clone_repo()
        create_github_repo()
        configure_mirror()
        # create_gitlab_mirror()
    else:
        print(Fore.RED + '[NOT ALLOWED]' + 'Invalid option')
    

    
