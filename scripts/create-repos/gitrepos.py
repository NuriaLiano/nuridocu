import sys, gitlab, os, git, shutil, json, datetime

############ TODO ############
###############################

#TODO: - Create README.md PARA EL PROYECTO DE GITREPOS
#TODO: ME FALTA LA PARTE DE GITHUB
#TODO: CUANDO ESTE LA PARTE DE GITHUB HACE FALTA EL MIRROR DE LOS DOS REPOSITORIOS, GITLAB Y GITHUB


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
            repo_name_input = input(Fore.CYAN + 'Enter the repos name: ')
            if repo_name_input != '':
                REPO_NAME = repo_name_input.replace(' ', '-')
                break

def get_local_dir():
    #global vars
    global LOCAL_PATH_REPO

    local_dir_input = input(Fore.CYAN + 'Enter the local path: ')
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
            print(f'Directory "{LOCAL_PATH_REPO}" has been deleted')
    except Exception as e:
        print(Fore.RED + '[ERROR]' + f'Directory "{LOCAL_PATH_REPO}" does not exist')
        print("Error:", str(e))

def create_local_directory():
    if LOCAL_PATH_REPO == "":
        LOCAL_PATH_REPO = os.path.dirname(os.path.abspath(__file__))
    
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
        print("[SUCCESS]" + f'File "{README_PATH}" created successfully')
    except IOError as e:
        print(Fore.RED + '[ERROR]' + f'Error creating file "{README_PATH}"')
        print(e)

############ GITLAB REMOTE FUNCTIONS ############
#################################################

def create_repo():
    global PROJECT_URL
    #create object with token
    gl = INSTANCE_GL
    #create new repo
    project = gl.projects.create({'name': REPO_NAME})
    #print url
    PROJECT_URL = project.http_url_to_repo
    print(Fore.YELLOW + '[CHECK]' + 'Check the new repo: ', project.web_url)
    return project

def search_repo():
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

def remove_repo():
    remove_prompt = input ('Are you sure you want to delete the repository? (y/n)')
    if remove_prompt.lower() == 'y':
        search_repo()
        if ID_REPO_GL is None:
            print(Fore.RED + '[ERROR]' + f'No project found with name "{REPO_NAME}"')
            return
        else:
            gl = INSTANCE_GL
            gl.projects.delete(ID_REPO_GL)
            print(Fore.GREEN + '[DONE]' + 'The repo ' + REPO_NAME + ' has been deleted')
    else:
        print(Fore.RED + '[ERROR]' + 'The repo ' + REPO_NAME + ' has not been deleted')

def git_add_commit_push():
    commit_message = "[COMMIT GENERATED BY GITREPOS ON " + str(datetime.datetime.now()) + "]"
    repo_branch = "origin"
    try:
        repo = git.Repo("LOCAL_PATH_REPO")  # Inicializa el repositorio en el directorio actual

        repo.index.add(README_PATH)  # Agrega el archivo al área de preparación (staging)

        repo.index.commit("commit_message")  # Realiza el commit con el mensaje especificado

        origin = repo.remote(name=repo_branch)  # Obtiene la referencia al repositorio remoto

        origin.push()  # Realiza el push al repositorio remoto
        
        print(Fore.GREEN + f"[SUCCESS] Changes pushed to remote repository successfully")

    except Exception as e:
        # Manejar errores en caso de fallo en las operaciones de Git
        print("[ERROR] Failed to perform Git operation")
        print("Error:", str(e))

def clone_repo():
    try:
        git.Repo.clone_from(PROJECT_URL, LOCAL_PATH_REPO)
        create_README()
        git_add_commit_push()
        print(f'Repository cloned to local folder "{LOCAL_PATH_REPO}" successfully')
    except Exception as e:
        print("Fore.RED + '[ERROR]' + Failed to perform Git operation")
        print("Error:", str(e))

############ GITHUB REMOTE FUNCTIONS ############
#################################################

def configure_mirror(gitlab_url, gitlab_token, github_url):
    try:
        # Clonar el repositorio de GitLab
        gitlab_repo = git.Repo.clone_from(gitlab_url, "gitlab_repo")
        
        # Configurar el mirror del repositorio de GitLab al repositorio de GitHub
        gitlab_repo.create_remote("mirror", url=github_url)
        gitlab_repo.remotes.mirror.push(mirror=True)
        
        print("Mirror configured successfully")
    except Exception as e:
        print("Failed to configure mirror")
        print("Error:", str(e))

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

    print(LOCAL_PATH_REPO)

    if main_prompt.lower() == 'r':
        print('\u26A0\ufe0f YOU HAVE CHOSEN TO REMOVE THE REPO AND DIRECTORY. ¡¡¡¡THIS ACTION CANNOT BE UNDONE \u26A0\ufe0f !!!!')
        confirm_prompt = input('Are you sure? (y/n)')
        if confirm_prompt == 'y':
            remove_repo()
            remove_local_directory()
        else:
            print('Oh my god you almost messed up')
    else:
        print('YOU HAVE CHOSEN TO CREATE NEW REPO.')
        project = create_repo()
        create_local_directory()
        clone_repo()
    

    
