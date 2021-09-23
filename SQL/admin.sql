Create Table If Not Exists Usuario(
	idUsuario VARCHAR(255) NOT NULL,
	nombre VARCHAR(255) NOT NULL,
	apellidoM VARCHAR(255) NOT NULL,
	apellidoP VARCHAR(255) NOT NULL,
	correo VARCHAR(255) NOT NULL,
	contrasena VARCHAR(255) NOT NULL,
	estatusHoras INT NOT NULL,
	ubicacion VARCHAR(255) NOT NULL,
	PRIMARY KEY(idUsuario)
);
CREATE TABLE Admin(id varchar(255)  NOT NULL,
 					  contrasena varchar(255) NOT NULL,
 					  PRIMARY KEY (id),
 				    );