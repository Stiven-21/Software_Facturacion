-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para software_facturacion
CREATE DATABASE IF NOT EXISTS `software_facturacion` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `software_facturacion`;

-- Volcando estructura para tabla software_facturacion.estado
CREATE TABLE IF NOT EXISTS `estado` (
  `id_estado` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla software_facturacion.estado: ~2 rows (aproximadamente)
DELETE FROM `estado`;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` (`id_estado`, `estado`) VALUES
	(1, 'pagado'),
	(2, 'no pagado');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;

-- Volcando estructura para tabla software_facturacion.facturas
CREATE TABLE IF NOT EXISTS `facturas` (
  `id_factura` int(11) NOT NULL AUTO_INCREMENT,
  `referencia` int(11) NOT NULL DEFAULT '0',
  `id_user` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `descripcion` varchar(255) DEFAULT NULL,
  `cantidad` varchar(255) DEFAULT NULL,
  `precio` float NOT NULL DEFAULT '0',
  `descuento` float NOT NULL DEFAULT '0',
  `impuesto` float NOT NULL DEFAULT '0',
  `id_estado` int(11) NOT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `FK_factura_cliente` (`id_user`),
  KEY `FK_factura_estado` (`id_estado`),
  CONSTRAINT `FK_factura_cliente` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`),
  CONSTRAINT `FK_factura_estado` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla software_facturacion.facturas: ~0 rows (aproximadamente)
DELETE FROM `facturas`;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` (`id_factura`, `referencia`, `id_user`, `fecha`, `descripcion`, `cantidad`, `precio`, `descuento`, `impuesto`, `id_estado`) VALUES
	(1, 62743380, 4, '2022-11-25 15:18:31', 'prueba', '22', 70000, 0, 19, 2),
	(2, 98791790, 4, '2022-11-25 15:43:09', 'prueba', '433', 1000, 0, 19, 2),
	(3, 98791790, 4, '2022-11-25 15:43:20', 'prueba2', '433', 70000, 2, 19, 2),
	(4, 98791790, 4, '2022-11-25 15:43:29', 'prueba', '12', 1000, 12, 19, 2);
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;

-- Volcando estructura para tabla software_facturacion.login
CREATE TABLE IF NOT EXISTS `login` (
  `id_login` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) NOT NULL DEFAULT '0',
  `user` varchar(50) NOT NULL DEFAULT '0',
  `password` varchar(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_login`),
  KEY `FK_user_login` (`id_user`),
  CONSTRAINT `FK_user_login` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla software_facturacion.login: ~2 rows (aproximadamente)
DELETE FROM `login`;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`id_login`, `id_user`, `user`, `password`) VALUES
	(1, 1, 'pelon', 'pelon'),
	(2, 2, 'empleado', 'pelon');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;

-- Volcando estructura para tabla software_facturacion.roles
CREATE TABLE IF NOT EXISTS `roles` (
  `id_rol` int(11) NOT NULL AUTO_INCREMENT,
  `rol` varchar(50) DEFAULT '0',
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla software_facturacion.roles: ~2 rows (aproximadamente)
DELETE FROM `roles`;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` (`id_rol`, `rol`) VALUES
	(1, 'administrador'),
	(2, 'empleado'),
	(3, 'cliente');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;

-- Volcando estructura para tabla software_facturacion.users
CREATE TABLE IF NOT EXISTS `users` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `identificacion` int(11) DEFAULT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `id_rol` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  KEY `FK_rol_user` (`id_rol`),
  CONSTRAINT `FK_rol_user` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla software_facturacion.users: ~4 rows (aproximadamente)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id_user`, `identificacion`, `nombre`, `apellido`, `telefono`, `email`, `ciudad`, `id_rol`) VALUES
	(1, 123456789, 'pelon', 'pelon', '12345678', 'pelon@gmail.com', 'Mocoa', 1),
	(2, 123456788, 'actualizacion', 'prueba', '123456', 'prueba@gmail.com', 'Bogota', 2),
	(3, 12345678, 'prueba2', 'prueba2', '98765', 'prueba2@gmail.com', 'Medellin', 3),
	(4, 1234567889, 'prueba2', 'prueba', '31313131', 'prueba2@gmail.com', 'Mocoa', 3);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
