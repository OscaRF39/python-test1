-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-07-2024 a las 17:05:11
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(10) NOT NULL,
  `cNombres` varchar(80) NOT NULL,
  `cApellidos` varchar(80) NOT NULL,
  `cCorreo` varchar(150) NOT NULL,
  `iEdad` int(3) NOT NULL,
  `cDireccion` varchar(200) NOT NULL,
  `cFoto` text NOT NULL,
  `lActivo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `cNombres`, `cApellidos`, `cCorreo`, `iEdad`, `cDireccion`, `cFoto`, `lActivo`) VALUES
(1, 'Oscar', 'Baeza Castillo', 'oscarbaeza39@gmail.com', 36, 'Calle 18E #244 por 11 y 13, Altabrisa', '', 1),
(2, 'as', 'as', 'as', 23, 'as', 'pinkrush.png', 1),
(3, 'kgb', 's', 'zinarmos@gmail.com', 34, 'Calle 18E #244 por 11 y 13, Altabrisa', 'roserush.png', 0),
(4, 'pedro', 'marmol', 'oscarbaeza39@gmail.com', 37, 'Conocida23', 'Amarige.png', 1),
(11, 'rambo', 'xxx', 'qwerty', 0, '', '', 1),
(12, '1', '2', '3', 0, '', '', 1),
(13, 'rambo', 'xxx', 'qwerty', 0, '', '', 1),
(14, 'Oscar', 'Baeza', 'oscarbaeza39@gmail.com', 23, 'Calle 18E #244 por 11 y 13, Altabrisa', 'clip0001.png', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
