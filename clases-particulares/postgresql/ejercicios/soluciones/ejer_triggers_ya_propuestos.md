
# Ejercicios disparadores

~~~sql
CREATE DATABASE tienda;
\c tienda;
CREATE TABLE vendedores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ventas NUMERIC(8, 2)
);

CREATE TABLE oficinas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ventas NUMERIC(8, 2)
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    credito NUMERIC(8, 2)
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    stock INTEGER
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    fecha DATE,
    vendedor_id INTEGER,
    cliente_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    importe NUMERIC(8, 2),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores (id),
    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
    FOREIGN KEY (producto_id) REFERENCES productos (id)
);

CREATE TABLE RepVenDesp (
    id SERIAL PRIMARY KEY,
    fecha DATE,
    vendedor_id INTEGER,
    nombre VARCHAR(100),
    ventas NUMERIC(8, 2)
);
INSERT INTO vendedores (nombre, ventas) VALUES
    ('Vendedor 1', 0),
    ('Vendedor 2', 0);

INSERT INTO oficinas (nombre, ventas) VALUES
    ('Oficina 1', 0),
    ('Oficina 2', 0);

INSERT INTO clientes (nombre, credito) VALUES
    ('Cliente 1', 1000),
    ('Cliente 2', 500);

INSERT INTO productos (nombre, stock) VALUES
    ('Producto 1', 20),
    ('Producto 2', 10);

INSERT INTO ventas (fecha, vendedor_id, cliente_id, producto_id, cantidad, importe) VALUES
    ('2023-05-01', 1, 1, 1, 3, 50.99),
    ('2023-05-02', 2, 2, 2, 2, 25.99);
~~~

Crear un disparador para cada una de las siguientes situaciones:

- Queremos que cada vez que un vendedor realice una venta, el importe del pedido se sume a las ventas que hasta ahora tenía el vendedor.

~~~sql
-- Disparador 1: Actualizar las ventas del vendedor al realizar una venta
CREATE OR REPLACE FUNCTION actualizar_ventas_vendedor()
    RETURNS TRIGGER
    AS $$
    BEGIN
        UPDATE vendedores
        SET ventas = ventas + NEW.importe
        WHERE id = NEW.vendedor_id;
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER actualizar_ventas_vendedor_trigger
    AFTER INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_ventas_vendedor();
~~~

- Queremos que cada vez que un vendedor realice una venta y esta (por el disparador anterior) se haya sumado a las ventas que hasta ahora tenía el vendedor, también se actualice el campo de ventas de la oficina a la que pertenece el vendedor.

~~~sql
-- Disparador 2: Actualizar las ventas de la oficina al realizar una venta
CREATE OR REPLACE FUNCTION actualizar_ventas_oficina()
    RETURNS TRIGGER
    AS $$
    BEGIN
        UPDATE oficinas
        SET ventas = ventas + NEW.importe
        WHERE id = (SELECT vendedor_id FROM vendedores WHERE id = NEW.vendedor_id);
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER actualizar_ventas_oficina_trigger
    AFTER INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_ventas_oficina();
~~~

- Si un cliente realiza una compra, debemos disminuir la cantidad de crédito que tiene el cliente.

~~~sql
-- Disparador 3: Disminuir el crédito del cliente al realizar una compra
CREATE OR REPLACE FUNCTION disminuir_credito_cliente()
    RETURNS TRIGGER
    AS $$
    BEGIN
        UPDATE clientes
        SET credito = credito - NEW.importe
        WHERE id = NEW.cliente_id;
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER disminuir_credito_cliente_trigger
    AFTER INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION disminuir_credito_cliente();
~~~

- Si un cliente intenta realizar una compra que supera su límite de crédito, la base de datos no debe permitir la compra.

~~~sql
-- Disparador 4: Evitar compras que excedan el límite de crédito del cliente
CREATE OR REPLACE FUNCTION verificar_limite_credito()
    RETURNS TRIGGER
    AS $$
    BEGIN
        IF NEW.importe > (SELECT credito FROM clientes WHERE id = NEW.cliente_id) THEN
            RAISE EXCEPTION 'La compra excede el límite de crédito del cliente';
        END IF;
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER verificar_limite_credito_trigger
    BEFORE INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION verificar_limite_credito();
~~~

- Si intentamos realizar un pedido de un producto en particular, pero la cantidad solicitada supera el número de unidades en stock, la base de datos no debe permitirlo.

~~~sql
-- Disparador 5: Evitar compras que superen el stock disponible
CREATE OR REPLACE FUNCTION verificar_stock_disponible()
    RETURNS TRIGGER
    AS $$
    BEGIN
        IF NEW.cantidad > (SELECT stock FROM productos WHERE id = NEW.producto_id) THEN
            RAISE EXCEPTION 'La compra supera el stock disponible del producto';
        END IF;
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER verificar_stock_disponible_trigger
    BEFORE INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION verificar_stock_disponible();

--opcion con variable
CREATE OR REPLACE FUNCTION verificar_limite_credito()
    RETURNS TRIGGER
    AS $$
    DECLARE
        credito_cliente NUMERIC(8, 2);
    BEGIN
        SELECT credito INTO credito_cliente FROM clientes WHERE id = NEW.cliente_id;
        
        IF NEW.importe > credito_cliente THEN
            RAISE EXCEPTION 'La compra supera el límite de crédito del cliente.';
        END IF;
        
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER verificar_limite_credito_trigger
    BEFORE INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION verificar_limite_credito();
~~~

- La base de datos debe actualizar automáticamente la cantidad de productos en stock al realizar una venta.

~~~sql
-- Disparador 6: Actualizar la cantidad de productos en stock al realizar una venta
CREATE OR REPLACE FUNCTION actualizar_stock_venta()
    RETURNS TRIGGER
    AS $$
    BEGIN
        UPDATE productos
        SET stock = stock - NEW.cantidad
        WHERE id = NEW.producto_id;
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER actualizar_stock_venta_trigger
    AFTER INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_stock_venta();
~~~

- Crear una tabla llamada "RepVenDesp", donde cada vez que se elimine un vendedor de la base de datos, sus datos se copien a esta tabla, incluyendo la fecha en que se le ha dado de baja.

~~~sql
-- Disparador 7: Copiar los datos de un comercial eliminado en la tabla "RepVenDesp"
CREATE OR REPLACE FUNCTION copiar_datos_comercial()
    RETURNS TRIGGER
    AS $$
    BEGIN
        INSERT INTO RepVenDesp (id, nombre, fecha_salida)
        VALUES (OLD.id, OLD.nombre, current_date);
        RETURN OLD;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER copiar_datos_comercial_trigger
    AFTER DELETE ON comerciales
    FOR EACH ROW
    EXECUTE FUNCTION copiar_datos_comercial();
~~~

- Crear una función para avisar al usuario cuando queden pocas existencias de un determinado producto (<10). Se verificará si las existencias en stock, una vez disminuidas, son inferiores a 10 y, en caso afirmativo, se notificará al usuario.

~~~sql
-- Disparador 8: Función para avisar al usuario cuando quedan pocas existencias de un producto
CREATE OR REPLACE FUNCTION verificar_existencias()
    RETURNS TRIGGER
    AS $$
    DECLARE
        stock_actual INTEGER;
    BEGIN
        SELECT stock INTO stock_actual
        FROM productos
        WHERE id = NEW.producto_id;
        
        IF stock_actual < 10 THEN
            RAISE NOTICE 'Quedan pocas existencias del producto %', NEW.producto_id;
        END IF;
        
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER verificar_existencias_trigger
    AFTER INSERT ON ventas
    FOR EACH ROW
    EXECUTE FUNCTION verificar_existencias();
~~~

Recuerda que estos disparadores y funciones se pueden implementar en PostgreSQL utilizando el lenguaje plpgsql.
