CREATE TABLE `Usuario` (
  `idUsuario` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellidoP` varchar(255) NOT NULL,
  `apellidoM` varchar(255) NOT NULL,
  `calle` varchar(255) NOT NULL,
  `numero` varchar(255) NOT NULL,
  `colonia` varchar(255) NOT NULL,
  `municipio` varchar(255) NOT NULL,
  `estado` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `CPP` int(11) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `estatusHoras` int(11) NOT NULL,
  `foto` varchar(255) NOT NULL,
  `documentos_approval` tinyint(1) NOT NULL,
  `email_approval` tinyint(1) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `correo` (`correo`)
);

CREATE TABLE `Documentos` (
  `idUser` varchar(255) NOT NULL,
  `ine` varchar(255) NOT NULL,
  `ine_approval` tinyint(1) NOT NULL,
  `comprobante` varchar(255) NOT NULL,
  `comprobante_approval` tinyint(1) NOT NULL,
  `cartaAntecedentes` varchar(255) NOT NULL,
  `cartaAntecedentes_approval` tinyint(1) NOT NULL,
  PRIMARY KEY (`idUser`),
  FOREIGN KEY (`idUser`) REFERENCES `Usuario` (`idUsuario`)
);
CREATE TABLE `Servicios` (
  `idServicio` int(11) NOT NULL AUTO_INCREMENT,
  `idUsuario` varchar(255) NOT NULL,
  `ubicacion` varchar(255) NOT NULL,
  `categoria` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  `certificado` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `V0` int(11) NOT NULL,
  `V1` int(11) NOT NULL,
  `V2` int(11) NOT NULL,
  `V3` int(11) NOT NULL,
  `V4` int(11) NOT NULL,
  `V5` int(11) NOT NULL,
  PRIMARY KEY (`idServicio`),
  UNIQUE KEY `u_service` (`nombre`,`idUsuario`),
  KEY `idUsuario` (`idUsuario`),
  FOREIGN KEY (`idUsuario`) REFERENCES `Usuario` (`idUsuario`)
);
CREATE TABLE `Recibe` (
  `idCita` int(11) NOT NULL AUTO_INCREMENT,
  `idReceptor` varchar(255) NOT NULL,
  `idServicio` int(11) NOT NULL,
  `idEmisor` varchar(255) NOT NULL,
  `estado` varchar(255) NOT NULL,
  PRIMARY KEY (`idCita`),
  KEY `idServicio` (`idServicio`),
  KEY `idReceptor` (`idReceptor`),
  KEY `idEmisor` (`idEmisor`),
  FOREIGN KEY (`idServicio`) REFERENCES `Servicios` (`idServicio`),
  FOREIGN KEY (`idReceptor`) REFERENCES `Usuario` (`idUsuario`),
  FOREIGN KEY (`idEmisor`) REFERENCES `Usuario` (`idUsuario`)
);

CREATE TABLE `Notificacion` (
  `idNotificacion` int(11) NOT NULL AUTO_INCREMENT,
  `idEmisor` varchar(255) NOT NULL,
  `idReceptor` varchar(255) NOT NULL,
  `idServicio` int(11) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`idNotificacion`),
  KEY `idEmisor` (`idEmisor`,`idServicio`),
  KEY `idReceptor` (`idReceptor`),
  FOREIGN KEY (`idEmisor`, `idServicio`) REFERENCES `Servicios` (`idUsuario`, `idServicio`),
  FOREIGN KEY (`idReceptor`) REFERENCES `Usuario` (`idUsuario`)
);

CREATE TABLE If Not Exists Admin(
    id varchar(255)  NOT NULL,
    contrasena varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
