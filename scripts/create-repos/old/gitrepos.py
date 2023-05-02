import os
import sys
import requests
import json
import gitlab

#import vars
with open('scripts/create-repos/config.json', 'r') as f:
    config = json.load(f)

#global vars and const
DNAME = ""
DMODE = 776
GITPATH = config['GITPATH']
GITLAB_USER = config['GITLAB_USER']

# GitLab API URL and token
GITLAB_URL = config['GITLAB_URL']
GITLAB_TOKEN = config['GITLAB_TOKEN']
# GitLab project namespace
NAMESPACE = config['NAMESPACE']
# GitLab repository default branch name
DEFAULT_BRANCH = config['DEFAULT_BRANCH']
# GitLab repository visibility
VISIBILITY = config['VISIBILITY']
#Gitlab username
USERNAME = config['GITLAB_USER']
INSTANCE = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)
#1. CREATE REPO IN GITLAB
#2. CLONE GITLAB REPO ON LOCAL
#3. CONFIG GIT INIT
#3. CREATE README
#4. COMMIT 
#5. PUSH


def createDirectory():
    try:
        return os.mkdir(GITPATH + DNAME, DMODE)
    except FileExistsError():
        print("ERROR | El directorio ya existe") 

def find_gitlab_repo():
    instance = gitlab.Gitlab('https://gitlab.com', private_token=GITLAB_TOKEN)

    #search all project with the same name
    projects = instance.projects.list(search='nuridocu')

    #filter the list with the name
    for project in projects:
        if project.path_with_namespace == f"Nuria_Liano/eliminar":
            return project
    
    return None


def createLocalRepo():
    #verify that a folder name has been passed as a parameter
    if len(sys.argv) < 2:
        #order the folder name
        print("Dime el nombre del repositorio: ")
        DNAME = replaceSpaces(input())
        while existsDirectory():
            print("Prueba con otro nombre: ")
            DNAME = replaceSpaces(input())
        createDirectory()
        #print(os.listdir(GITPATH))
        print("CORRECTO. El directorio se ha creado")
    else:
        #extract repo name for the arguments
        DNAME = replaceSpaces(sys.argv[1])
        while existsDirectory():
            print("Prueba con otro nombre: ")
            DNAME = replaceSpaces(input())
        createDirectory()
        #print(os.listdir(GITPATH))
        print("CORRECTO. El directorio se ha creado")

# def get_user_id(username):
#     try:
#         # Set the API endpoint  
#         url = GITLAB_URL + "users?username="+username
        
#         #set the request headers and data
#         headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
        
#         # Send the GET request to get the user ID
#         response = requests.get(url, headers=headers)


# def checkRepoNameExits():
#     #1. like param
#     #2. ask to user
#     #3. set default dname 

#     if(len(sys.argv) >= 2):
#         DNAME = sys.argv[1]
#     #else:
#         #chequear si existe el repo en gitlab

#         #chequear si existe la carpeta en local


# def createGitLabRepo():
#     try:
#         #set endpoint API
#         url = GITLAB_URL + "/projects"

#         #set the request headers and data
#         headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
#         data = {
#             "name": DNAME,
#             "namespace": {
#                 "id": NAMESPACE
#             },
#             "default_branch": DEFAULT_BRANCH,
#             "visibility": VISIBILITY
#         }

#         #send the POST request to create the repo
#         response = requests.post(url, headers=headers, data=data)

#         #debug to fic error with request to API
#         #print(response.status_code)
#         #print(response.json())

#         #check if the request was succesfull
#         if response.status_code == 201:
#             return True
#         else:
#             print("ERROR | The GitLab Repository could not be created")
#             return False
#     except requests.exceptions.RequestException as e:
#         print("ERROR | An error occurred while creating the repo: ", e)
#         return False

#checkRepoNameExits()
def check_repository_exists():
    try:
        # Set the API endpoint  
        url = GITLAB_URL + "users?username=Nuria_Liano"
        
        #set the request headers and data
        headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
        data = {
            "name": DNAME,
            "namespace": {
                "id": NAMESPACE
            },
            "default_branch": DEFAULT_BRANCH,
            "visibility": VISIBILITY
        }

        #send the POST request to create the repository
        response = requests.post(url, headers=headers, data=data)

        #debug to fix errors with api
        #print(response.status_code)
        #print(response.json())

        #check if the request was successful
        if response.status_code == 201:
            return True
        else:
            print("ERROR | No se ha podido crear el repositorio en GitLab")
            return False
    except requests.exceptions.RequestException as e:
        print("ERROR | Ha ocurrido un error al crear el repositorio: ", e)
        return False

def cloneGitlabRepo():
    try:
        #create instance
        instance = gitlab.Gitlab('https://gitlab.com', private_token='glpat-Xx2Gj7v4F5jMp9Sy75uz')

        #search gitlab repo
        project = instance.projects.get('44773891')

        # #clone gitlab repo
        # result = project.repository_archive(prefix=None, path="/home/glianon/gitlab/")

        # print(result)
        tree = project.repository_tree()

        # loop through the tree and download each file
        for item in tree:
            if item["type"] == "blob":
                file_content = project.repository_raw(file_path=item["path"], ref="master")
                with open("/home/glianon/gitlab/" + item["path"], "wb") as f:
                    f.write(file_content)
    except Exception as e:
        print("Error:", e)

def createInitialReadme():

    # Crear archivo README.md en la carpeta local del repositorio
    with open(os.path.join(GITPATH, DNAME, "README.md"), "w") as f:
        f.write("# " + DNAME)

    # Agregar archivo README.md al repositorio local
    os.system(f"cd {os.path.join(GITPATH, DNAME)} && git add README.md")

    # Hacer un commit y push al repositorio remoto
    os.system(f"cd {os.path.join(GITPATH, DNAME)} && git commit -m 'Agregando archivo README.md' && git push")


def main():
    # createLocalRepo()
    # createGitLabRepo()
    # createInitialReadme()
    print(cloneGitlabRepo())
    # print(find_gitlab_repo())



main()
