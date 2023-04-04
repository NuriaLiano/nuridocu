import os, sys, requests, json, git, gitlab

#global vars and const
DNAME = ""
DMODE = 776

#import vars form config file
with open("config.json") as f:
    config = json.load(f)

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
        
        # Send the GET request to get the user ID
        response = requests.get(url, headers=headers)

        # Parse the response JSON and return the user ID
        return response.json()

    except requests.exceptions.RequestException as e:
        print("ERROR | Ha ocurrido un error al obtener el ID de usuario: ", e)
        return None


print(check_repository_exists())
# da error 404 no eneucnetra el repo
