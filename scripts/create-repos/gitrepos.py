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

#global const
DNAME = ""
DMODE = 776
GITPATH = "/home/glianon/gitlab/"

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
        print(os.path.exists(GITPATH + DNAME))
        return os.path.exists(GITPATH + DNAME)
    except FileExistsError():
        print("ERROR | El directorio ya existe") 

def createDirectory():
    try:
        return os.mkdir(GITPATH + DNAME, DMODE)
    except FileExistsError():
        print("ERROR | El directorio ya existe") 
    
#verify that a folder name has been passed as a parameter
if len(sys.argv) < 2:
    #order the folder name
    print("Dime el nombre del repositorio: ")
    DNAME = replaceSpaces(input())
    while existsDirectory():
        DNAME = replaceSpaces(input())
    createDirectory()
    print(os.listdir(GITPATH))
    print("CORRECTO. El directorio se ha creado")
else:
    #extract repo name for the arguments
    DNAME = replaceSpaces(sys.argv[1])
    if (existsDirectory()):
        createDirectory()
        print("CORRECTO | El directorio se ha creado")




    




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