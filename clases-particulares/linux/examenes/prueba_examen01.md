# Prueba de examen 01

## Instrucciones

- Escribe las ordenes necesarias para realizar las tareas en Bash
- Debes escribir una orden en cada caso, a no ser que se indique lo contrario
- Añade 5 discos duros virtuales de 10GB a tu máquina. Utiliza los siguientes nombres: ex1.vdi, ex2.vdi, ex3.vdi, ex4.vdi y ex5.vdi
- Utiliza rutas relativas, a no ser que se indique lo contrario

## 1. Muestra el contenido de tu directorio activo

## 2. Crea una directorio 'SCRIPTS_exa' en tu home

## 3. Utiliza el directorio que acabas de crear como directorio activo para el examen

## 4. Crea un script 'auto_usuarios.sh' para automatizar la creación de cuenta de usuarios y grupos. El script tendra que validar si en el fichero de autenticación de fichero de Linux existe el usuario y tiene los parámetros correctos que recogerá por parámetro al ejecutar el script

- Si el usuario existe
  - pedir el grupo. NO existe
    - bucle de pedir grupo hasta acertar
      - mostrar mensaje
  - pedir grupo existe
    - mostrar mensaje
- Si el usuario no existe
  - pedir todos los parametros para crear home, grupo y usuario
  - crear mkdir home del usuario
  - crear grupo
  - crear usuario
  - añadir username y fecha de creacion a un fichero usu_creados
  - mensaje donde se vea el usuario, la contraseña por defecto y un aviso de que se va a pedir cambia al iniciar.


### En caso de que el usuario exista deberás de mostrar un mensaje 'El usuario ya existe' y pedir por teclado que introduzcan el grupo

#### Si el grupo es correcto con lo que está en el fichero de usuarios deberá mostrar un mensaje de 'El usuario y el grupo introducido es correcto y ya existe', seguidamente lanzará un proceso de terminal

#### Si el grupo no es correcto pedirá en bucle el grupo hasta que se acierte el grupo correcto, una vez acertado ejecutará los mismos pasos que si se acierta inicialmente

### En caso de que el usuario no exista deberá solicitar toda la información relevante acerca del usuario a crear y realizar todos los pasos previos para poder crear el usuario

>:black_joker: **PISTA** deberás usar el comando useradd

## 5. Crea estas particiones y formatos en el primero disco extra
- primaria 3gb ext4
- primaria 2gb ntfs
- logica 2 gb fat32
- logica 1gb ext3
- logica 2 ext4

## 6. Crea un 