
# Ejercicios disparadores

Crear un disparador para cada una de las siguientes situaciones:

- Queremos que cada vez que un vendedor realice una venta, el importe del pedido se sume a las ventas que hasta ahora tenía el vendedor.
- Queremos que cada vez que un vendedor realice una venta y esta (por el disparador anterior) se haya sumado a las ventas que hasta ahora tenía el vendedor, también se actualice el campo de ventas de la oficina a la que pertenece el vendedor.
- Si un cliente realiza una compra, debemos disminuir la cantidad de crédito que tiene el cliente.
- Si un cliente intenta realizar una compra que supera su límite de crédito, la base de datos no debe permitir la compra.
- Si intentamos realizar un pedido de un producto en particular, pero la cantidad solicitada supera el número de unidades en stock, la base de datos no debe permitirlo.
- La base de datos debe actualizar automáticamente la cantidad de productos en stock al realizar una venta.
- Crear una tabla llamada "RepVenDesp", donde cada vez que se elimine un vendedor de la base de datos, sus datos se copien a esta tabla, incluyendo la fecha en que se le ha dado de baja.
- Crear una función para avisar al usuario cuando queden pocas existencias de un determinado producto (<10). Se verificará si las existencias en stock, una vez disminuidas, son inferiores a 10 y, en caso afirmativo, se notificará al usuario.

Recuerda que estos disparadores y funciones se pueden implementar en PostgreSQL utilizando el lenguaje plpgsql.
