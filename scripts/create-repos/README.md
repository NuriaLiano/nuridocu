# GITREPOS: Automate Your Repository Management with Python Script

## What is GITREPOS?

GITREPOS is a Python script designed to streamline and automate a process that can be slow and tedious when done through the graphical interface. It allows you to create and delete repositories on GitLab and GitHub, as well as set up a local directory with an initial README. Once the process is complete, it establishes a mirror between the GitLab and GitHub repositories, ensuring that both are exact copies. Any changes made to one repository will be replicated to the other using CI/CD.

## How does GITREPOS work?

The program provides a command-line interface (CLI) that allows you to execute various actions with ease. Some of its main functionalities include:

1. Repository creation: With just a few commands, GITREPOS enables you to create repositories on both GitLab and GitHub. You can specify the repository name, privacy settings, and other relevant details. The script handles the API requests and automates the repository creation process.

2. Repository deletion: If you no longer need a repository, GITREPOS allows you to delete it quickly. Simply provide the repository name and the platform (GitLab or GitHub) it belongs to, and the script will securely remove it.

3. Mirror configuration: One of GITREPOS' standout features is the ability to establish a mirror between a GitLab repository and a GitHub repository. This means that any changes made in either repository will automatically be replicated to the other. The mirror configuration is particularly useful if you want to maintain identical copies of your project on both platforms and ensure continuous synchronization of changes.

4. CI/CD integration: By automating the repository creation and configuration process, GITREPOS saves you time and effort when implementing CI/CD (Continuous Integration/Continuous Delivery) in your development workflow. You can leverage the CI/CD capabilities offered by GitLab and GitHub to automate testing, building, and deploying efficiently.

In addition to these core functionalities, GITREPOS provides additional options for customization, allowing you to tailor its behavior to your specific needs. You can configure authentication using access tokens to interact with the GitLab and GitHub APIs, set default privacy options, and more.

## Install and usage

If you consider yourself an expert Linux user you can take your own decision on how to install the requirements.
But anyway, we recommend that you follow these steps.

### Clone or download the repo

#### Clone the repository

>:warning:**CAUTION** You must install git on your local system before following these steps

##### from GITLAB

~~~ps
git clone git@gitlab.com:Nuria_Liano/gitrepos.git
~~~

##### from GITHUB

~~~ps
git clone git@github.com:NuriaLiano/gitrepos.git
~~~

#### Download

You can download the code by ZIP, tar.gz, tar.bz2 or tar

##### GITLAB

[ZIP](https://gitlab.com/Nuria_Liano/gitrepos/-/archive/main/gitrepos-main.zip)
[TAR.GZ](https://gitlab.com/Nuria_Liano/gitrepos/-/archive/main/gitrepos-main.tar.gz)
[TAR.BZ2](https://gitlab.com/Nuria_Liano/gitrepos/-/archive/main/gitrepos-main.tar.bz2)
[TAR](https://gitlab.com/Nuria_Liano/gitrepos/-/archive/main/gitrepos-main.tar)

##### GITHUB

[ZIP](https://github.com/NuriaLiano/gitrepos/archive/refs/heads/main.zip)
[GITHUB DESKTOP](x-github-client://openRepo/https://github.com/NuriaLiano/gitrepos)

### Install requirements

>:warning:**CAUTION** You must install python and pip in your local system before following this steps

~~~sh
pip install -r requirements.txt
~~~

>:pencil: **NOTE** If you want generete your own requirements file
> ```pip freeze > requirements.txt```

### Execute

Once you follow this steps, you can execute the script.

>:warning: **CAUTION** your python path installation may be different

~~~sh
python3.11 gitrepos.py
~~~

## Contributors

Up to date:

**NuriaLiano**

![@Nuria_Liano](https://gitlab.com/uploads/-/system/user/avatar/7736983/avatar.png?width=400)
![@NuriaLiano](https://avatars.githubusercontent.com/u/74002643?v=4)

## License

Todos los documentos reflejados en este repositorio están bajo la licencia [Creative Commons Atribución-NoComercial (CC BY-NC)](https://creativecommons.org/licenses/by-nc/4.0/)

Se permite la distribución gratuita de este archivo y su contenido, siempre y cuando se cumplan las siguientes condiciones:

- Se debe mantener intacta la información de derechos de autor y propiedad intelectual y se debe incluir una nota de atribución al autor original en cualquier distribución del archivo.
- No se permite la venta de este archivo o de cualquier contenido incluido en él, ya sea en su forma original o modificada.
- No se permite la modificación del archivo original o de cualquier contenido incluido en él, sin el permiso expreso del autor original.

Cualquier violación de estas condiciones será considerada una infracción de los derechos de autor y propiedad intelectual, y se tomarán las medidas legales apropiadas para proteger los intereses del autor original.

Gracias por tu comprensión y cumplimiento de estas condiciones.