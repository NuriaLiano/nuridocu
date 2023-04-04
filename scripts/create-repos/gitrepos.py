#TODO: check if ssh key is enable on gitlab and github
#ensure if git init config is ok
#create directory
#create readme
#create repo in gitlab
#git add
#git commit
#git push

import os
import sys
import requests
import json

#import vars
with open('config.json', 'r') as f:
    config = json.load(f)

#global const
DNAME = ""
DMODE = 776
#GITPATH = "/home/glianon/gitlab/"
GITPATH = config['GITPATH']

# GitLab API URL and token
GITLAB_URL = config['GITLAB_URL']
GITLAB_TOKEN = config['GITLAB_TOKEN']
# GitLab project namespace
NAMESPACE = config['NAMESPACE']
# GitLab repository default branch name
DEFAULT_BRANCH = config['DEFAULT_BRANCH']
# GitLab repository visibility
VISIBILITY = config['VISIBILITY']

#change spaces for lines
def replaceSpaces(reponame):
    try:
        global DNAME
        DNAME = reponame.replace(" ", "-")
        return DNAME
    except ValueError():
        print("ERROR | Ha ocurrido un error al formatear el nombre del repo") 

#check if that directory exists
def existsDirectory():
    try:
        return os.path.exists(GITPATH + DNAME)
    except FileExistsError():
        print("ERROR | El directorio ya existe") 

def createDirectory():
    try:
        return os.mkdir(GITPATH + DNAME, DMODE)
    except FileExistsError():
        print("ERROR | El directorio ya existe") 
    
def createLocalRepo():

    !IMPORTANTE PRIMERO HAY QUE HACER UN CLONE DEL REPO DE GITLAB EN LOCAL, NO VALE CREAR LA CARPETA PRIMERO¡

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

#         # Parse the response JSON and return the user ID
#         return response.json()[0]["id"]

#     except requests.exceptions.RequestException as e:
#         print("ERROR | Ha ocurrido un error al obtener el ID de usuario: ", e)
#         return None

# def namespace_exists(username):
#     try:
#         # Get the user ID
#         user_id = get_user_id(username)

#         # Set the API endpoint
#         url = GITLAB_URL + "users/" + str(user_id) + "/projects"

#         # Set the request headers
#         headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}

#         # Send the GET request to get the projects for the user
#         response = requests.get(url, headers=headers)

#         # Parse the response JSON and check if any project has the namespace equal to the username
#         projects = response.json()
#         for project in projects:
#             if project["namespace"]["name"] == username:
#                 return True

#         return False
#     except requests.exceptions.RequestException as e:
#         print("ERROR | Ha ocurrido un error al obtener los proyectos del usuario: ", e)
#         return False

def createGitLabRepo():
    try:
        # Set the API endpoint  
        url = GITLAB_URL + "/projects"

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

def gitInitLocalRepo():


def createInitialReadme():

    # Crear archivo README.md en la carpeta local del repositorio
    with open(os.path.join(GITPATH, DNAME, "README.md"), "w") as f:
        f.write("# " + DNAME)

    # Agregar archivo README.md al repositorio local
    os.system(f"cd {os.path.join(GITPATH, DNAME)} && git add README.md")

    # Hacer un commit y push al repositorio remoto
    os.system(f"cd {os.path.join(GITPATH, DNAME)} && git commit -m 'Agregando archivo README.md' && git push")


def main():
    createLocalRepo()
    createGitLabRepo()
    createInitialReadme()

main()

    




# import subprocess

# # Ejecutamos el comando git config --list y obtenemos la salida como una cadena
# output = subprocess.check_output(["git", "config", "--list"]).decode("utf-8")

# # Creamos un diccionario para almacenar las variables de configuración
# config_vars = {}

# # Analizamos la salida y almacenamos cada variable en el diccionario
# for line in output.split("\n"):
#     if line.strip() == "":
#         continue
#     key, value = line.split("=")
#     config_vars[key.strip()] = value.strip()

# # Verificamos que el nombre de usuario y el correo electrónico sean correctos
# username = config_vars.get("user.name")
# email = config_vars.get("user.email")
# if not username or not email:
#     print("No se encontró el nombre de usuario o el correo electrón