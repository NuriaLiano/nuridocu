import configparser, sys, gitlab, os, git, shutil

#TODO: revisar que pasa con get_token
#TODO: añadir que compruebe el git config y si no le configure
#TODO: revisar para meter las variables importantes en .config
#TODO: preguntar si va a eliminar o crear repo
#TODO: crear fichero con las dependencias que haya que instalar
#pip install gitpython
#pip install python-gitlab
#TODO: al borrar el repo preguntar para borrar la carpeta local


# def get_token():
#     #read config file
#     config = configparser.ConfigParser()
#     config.read('.config')
#     #obtain token
#     print(config.sections())
#     return config.get('gitlab', 'token')

def get_repo_name():
    #read repo_name from parameter
    if len (sys.argv) > 1:
        repo_name = sys.argv[1]
    else:
        while True:
            repo_name = input('Enter the repos name: ')
            if repo_name:
                return repo_name

def create_repo(repo_name, token):
    #create object with token
    gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
    #repo_name = 'eliminar'
    #create new repo
    project = gl.projects.create({'name': repo_name})
    #print url
    print('Check the new repo: ', project.web_url)
    return project

def search_repo(repo_name, token):
    #search project by name
    gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
    projects = gl.projects.list(search=repo_name)
    if not projects:
        print(f'No projects found with name "{repo_name}"')
        return
    return projects[0]

def remove_repo(repo_name, token):
    remove_prompt = input ('Are you sure you want to delete the repository? (y/n)')
    if remove_prompt.lower() == 'y':
        project = search_repo(repo_name, token)
        if project is None:
            print(f'No project found with name "{repo_name}"')
            return
        gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
        gl.projects.delete(project.id)
        print('The repo ' + repo_name + ' has been deleted')
    else:
        print('The repo ' + repo_name + ' has not been deleted')

def remove_local_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        print(f'Directory "{dir_name}" has been deleted')
    else:
        print(f'Directory "{dir_name}" does not exist')

def create_local_directory(dir_name):
    os.mkdir(dir_name)
    print(f'Local folder "{dir_name}" created successfully')

def clone_repo(repo_url, dir_path):
    git.Repo.clone_from(repo_url, dir_path)
    print(f'Repository cloned to local folder "{dir_path}" successfully')

if __name__ == '__main__':
    
    token = ""

    main_prompt = input('Do you want remove or create new repo (r/c)')
    
    # token = get_token()
    repo_name = get_repo_name()

    if main_prompt == 'r':
        print('YOU HAVE CHOSEN TO REMOVE THE REPO AND DIRECTORY. ¡¡¡¡THIS ACTION CANNOT BE UNDONE!!!!')
        confirm_prompt = input('Are you sure? (y/n)')
        if confirm_prompt == 'y':
            remove_repo(repo_name, token)
            remove_local_directory(repo_name)
        else:
            print('Oh my god you almost messed up')
    else:
        print('YOU HAVE CHOSEN TO CREATE NEW REPO.')
        project = create_repo(repo_name, token)
        create_local_directory(repo_name)
        clone_repo(project.http_url_to_repo, repo_name)
    

    
