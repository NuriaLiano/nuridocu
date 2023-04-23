# Directivas de seguridad

Las directivas (también conocidas como políticas o políticas de grupo) en Windows son un conjunto de reglas y configuraciones que permiten a los administradores de sistemas establecer y aplicar políticas de seguridad, gestión de recursos y otras configuraciones en los equipos y usuarios de una red de manera centralizada.

Pueden ser configuradas en un controlador de dominio de Windows y aplicadas a todos los equipos y usuarios de la red que estén unidos al dominio. También es posible configurar directivas de forma local en cada equipo individualmente.

Son una herramienta útil para los administradores de sistemas ya que permiten una gestión centralizada y coherente de la seguridad y configuración de los equipos y usuarios de una red.

## Directivas de seguridad de contraseñas

Son un conjunto de reglas y configuraciones que se utilizan para establecer políticas de seguridad en relación a las contraseñas de usuario en una red de ordenadores. Su objetivo es mejorar la seguridad de la red y proteger la información y recursos sensibles.

- **Longitud mínima de contraseña** (Si se pone a 0 se permiten contraseñas en blanco. No se recomienda.)
- **Almacenar contraseñas con cifrado reversible**: Esta directiva determina si se permite o no que las contraseñas se almacenen con un cifrado que pueda ser revertido, lo que significa que se pueda conocer la contraseña real. Por motivos de seguridad, se recomienda no activar esta opción.
- **Complejidad de la contraseña** (uso de mayúsculas, minúsculas, números, símbolos, etc.)
  - No contener el nombre de usuario o partes del mismo
  - Longitud mínima de 6 caracteres
  - Incluir al menos 3 de lo siguiente: mayúsculas, minúsculas, números y símbolos.
- **Periodo de validez de la contraseña**
- **Vigencia máxima de la contraseña**: Esta directiva determina el tiempo que una contraseña puede ser utilizada antes de que se requiera cambiarla.
- **Vigencia mínima de la contraseña**: Esta directiva establece el tiempo que debe transcurrir antes de que un usuario pueda cambiar su contraseña después de haberla cambiado recientemente.
- **Historial de contraseñas** (no permitir reutilización de contraseñas antiguas)

## Directivas de bloqueo de cuenta

Las directivas de bloqueo de cuenta son un conjunto de configuraciones de seguridad que permiten a los administradores de sistemas establecer reglas y restricciones en cuanto al acceso a cuentas de usuario de una red.

Estas directivas ayudan a prevenir accesos no autorizados o ataques de fuerza bruta al establecer restricciones en el número de intentos de inicio de sesión permitidos antes de que una cuenta sea bloqueada.

- **Duración del bloqueo de cuenta**: establece la cantidad de tiempo que una cuenta bloqueada permanecerá bloqueada antes de desbloquearse automáticamente.
- **Restablecer el bloqueo de cuenta después de**: establece el tiempo que debe pasar después de un intento de inicio de sesión incorrecto para que el contador de intentos de inicio de sesión incorrectos se restablezca en cero.
- **Umbral de bloqueo de cuenta**: establece el número máximo de intentos de inicio de sesión incorrectos permitidos antes de que una cuenta sea bloqueada.
