import configparser, sys, gitlab, os, git, shutil

#TODO: NO FUNCIONA POR QUE LAS RUTAS ESTAN MAL, TIENES QUE REVISAR DESDE DONDE SE EJECUTA EL SCRIPT Y FIJAR UNA UBICACION FIJA QUE SE PUEDA MODIFICAR EN EL CONFIG
#TODO: añadir que compruebe el git config y si no le configure
#TODO: al borrar el repo preguntar para borrar la carpeta local

def load_config():

    #global vars
    global GL_TK, URL_GL, INSTANCE_GL, USERNAME_GL, CONFIG_PATH

    #request config path
    config_path = input(Fore.CYAN + 'Enter the .config path: ')

    #read config file
    config = configparser.ConfigParser()
    config.read(config_path)
    #obtain token
    GL_TK = config.get('DEFAULT', 'GL_TOKEN')
    URL_GL = config.get('DEFAULT', 'URL_GL')
    INSTANCE_GL = gitlab.Gitlab('https://gitlab.com', private_token=GL_TK)


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
    while True:
        local_dir_input = input(Fore.CYAN + 'Enter the local path: ')
        if local_dir_input != '':
            LOCAL_PATH_REPO = local_dir_input.replace(' ', '-')
            #LOCAL_PATH_REPO = os.path.join(local_dir_input, REPO_NAME)
            # C:\Users\nuria-msi\gitlab\eliminar
            print("esta ejecuandose en ", local_dir_input)
            break
        elif local_dir_input == '':
            LOCAL_PATH_REPO = REPO_NAME
            break

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

def remove_local_directory():
    print("Directorio de trabajo actual:", os.getcwd())
    print("Directorio LOCAL de trabajo actual:", LOCAL_PATH_REPO)
    if os.path.exists(LOCAL_PATH_REPO):
        shutil.rmtree(LOCAL_PATH_REPO)
        print(f'Directory "{LOCAL_PATH_REPO}" has been deleted')
    else:
        print(Fore.RED + '[ERROR]' + f'Directory "{LOCAL_PATH_REPO}" does not exist')

def create_local_directory():
    os.mkdir(LOCAL_PATH_REPO)
    print(f'Local folder "{LOCAL_PATH_REPO}" created successfully')

def clone_repo():
    git.Repo.clone_from(PROJECT_URL, LOCAL_PATH_REPO)
    print(f'Repository cloned to local folder "{LOCAL_PATH_REPO}" successfully')

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

    if main_prompt == 'r':
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
    

    
