import gitlab
import git

# Define el nombre de usuario y correo electrónico que se esperan
EXPECTED_USERNAME = "NuriaLiano"
EXPECTED_EMAIL = "nuria.gutierrezliano@unican.es"

# Inicializa el repositorio local y verifica el nombre de usuario y correo electrónico
repo = git.Repo.init("path/to/repo")
if repo.config_reader().get_value("user", "name") != EXPECTED_USERNAME:
    raise ValueError("El nombre de usuario no coincide con el esperado")
if repo.config_reader().get_value("user", "email") != EXPECTED_EMAIL:
    raise ValueError("El correo electrónico no coincide con el esperado")

# Crea un cliente GitLab y autentica con una clave privada
gl = gitlab.Gitlab('https://gitlab.com', private_token='user-access')

# # Crea un nuevo proyecto en GitLab
project = gl.projects.create({'name': 'eliminar2'})

# Clona el proyecto recién creado en la carpeta local
git.Repo.clone_from(project.ssh_url_to_repo, "/home/glianon/gitlab/eliminar2")