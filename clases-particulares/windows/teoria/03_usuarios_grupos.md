# Usuarios y grupos con NetUser y Net LocalGroup

NET USER y NET LOCALGROUP son comandos en CMD que se utilizan para administrar usuarios y grupos en Windows.

## NET USER

### Consultar usuarios existentes

~~~bash
NET USER
~~~

### Consultar información del usuario

~~~bash
NET USER [nombre de usuario]
~~~

### Cambiar la contraseña a un usuario

~~~bash
NET USER [nombre de usuario] [contraseña]
~~~

### Crear una cuenta de usuario

~~~bash
NET USER [nombre de usuario] [contraseña] /ADD
~~~

### Eliminar una cuenta de usuario

~~~bash
NET USER [nombre de usuario] /DELETE
~~~

## NET LOCALGROUP

### Consultar grupos existentes

~~~bash
NET LOCALGROUP
~~~

### Consultar usuarios pertenecientes a un grupo

~~~bash
NET LOCALGROUP [nombre de grupo] /USERS
~~~

### Crear un grupo

~~~bash
NET LOCALGROUP [nombre de grupo] /ADD
~~~

### Añadir usuario a un grupo

~~~bash
NET LOCALGROUP [nombre de grupo] [nombre de usuario] /ADD
~~~

### Eliminar usuario de un grupo

~~~bash
NET LOCALGROUP [nombre de grupo] [nombre de usuario] /DELETE
~~~

### Eliminar un grupo

~~~bash
NET LOCALGROUP [nombre de grupo] /DELETE
~~~
