DROP TABLE IF EXISTS venta;
CREATE TABLE IF NOT EXISTS venta (
  IdVenta				INTEGER,
  Fecha 				DATE NOT NULL,
  Fecha_Entrega 		DATE NOT NULL,
  IdCanal				INTEGER, 
  IdCliente			INTEGER, 
  IdSucursal			INTEGER,
  IdEmpleado			INTEGER,
  IdProducto			INTEGER,
  Precio				FLOAT,
  Cantidad			INTEGER
);
DROP TABLE IF EXISTS canal_venta;
CREATE TABLE IF NOT EXISTS canal_venta (
  IdCanal				INTEGER,
  Canal 				VARCHAR(50)
);
DROP TABLE IF EXISTS cliente;
CREATE TABLE IF NOT EXISTS cliente (
	ID					INTEGER,
	Provincia			VARCHAR(50),
	Nombre_y_Apellido	VARCHAR(80),
	Domicilio			VARCHAR(150),
	Telefono			VARCHAR(30),
	Edad				VARCHAR(5),
	Localidad			VARCHAR(80),
	X					VARCHAR(30),
	Y					VARCHAR(30),
	col10				VARCHAR(1)
);
DROP TABLE IF EXISTS producto;
CREATE TABLE IF NOT EXISTS producto (
	IdProducto					INTEGER,
	Concepto					VARCHAR(100),
	Tipo						VARCHAR(50),
	Precio						FLOAT
);
DROP TABLE IF EXISTS sucursal;
CREATE TABLE IF NOT EXISTS sucursal (
	ID			INTEGER,
	Sucursal	VARCHAR(40),
	Domicilio	VARCHAR(150),
	Localidad	VARCHAR(80),
	Provincia	VARCHAR(50),
	Latitud2	VARCHAR(30),
	Longitud2	VARCHAR(30)
);
DROP TABLE IF EXISTS `calendario`;
CREATE TABLE calendario (
        id                      INTEGER PRIMARY KEY,  -- year*10000+month*100+day
        fecha                 	DATE NOT NULL,
        anio                    INTEGER NOT NULL,
        mes                   	INTEGER NOT NULL, -- 1 to 12
        dia                     INTEGER NOT NULL, -- 1 to 31
        trimestre               INTEGER NOT NULL, -- 1 to 4
        semana                  INTEGER NOT NULL, -- 1 to 52/53
        dia_nombre              VARCHAR(9) NOT NULL, -- 'Monday', 'Tuesday'...
        mes_nombre              VARCHAR(9) NOT NULL -- 'January', 'February'...
);

SELECT * FROM venta LIMIT 10;
SELECT COUNT(*) FROM venta;
SELECT * FROM calendario LIMIT 10;
SELECT COUNT(*) FROM calendario;
SELECT * FROM canal_venta LIMIT 10;
SELECT COUNT(*) FROM canal_venta;
SELECT * FROM cliente LIMIT 10;
SELECT COUNT(*) FROM cliente;
SELECT * FROM producto LIMIT 10;
SELECT COUNT(*) FROM producto;
SELECT * FROM sucursal LIMIT 10;
SELECT COUNT(*) FROM sucursal;

