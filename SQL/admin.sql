Create Table If Not Exists Usuario(
	idUsuario VARCHAR(255) NOT NULL,
	nombre VARCHAR(255) NOT NULL,
    apellidoP VARCHAR(255) NOT NULL,
	apellidoM VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
	correo VARCHAR(255) NOT NULL,
	contrasena VARCHAR(255) NOT NULL,
	estatusHoras INT NOT NULL,
    documentos_approval tinyint(1) NOT NULL,
	PRIMARY KEY(idUsuario)
);
Create Table If Not Exists Documentos(
	idUser VARCHAR(255) NOT NULL,
	ine VARCHAR(255) NOT NULL,
	ine_approval tinyint(1) NOT NULL,
    comprobante VARCHAR(255) NOT NULL,
	comprobante_approval tinyint(1) NOT NULL,
    cartaAntecedentes VARCHAR(255) NOT NULL,
	cartaAntecedentes_approval tinyint(1) NOT NULL,
    PRIMARY KEY(idUser),
	FOREIGN KEY(idUser) REFERENCES Usuario(idUsuario)
);
Create Table If Not Exists Servicios(
    idServicio VARCHAR(255) NOT NULL,
    idUsuario  VARCHAR(255) NOT NULL,
    ubicacion  VARCHAR(255) NOT NULL,
    categoria  VARCHAR(255) NOT NULL,
    nombre     VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    tiempoActivo TIME NOT NULL,
    V0 INT NOT NULL,
    V1 INT NOT NULL,
    V2 INT NOT NULL,
    V3 INT NOT NULL,
    V4 INT NOT NULL,
    V5 INT NOT NULL,
    PRIMARY KEY(idServicio),
    FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario)
);
Create Table If Not Exists Recibe(
    idCita VARCHAR(255) NOT NULL,
    idReceptor VARCHAR(255) NOT NULL,
    idServicio VARCHAR(255) NOT NULL,
    idEmisor VARCHAR(255) NOT NULL,
    estado VARCHAR(255) NOT NULL,
    comentario VARCHAR(255) NOT NULL,
    PRIMARY KEY(idCita),
    FOREIGN KEY(idServicio) REFERENCES Servicios(idServicio),
    FOREIGN KEY(idReceptor, idEmisor) REFERENCES Usuario(idUsuario)
);

CREATE TABLE If Not Exists Admin(
    id varchar(255)  NOT NULL,
    contrasena varchar(255) NOT NULL,
    PRIMARY KEY (id),
);