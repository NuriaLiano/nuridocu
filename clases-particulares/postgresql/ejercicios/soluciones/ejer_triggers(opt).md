# Ejercicios disparadores

~~~sql
CREATE DATABASE registro_eventos;
\c registro_eventos;
CREATE TABLE eventos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
~~~

## Ejercicio 1. Simular una aplicación de registro de eventos y enviar notificaciones cuando se inserta un nuevo evento

~~~sql
CREATE OR REPLACE FUNCTION enviar_notificacion()
    RETURNS TRIGGER AS $$
BEGIN
    PERFORM pg_notify('nueva_notificacion', 'Se ha insertado un nuevo evento: ' || NEW.nombre);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER despues_insertar_evento
AFTER INSERT ON eventos
FOR EACH ROW
EXECUTE FUNCTION enviar_notificacion();
~~~

** PARA PROBAR **

1. Insertar datos en tabla 'eventos'

~~~sql
INSERT INTO eventos (nombre) VALUES
    ('Evento A'),
    ('Evento B'),
    ('Evento C');
~~~

2. Escuchar las notificaciones en otro cliente PostgreSQL

En otra ventana o cliente de PostgreSQL, puedes ejecutar el siguiente comando para escuchar las notificaciones y ver los mensajes cuando se inserten nuevos eventos:

~~~sql
LISTEN nueva_notificacion;
~~~

Después de esto, cualquier notificación enviada en el canal "nueva_notificacion" se mostrará en esta ventana.

3. Insertar nuevo evento y verificar la recepcion de la notificacion

~~~sql
INSERT INTO eventos (nombre) VALUES ('Nuevo Evento');
~~~

En la ventana donde se está escuchando las notificaciones, deberías ver el mensaje de notificación que indica que se ha insertado un nuevo evento.

## Ejercicio 2. 