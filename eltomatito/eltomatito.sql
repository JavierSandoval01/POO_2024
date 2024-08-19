-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-08-2024 a las 04:08:05
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `eltomatito`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `id_admin` int(11) NOT NULL,
  `id_restaurante` int(11) DEFAULT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `usuario` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id_admin`, `id_restaurante`, `nombres`, `apellidos`, `usuario`, `password`, `telefono`) VALUES
(4, 1, 'alma', 'alma', 'alma', 'cf43e029efe6476e1f7f84691f89c876818610c2eaeaeb881103790a48745b82', '61726352535'),
(5, 1, 'idali', 'gonzalez', 'idali123', '1871a8acc472df33ad6ba3904c33ec2e47d102447e0b97944895c9f4c29b002e', '6187263435'),
(6, 1, 'javier', 'sandoval', 'javier123', '26ce13833bf9b1a34904d0b8ff10bc035178931c4ac6d8d02cc2274c6d20a09c', '6182543456'),
(7, 1, 'aaaaa', 'aaaaa', 'aaaaa', 'ed968e840d10d2d313a870bc131a4e2c311d7ad09bdf32b3418147221f51a6e2', '324221'),
(8, 1, 'wwwwwwwwww', 'wwwwwwwwww', 'wwwwwwwwww', '4165544e6b3d9440711125e462be340d8b71a909d237f9eb0d0a23f0ba2e6586', 'wwwwwwwwww'),
(9, 1, 'ana', 'ana', 'ana', '24d4b96f58da6d4a8512313bbd02a28ebf0ca95dec6e4c86ef78ce7f01e788ac', '6182435434'),
(10, 1, 'javier', 'vazquez', 'javier123', '26ce13833bf9b1a34904d0b8ff10bc035178931c4ac6d8d02cc2274c6d20a09c', '6182139688'),
(11, 1, 'aa', 'ss', 'ss', 'e38ff5c759b3ede59367eaf5bac7179b06f608da5730315835ba263bc27c8600', '124');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `nombre`) VALUES
(1, 'luis'),
(2, 'alonso'),
(3, 'ana'),
(4, '4'),
(5, '4'),
(6, 'lola'),
(7, 'ana'),
(8, 'lina'),
(9, 'nose'),
(10, 'hh'),
(11, 'f'),
(12, 'd'),
(13, 'goku'),
(14, 'bulma'),
(15, 'ff'),
(16, 'calamardo'),
(17, 'dd'),
(18, 'lalo'),
(19, 'aladin'),
(20, 'fito'),
(21, 'sam'),
(22, 'arbol'),
(23, 'lluvia'),
(24, 'bebedor'),
(25, 'alondra'),
(26, 'dd'),
(27, 'f'),
(28, '2'),
(29, 'lupita'),
(30, 'yo mero'),
(31, 'el chavo'),
(32, 'leti'),
(33, '4'),
(34, 'ff'),
(35, 'dd'),
(36, 'shakira'),
(37, 'shakira'),
(38, 'bravito'),
(39, '4'),
(40, 'batman'),
(41, 'ss'),
(42, 'ss'),
(43, '33'),
(44, 'gg'),
(45, ''),
(46, ''),
(47, 'rosa meraz'),
(48, 'luis'),
(49, 'ana'),
(50, 'casac'),
(51, 'fff');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_pedido`
--

CREATE TABLE `detalles_pedido` (
  `id` int(11) NOT NULL,
  `id_pedido` int(11) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `id_platillo` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalles_pedido`
--

INSERT INTO `detalles_pedido` (`id`, `id_pedido`, `id_categoria`, `id_platillo`, `cantidad`) VALUES
(1, 11, 1, 1, 2),
(2, 11, 1, 1, 10),
(3, 12, 1, 1, 7),
(4, 13, 1, 1, 4),
(5, 13, 2, 6, 4),
(6, 13, 1, 5, 100),
(7, 13, 2, 8, 33),
(8, 14, 1, 1, 1),
(9, 14, 2, 6, 6),
(10, 14, 3, 10, 2),
(11, 14, 4, 13, 3),
(12, 15, 4, 13, 3),
(14, 15, 6, 26, 2),
(15, 16, 6, 26, 2),
(18, 18, 5, 25, 2),
(19, 18, 6, 26, 3),
(20, 19, 1, 4, 4),
(21, 19, 3, 10, 2),
(22, 19, 4, 13, 2),
(23, 19, 5, 24, 1),
(24, 19, 6, 26, 1),
(25, 20, 1, 1, 2),
(26, 20, 6, 26, 1),
(27, 21, 1, 2, 2),
(28, 21, 1, 2, 2),
(29, 21, 1, 3, 3),
(30, 21, 5, 18, 2),
(31, 22, 1, 1, 2),
(32, 22, 5, 18, 2),
(33, 23, 1, 1, 2),
(34, 23, 6, 26, 2),
(35, 24, 1, 1, 2),
(36, 24, 5, 18, 4),
(37, 25, 1, 1, 2),
(38, 26, 1, 2, 2),
(39, 34, 1, 3, 3),
(40, 36, 1, 2, 5),
(41, 36, 5, 16, 2),
(42, 37, 1, 2, 5),
(43, 37, 2, 7, 2),
(44, 37, 4, 12, 1),
(45, 37, 5, 21, 1),
(46, 37, 5, 20, 2),
(47, 37, 5, 17, 1),
(48, 39, 3, 10, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `menu`
--

CREATE TABLE `menu` (
  `id_categoria` int(11) NOT NULL,
  `id_restaurante` int(11) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `menu`
--

INSERT INTO `menu` (`id_categoria`, `id_restaurante`, `nombre`) VALUES
(1, 1, 'Tacos'),
(2, 1, 'Burros'),
(3, 1, 'Chonchos'),
(4, 1, 'Campechanos'),
(5, 1, 'Bebidas'),
(6, 1, 'postres');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mesa`
--

CREATE TABLE `mesa` (
  `id_mesa` int(11) NOT NULL,
  `NumeroMesa` int(11) DEFAULT NULL,
  `id_restaurante` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mesa`
--

INSERT INTO `mesa` (`id_mesa`, `NumeroMesa`, `id_restaurante`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1),
(9, 9, 1),
(10, 10, 1),
(11, 11, 1),
(12, 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mesero`
--

CREATE TABLE `mesero` (
  `id_mesero` int(11) NOT NULL,
  `id_restaurante` int(11) DEFAULT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `usuario` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mesero`
--

INSERT INTO `mesero` (`id_mesero`, `id_restaurante`, `nombres`, `apellidos`, `usuario`, `password`, `telefono`) VALUES
(3, 1, 'miguel', 'miguel', 'miguel', '5ef68465886fa04d3e0bbe86b59d964dd98e5775e95717df978d8bedee6ff16c', '6182382733'),
(8, 1, 'idali', 'gonzalez', 'idali123', '1871a8acc472df33ad6ba3904c33ec2e47d102447e0b97944895c9f4c29b002e', '61823253666'),
(9, 1, 'pitufo', 'dd', 'dd', '9b7ecc6eeb83abf9ade10fe38865df4499be3568dcc507ae2ec3b44989cb0093', '33');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id_pedido` int(11) NOT NULL,
  `id_mesa` int(11) DEFAULT NULL,
  `numeroMesa` int(11) DEFAULT NULL,
  `numeroPersonas` int(11) DEFAULT NULL,
  `numOrden` int(11) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_mesero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`id_pedido`, `id_mesa`, `numeroMesa`, `numeroPersonas`, `numOrden`, `id_cliente`, `id_mesero`) VALUES
(3, 3, 3, 2, 1, 12, 3),
(4, 4, 4, 7, 1, 13, 3),
(5, 4, 4, 3, 1, 14, 3),
(6, 3, 3, 3, 1, 15, 3),
(7, 4, 4, 5, 1, 16, 3),
(8, 3, 3, 4, 1, 17, 3),
(9, 3, 3, 4, 1, 18, 3),
(10, 3, 3, 4, 1, 19, 3),
(11, 3, 3, 2, 1, 20, 3),
(12, 3, 3, 4, 1, 21, 3),
(13, 2, 2, 3, 1, 22, 3),
(14, 5, 5, 4, 1, 23, 3),
(15, 4, 4, 3, 1, 24, 3),
(16, 3, 3, 4, 1, 25, 3),
(17, 2, 2, 3, 2, 26, 3),
(18, 2, 2, 3, 1, 27, 3),
(19, 4, 4, 3, 1, 28, 3),
(20, 2, 2, 3, 1, 29, 3),
(21, 2, 2, 3, 1, 30, 3),
(22, 3, 3, 4, 1, 31, 3),
(23, 2, 2, 3, 1, 32, 3),
(24, 2, 2, 3, 1, 33, 3),
(25, 3, 3, 4, 2, 34, 3),
(26, 3, 3, 2, 1, 35, 3),
(27, 2, 2, 2, 1, 37, 3),
(28, 3, 3, 4, 1, 38, 3),
(29, 5, 5, 3, 1, 39, 3),
(30, 1, 1, 4, 1, 40, 8),
(31, 5, 5, 3, 1, 41, 8),
(32, 3, 3, 3, 1, 42, 3),
(33, 4, 4, 2, 1, 43, 3),
(34, 2, 2, 3, 1, 44, 3),
(35, 2, 2, 4, 1, 47, 8),
(36, 2, 2, 2, 1, 48, 8),
(37, 2, 2, 4, 1, 49, 8),
(38, 3, 3, 3, 1, 50, 8),
(39, 5, 5, 3, 2, 51, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `platillo`
--

CREATE TABLE `platillo` (
  `id_platillo` int(11) NOT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `precio` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `platillo`
--

INSERT INTO `platillo` (`id_platillo`, `tipo`, `id_categoria`, `precio`) VALUES
(1, 'pastor', 1, 19),
(2, 'asada', 1, 19),
(3, 'suadero', 1, 19),
(4, 'longaniza', 1, 19),
(5, 'chicharron', 1, 19),
(6, 'asada', 2, 49),
(7, 'pastor', 2, 49),
(8, 'chicharron', 2, 49),
(9, 'asada', 3, 160),
(10, 'pastor', 3, 160),
(11, 'asada y pastor', 4, 25),
(12, 'longaniza y suadero', 4, 25),
(13, 'asada y salchicha', 4, 25),
(14, 'Horchata (chica)', 5, 25),
(15, 'Jamaica (chica)', 5, 25),
(16, 'Limón (chica)', 5, 25),
(17, 'Pepino y Limón (chica)', 5, 25),
(18, 'Piña (chica)', 5, 25),
(19, 'Horchata (grande)', 5, 40),
(20, 'Jamaica (grande)', 5, 40),
(21, 'Limón (grande)', 5, 40),
(22, 'Pepino y Limón (grande)', 5, 40),
(23, 'Piña (grande)', 5, 40),
(24, 'Café', 5, 20),
(25, 'Refresco', 5, 25),
(26, 'Fresas con crema', 6, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurante`
--

CREATE TABLE `restaurante` (
  `id_restaurante` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `calle` varchar(255) DEFAULT NULL,
  `numero` varchar(50) DEFAULT NULL,
  `colonia` varchar(255) DEFAULT NULL,
  `codigo_postal` varchar(10) NOT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `municipio` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `rfc` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `restaurante`
--

INSERT INTO `restaurante` (`id_restaurante`, `nombre`, `calle`, `numero`, `colonia`, `codigo_postal`, `estado`, `municipio`, `telefono`, `rfc`) VALUES
(1, 'EL TOMATITO', '5 de febrero', '710', 'Zona Centro', '34000', 'Durango', 'Durango', '6182737551', '0EVE900630684');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ticket`
--

CREATE TABLE `ticket` (
  `id_ticket` int(11) NOT NULL,
  `id_pedido` int(11) DEFAULT NULL,
  `fecha` varchar(30) DEFAULT NULL,
  `ImportePedido` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ticket`
--

INSERT INTO `ticket` (`id_ticket`, `id_pedido`, `fecha`, `ImportePedido`) VALUES
(1, 23, '2024-08-11 21:30:48.162417', 98),
(2, 24, '2024-08-11 21:38:15.044518', 138),
(3, 25, '2024-08-11 21:38:15.044518', 38),
(4, 26, '2024-08-11 21:41:32.001252', 38),
(5, 27, '2024-08-17 10:34:32.241722', 0),
(6, 31, '2024-08-17 14:33:19.056397', 0),
(7, 33, '2024-08-17 14:35:46.614352', 0),
(8, 34, '2024-08-17 16:02:55.838079', 57),
(9, 35, '2024-08-17 17:32:56.371061', 0),
(10, 36, '2024-08-17 20:10:10.293070', 145),
(11, 37, '2024-08-18 18:02:43.782873', 363),
(12, 38, '2024-08-18 18:20:32.483340', 0),
(13, 39, '2024-08-18 20:06:37.541790', 320);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id_admin`),
  ADD KEY `id_restaurante` (`id_restaurante`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `detalles_pedido`
--
ALTER TABLE `detalles_pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pedido` (`id_pedido`),
  ADD KEY `id_categoria` (`id_categoria`),
  ADD KEY `id_platillo` (`id_platillo`);

--
-- Indices de la tabla `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id_categoria`),
  ADD KEY `id_restaurante` (`id_restaurante`);

--
-- Indices de la tabla `mesa`
--
ALTER TABLE `mesa`
  ADD PRIMARY KEY (`id_mesa`),
  ADD KEY `id_restaurante` (`id_restaurante`);

--
-- Indices de la tabla `mesero`
--
ALTER TABLE `mesero`
  ADD PRIMARY KEY (`id_mesero`),
  ADD KEY `id_restaurante` (`id_restaurante`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id_pedido`),
  ADD KEY `id_mesa` (`id_mesa`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_mesero` (`id_mesero`);

--
-- Indices de la tabla `platillo`
--
ALTER TABLE `platillo`
  ADD PRIMARY KEY (`id_platillo`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `restaurante`
--
ALTER TABLE `restaurante`
  ADD PRIMARY KEY (`id_restaurante`);

--
-- Indices de la tabla `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`id_ticket`),
  ADD KEY `id_pedido` (`id_pedido`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT de la tabla `detalles_pedido`
--
ALTER TABLE `detalles_pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `menu`
--
ALTER TABLE `menu`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `mesa`
--
ALTER TABLE `mesa`
  MODIFY `id_mesa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `mesero`
--
ALTER TABLE `mesero`
  MODIFY `id_mesero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT de la tabla `platillo`
--
ALTER TABLE `platillo`
  MODIFY `id_platillo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `restaurante`
--
ALTER TABLE `restaurante`
  MODIFY `id_restaurante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `ticket`
--
ALTER TABLE `ticket`
  MODIFY `id_ticket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `administrador_ibfk_1` FOREIGN KEY (`id_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `detalles_pedido`
--
ALTER TABLE `detalles_pedido`
  ADD CONSTRAINT `detalles_pedido_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`),
  ADD CONSTRAINT `detalles_pedido_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `menu` (`id_categoria`),
  ADD CONSTRAINT `detalles_pedido_ibfk_3` FOREIGN KEY (`id_platillo`) REFERENCES `platillo` (`id_platillo`);

--
-- Filtros para la tabla `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`id_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `mesa`
--
ALTER TABLE `mesa`
  ADD CONSTRAINT `mesa_ibfk_1` FOREIGN KEY (`id_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `mesero`
--
ALTER TABLE `mesero`
  ADD CONSTRAINT `mesero_ibfk_1` FOREIGN KEY (`id_restaurante`) REFERENCES `restaurante` (`id_restaurante`);

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`id_mesa`) REFERENCES `mesa` (`id_mesa`),
  ADD CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `pedido_ibfk_3` FOREIGN KEY (`id_mesero`) REFERENCES `mesero` (`id_mesero`);

--
-- Filtros para la tabla `platillo`
--
ALTER TABLE `platillo`
  ADD CONSTRAINT `platillo_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `menu` (`id_categoria`);

--
-- Filtros para la tabla `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
