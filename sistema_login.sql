-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: sistema_login
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `almacen_produccion`
--

DROP TABLE IF EXISTS `almacen_produccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `almacen_produccion` (
  `id_almacen` int NOT NULL AUTO_INCREMENT,
  `id_cultivo` int NOT NULL,
  `cantidad_disponible` decimal(10,2) DEFAULT NULL,
  `unidad_medida` varchar(20) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_almacen`),
  KEY `id_cultivo` (`id_cultivo`),
  CONSTRAINT `almacen_produccion_ibfk_1` FOREIGN KEY (`id_cultivo`) REFERENCES `cultivos` (`id_cultivo`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `almacen_produccion`
--

LOCK TABLES `almacen_produccion` WRITE;
/*!40000 ALTER TABLE `almacen_produccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `almacen_produccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aplicaciones_insumos`
--

DROP TABLE IF EXISTS `aplicaciones_insumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aplicaciones_insumos` (
  `id_aplicacion` int NOT NULL AUTO_INCREMENT,
  `id_insumo` int NOT NULL,
  `id_siembra` int NOT NULL,
  `cantidad_aplicada` decimal(10,2) DEFAULT NULL,
  `fecha_aplicacion` date DEFAULT NULL,
  `observaciones` text,
  PRIMARY KEY (`id_aplicacion`),
  KEY `id_insumo` (`id_insumo`),
  KEY `id_siembra` (`id_siembra`),
  CONSTRAINT `aplicaciones_insumos_ibfk_1` FOREIGN KEY (`id_insumo`) REFERENCES `insumos` (`id_insumo`) ON DELETE CASCADE,
  CONSTRAINT `aplicaciones_insumos_ibfk_2` FOREIGN KEY (`id_siembra`) REFERENCES `siembras` (`id_siembra`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aplicaciones_insumos`
--

LOCK TABLES `aplicaciones_insumos` WRITE;
/*!40000 ALTER TABLE `aplicaciones_insumos` DISABLE KEYS */;
/*!40000 ALTER TABLE `aplicaciones_insumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clima`
--

DROP TABLE IF EXISTS `clima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clima` (
  `id_clima` int NOT NULL AUTO_INCREMENT,
  `id_parcela` int NOT NULL,
  `temperatura` decimal(5,2) DEFAULT NULL,
  `humedad` decimal(5,2) DEFAULT NULL,
  `precipitacion` decimal(5,2) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_clima`),
  KEY `id_parcela` (`id_parcela`),
  CONSTRAINT `clima_ibfk_1` FOREIGN KEY (`id_parcela`) REFERENCES `parcelas` (`id_parcela`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clima`
--

LOCK TABLES `clima` WRITE;
/*!40000 ALTER TABLE `clima` DISABLE KEYS */;
/*!40000 ALTER TABLE `clima` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cosechas`
--

DROP TABLE IF EXISTS `cosechas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cosechas` (
  `id_cosecha` int NOT NULL AUTO_INCREMENT,
  `id_siembra` int NOT NULL,
  `cantidad_cosechada` decimal(10,2) DEFAULT NULL,
  `fecha_cosecha` date DEFAULT NULL,
  `calidad` enum('Alta','Media','Baja') DEFAULT 'Alta',
  `destino` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cosecha`),
  KEY `id_siembra` (`id_siembra`),
  CONSTRAINT `cosechas_ibfk_1` FOREIGN KEY (`id_siembra`) REFERENCES `siembras` (`id_siembra`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cosechas`
--

LOCK TABLES `cosechas` WRITE;
/*!40000 ALTER TABLE `cosechas` DISABLE KEYS */;
/*!40000 ALTER TABLE `cosechas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cult_personalizado`
--

DROP TABLE IF EXISTS `cult_personalizado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cult_personalizado` (
  `id_cult` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `nombre_cult` varchar(100) NOT NULL,
  `tipo_cult` varchar(100) DEFAULT NULL,
  `precio_estimado` decimal(10,2) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_cult`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `cult_personalizado_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cult_personalizado`
--

LOCK TABLES `cult_personalizado` WRITE;
/*!40000 ALTER TABLE `cult_personalizado` DISABLE KEYS */;
INSERT INTO `cult_personalizado` VALUES (2,1,'maiz','maiz',54.00,'jsjsj','hsjsj'),(5,2,'frijol','semilla',67.00,'tehuacan','leonel'),(6,3,'maiz','semilla',67.00,'tehuacan','nieves'),(7,2,'Soja','Soja',45.00,'Soja','Soja');
/*!40000 ALTER TABLE `cult_personalizado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cultivos`
--

DROP TABLE IF EXISTS `cultivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cultivos` (
  `id_cultivo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `precio_estimado` decimal(10,2) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_cultivo`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cultivos`
--

LOCK TABLES `cultivos` WRITE;
/*!40000 ALTER TABLE `cultivos` DISABLE KEYS */;
INSERT INTO `cultivos` VALUES (1,'Ma√≠z','Cereal',5.00,'Regi√≥n central y norte','Base de la alimentaci√≥n mexicana, usado en tortillas y tamales.'),(2,'Ca√±a de az√∫car','Perenne',3.50,'Regi√≥n de Tehuac√°n','Cultivo para producci√≥n de az√∫car y derivados.'),(3,'Alfalfa','Forraje',2.80,'Valle de Puebla','Planta forrajera para alimentaci√≥n de ganado.'),(4,'Naranja','Fruta',6.00,'Regi√≥n de Atlixco','Fruta c√≠trica consumida fresca o en jugos.'),(5,'Caf√©','Perenne',25.00,'Sierra Norte','Grano usado para la producci√≥n de caf√©.'),(6,'Frijol','Leguminosa',10.00,'Mixteca poblana','Leguminosa b√°sica en la dieta mexicana.'),(7,'Sorgo','Cereal',4.50,'Regi√≥n de Tehuac√°n','Cereal para alimentaci√≥n animal y humana.'),(8,'Cebolla','Hortaliza',8.00,'Regi√≥n de Tehuac√°n','Hortaliza usada como condimento en cocina.'),(9,'Papa','Tub√©rculo',12.00,'Sierra Norte','Tub√©rculo consumido en diversas formas.'),(10,'Br√≥coli','Hortaliza',15.00,'Regi√≥n de Tehuac√°n','Hortaliza rica en nutrientes.'),(11,'Chile poblano','Hortaliza',18.00,'Regi√≥n de los volcanes','Chile usado en chile en nogada.'),(12,'Jengibre','Rizoma',40.00,'Xicotepec, Jalpan y Pantepec','Planta medicinal y culinaria.'),(13,'Ar√°ndano azul','Fruta',80.00,'Regi√≥n de Atlixco','Fruta rica en antioxidantes.'),(14,'Amaranto','Pseudocereal',20.00,'Tochimilco, Cohuecan y Atlixco','Semillas de alto valor nutritivo.'),(15,'Manzana','Fruta',30.00,'Zacatl√°n y Chignahuapan','Fruta dulce y crujiente.'),(16,'Granada','Fruta',25.00,'Coyomeapan, Coxcatl√°n y Tehuac√°n','Fruta con semillas jugosas.'),(17,'Vainilla','Especia',600.00,'Sierra Nororiental y Sierra Norte','Especia usada en reposter√≠a.'),(18,'Rosa','Flor',15.00,'Chiautzingo y Atlixco','Flor ornamental.'),(19,'Cilantro','Hortaliza',7.00,'Regi√≥n de Tehuac√°n','Hierba arom√°tica condimento.'),(20,'Coliflor','Hortaliza',12.00,'Regi√≥n de Tehuac√°n','Hortaliza rica en fibra.'),(21,'Calabacita','Hortaliza',10.00,'Regi√≥n de Tehuac√°n','Hortaliza de sabor suave.'),(22,'Jitomate','Hortaliza',9.00,'Regi√≥n de Tehuac√°n','Fruto usado en salsas y ensaladas.'),(23,'Pepino','Hortaliza',6.50,'Regi√≥n de Tehuac√°n','Hortaliza fresca para ensaladas.'),(24,'Fresa','Fruta',35.00,'Regi√≥n de Atlixco','Fruta dulce consumida fresca.'),(25,'Arroz','Cereal',14.00,'Regi√≥n de Tehuac√°n','Cereal b√°sico en alimentaci√≥n.'),(26,'Avena','Cereal',9.00,'Regi√≥n de Tehuac√°n','Cereal rico en fibra.'),(27,'Cebada','Cereal',7.50,'Regi√≥n Mixteca','Cereal para cerveza y forraje.'),(28,'Trigo','Cereal',8.50,'Regi√≥n Mixteca','Cereal para harina y pan.'),(29,'Esp√°rrago','Hortaliza',50.00,'Regi√≥n de Tehuac√°n','Hortaliza de alto valor nutricional.'),(30,'Lechuga','Hortaliza',5.00,'Regi√≥n de Tehuac√°n','Hortaliza de hoja en ensaladas.'),(31,'Zanahoria','Hortaliza',7.00,'Atlixco y Tehuac√°n','Ra√≠z rica en betacarotenos.'),(32,'Betabel','Hortaliza',9.00,'Atlixco y Tehuac√°n','Ra√≠z roja rica en antioxidantes.'),(33,'Sand√≠a','Fruta',6.00,'Regi√≥n Mixteca','Fruta dulce con alto contenido de agua.'),(34,'Mel√≥n','Fruta',8.00,'Regi√≥n de Tehuac√°n','Fruta jugosa y dulce.'),(35,'Nopal','Cact√°cea',4.00,'Regi√≥n Mixteca y Tehuac√°n','Planta comestible mexicana.'),(36,'Ch√≠a','Semilla',35.00,'Regi√≥n Mixteca y Atlixco','Semilla rica en omega-3.'),(37,'Guayaba','Fruta',10.00,'Caltepec y Sierra Norte','Fruta tropical rica en vitamina C.'),(38,'Maguey pulquero','Perenne',3.00,'Regi√≥n Mixteca','Planta para producci√≥n de pulque.'),(39,'Aguacate','Fruta',50.00,'Atlixco y Sierra Norte','Fruta rica en grasas saludables.'),(40,'Pimienta gorda','Especia',200.00,'Sierra Norte y Nororiental','Especia arom√°tica en cocina.'),(41,'Ciruela','Fruta',15.00,'Regi√≥n de Atlixco','Fruta jugosa y dulce.'),(42,'Durazno','Fruta',18.00,'Regi√≥n de Atlixco','Fruta dulce y arom√°tica.'),(43,'Chirimoya','Fruta',35.00,'Regi√≥n de la Sierra Norte','Fruta ex√≥tica de pulpa cremosa.'),(44,'Higo','Fruta',28.00,'Regi√≥n de Atlixco','Fruta dulce y nutritiva.'),(45,'Mango','Fruta',22.00,'Regi√≥n de la Sierra Norte','Fruta tropical con alto contenido de vitamina C.'),(46,'Maracuy√°','Fruta',40.00,'Regi√≥n de la Sierra Norte','Fruta ex√≥tica con pulpa √°cida y arom√°tica.'),(47,'Nogal','Fruto seco',120.00,'Regi√≥n Mixteca','√Årbol productor de nueces.'),(48,'Cacao','Perenne',180.00,'Sierra Norte','Fruto utilizado para la producci√≥n de chocolate.'),(49,'Tuna','Fruta',8.00,'Regi√≥n Mixteca','Fruta del nopal de sabor dulce.');
/*!40000 ALTER TABLE `cultivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentos`
--

DROP TABLE IF EXISTS `documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `archivo` longblob,
  `fecha_subida` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `documentos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES (1,2,'Julio',_binary '%PDF-1.3\n3 0 obj\n<</Type /Page\n/Parent 1 0 R\n/Resources 2 0 R\n/Contents 4 0 R>>\nendobj\n4 0 obj\n<</Filter /FlateDecode /Length 141>>\nstream\nxúmÕ±Ç@–ûØòRõeo\Ôˆ,M§†4˜Dœ®¡`à\∆\ﬂ7\‘v2oF\–Ljx€Ñ≤qpëòëNÿ•)_ë\n¨S+±\⁄\Á˚0>2öaºu˝\Z\È˙©\ŒZ\⁄;r5L=âŒ∏}ˆóaaé&TL\∆0QRûQì\ÁnJñRXÙ{\‡\ﬂi4°OﬂèC7˙\nendstream\nendobj\n1 0 obj\n<</Type /Pages\n/Kids [3 0 R ]\n/Count 1\n/MediaBox [0 0 595.28 841.89]\n>>\nendobj\n5 0 obj\n<</Type /Font\n/BaseFont /Helvetica-Bold\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n6 0 obj\n<</Type /Font\n/BaseFont /Helvetica\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n2 0 obj\n<<\n/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/Font <<\n/F1 5 0 R\n/F2 6 0 R\n>>\n/XObject <<\n>>\n>>\nendobj\n7 0 obj\n<<\n/Producer (PyFPDF 1.7.2 http://pyfpdf.googlecode.com/)\n/CreationDate (D:20250214123719)\n>>\nendobj\n8 0 obj\n<<\n/Type /Catalog\n/Pages 1 0 R\n/OpenAction [3 0 R /FitH null]\n/PageLayout /OneColumn\n>>\nendobj\nxref\n0 9\n0000000000 65535 f \n0000000298 00000 n \n0000000582 00000 n \n0000000009 00000 n \n0000000087 00000 n \n0000000385 00000 n \n0000000486 00000 n \n0000000696 00000 n \n0000000805 00000 n \ntrailer\n<<\n/Size 9\n/Root 8 0 R\n/Info 7 0 R\n>>\nstartxref\n908\n%%EOF\n','2025-02-14 12:37:19'),(2,2,'cuidado',_binary '%PDF-1.3\n3 0 obj\n<</Type /Page\n/Parent 1 0 R\n/Resources 2 0 R\n/Contents 4 0 R>>\nendobj\n4 0 obj\n<</Filter /FlateDecode /Length 137>>\nstream\nxúmÕ±\¬0–Ω_q#,é\Ì&1eD¢#\ TM∞!øè\Z±u=›ªSú\Z¶`¯4á\◊$3\“\«4G\Zçº\¬:?∑R\∆\Ê\\\”ÛU∂H˜_ß2]∞VH:XhICU\„˚ñá<-îBx°¸é\…¶ÅW÷óÒ:\Ï!ﬁ±:e\rˇk∑—î|\\ª˝|I7&\nendstream\nendobj\n1 0 obj\n<</Type /Pages\n/Kids [3 0 R ]\n/Count 1\n/MediaBox [0 0 595.28 841.89]\n>>\nendobj\n5 0 obj\n<</Type /Font\n/BaseFont /Helvetica-Bold\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n6 0 obj\n<</Type /Font\n/BaseFont /Helvetica\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n2 0 obj\n<<\n/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/Font <<\n/F1 5 0 R\n/F2 6 0 R\n>>\n/XObject <<\n>>\n>>\nendobj\n7 0 obj\n<<\n/Producer (PyFPDF 1.7.2 http://pyfpdf.googlecode.com/)\n/CreationDate (D:20250214135507)\n>>\nendobj\n8 0 obj\n<<\n/Type /Catalog\n/Pages 1 0 R\n/OpenAction [3 0 R /FitH null]\n/PageLayout /OneColumn\n>>\nendobj\nxref\n0 9\n0000000000 65535 f \n0000000294 00000 n \n0000000578 00000 n \n0000000009 00000 n \n0000000087 00000 n \n0000000381 00000 n \n0000000482 00000 n \n0000000692 00000 n \n0000000801 00000 n \ntrailer\n<<\n/Size 9\n/Root 8 0 R\n/Info 7 0 R\n>>\nstartxref\n904\n%%EOF\n','2025-02-14 13:55:07'),(3,2,'s',_binary '%PDF-1.3\n3 0 obj\n<</Type /Page\n/Parent 1 0 R\n/Resources 2 0 R\n/Contents 4 0 R>>\nendobj\n4 0 obj\n<</Filter /FlateDecode /Length 131>>\nstream\nxúmç1\¬0˚ºbKh\Œwüè§D\"%Ú!\Z \Â˚(ç\ÌjfG±\Ôò\Ã1w€å0	$3ÚªºLöú¢¬á∏P˘å’°<\Ó\œwY#ﬂæL’¥\—z!\‡÷ìZµ^\rØn¯∏arÜ´ëq¶r∫GH¨AY\Ì˜\‡_0πRLmuj2Z\nendstream\nendobj\n1 0 obj\n<</Type /Pages\n/Kids [3 0 R ]\n/Count 1\n/MediaBox [0 0 595.28 841.89]\n>>\nendobj\n5 0 obj\n<</Type /Font\n/BaseFont /Helvetica-Bold\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n6 0 obj\n<</Type /Font\n/BaseFont /Helvetica\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n2 0 obj\n<<\n/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/Font <<\n/F1 5 0 R\n/F2 6 0 R\n>>\n/XObject <<\n>>\n>>\nendobj\n7 0 obj\n<<\n/Producer (PyFPDF 1.7.2 http://pyfpdf.googlecode.com/)\n/CreationDate (D:20250214135814)\n>>\nendobj\n8 0 obj\n<<\n/Type /Catalog\n/Pages 1 0 R\n/OpenAction [3 0 R /FitH null]\n/PageLayout /OneColumn\n>>\nendobj\nxref\n0 9\n0000000000 65535 f \n0000000288 00000 n \n0000000572 00000 n \n0000000009 00000 n \n0000000087 00000 n \n0000000375 00000 n \n0000000476 00000 n \n0000000686 00000 n \n0000000795 00000 n \ntrailer\n<<\n/Size 9\n/Root 8 0 R\n/Info 7 0 R\n>>\nstartxref\n898\n%%EOF\n','2025-02-14 13:58:14'),(4,3,'Nieves',_binary '%PDF-1.3\n3 0 obj\n<</Type /Page\n/Parent 1 0 R\n/Resources 2 0 R\n/Contents 4 0 R>>\nendobj\n4 0 obj\n<</Filter /FlateDecode /Length 136>>\nstream\nxúmÕ±\¬0–Ω_q#,Æ\Ì\∆1eD¢\   ¯}‘à%®\Î\Èﬁùb\”0ô\„”¨\⁄A ëòëNXß1\“\Ëﬁá±ïéò\ÌÚ˝ˆx\Â9\“ı\◊)L+\÷	I∑é‘ä\⁄^Ú;?+§ÆPX09\√\’»∏®!\Œ˚%$¥¨≠≤\⁄ˇ¿\‘kt•\'^øÒè6H\nendstream\nendobj\n1 0 obj\n<</Type /Pages\n/Kids [3 0 R ]\n/Count 1\n/MediaBox [0 0 595.28 841.89]\n>>\nendobj\n5 0 obj\n<</Type /Font\n/BaseFont /Helvetica-Bold\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n6 0 obj\n<</Type /Font\n/BaseFont /Helvetica\n/Subtype /Type1\n/Encoding /WinAnsiEncoding\n>>\nendobj\n2 0 obj\n<<\n/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/Font <<\n/F1 5 0 R\n/F2 6 0 R\n>>\n/XObject <<\n>>\n>>\nendobj\n7 0 obj\n<<\n/Producer (PyFPDF 1.7.2 http://pyfpdf.googlecode.com/)\n/CreationDate (D:20250214152935)\n>>\nendobj\n8 0 obj\n<<\n/Type /Catalog\n/Pages 1 0 R\n/OpenAction [3 0 R /FitH null]\n/PageLayout /OneColumn\n>>\nendobj\nxref\n0 9\n0000000000 65535 f \n0000000293 00000 n \n0000000577 00000 n \n0000000009 00000 n \n0000000087 00000 n \n0000000380 00000 n \n0000000481 00000 n \n0000000691 00000 n \n0000000800 00000 n \ntrailer\n<<\n/Size 9\n/Root 8 0 R\n/Info 7 0 R\n>>\nstartxref\n903\n%%EOF\n','2025-02-14 15:29:35');
/*!40000 ALTER TABLE `documentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `finanzas`
--

DROP TABLE IF EXISTS `finanzas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `finanzas` (
  `id_transaccion` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `tipo` enum('Ingreso','Gasto') DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `detalle` text,
  PRIMARY KEY (`id_transaccion`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `finanzas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finanzas`
--

LOCK TABLES `finanzas` WRITE;
/*!40000 ALTER TABLE `finanzas` DISABLE KEYS */;
/*!40000 ALTER TABLE `finanzas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insumos`
--

DROP TABLE IF EXISTS `insumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insumos` (
  `id_insumo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo` enum('Fertilizante','Pesticida','Herbicida','Semilla','Otro') DEFAULT NULL,
  `cantidad_disponible` decimal(10,2) DEFAULT NULL,
  `unidad_medida` varchar(20) DEFAULT NULL,
  `fecha_caducidad` date DEFAULT NULL,
  PRIMARY KEY (`id_insumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insumos`
--

LOCK TABLES `insumos` WRITE;
/*!40000 ALTER TABLE `insumos` DISABLE KEYS */;
/*!40000 ALTER TABLE `insumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maquinaria`
--

DROP TABLE IF EXISTS `maquinaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maquinaria` (
  `id_maquinaria` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `estado` enum('Disponible','En reparaci√≥n','En uso') DEFAULT 'Disponible',
  `ubicacion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_maquinaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maquinaria`
--

LOCK TABLES `maquinaria` WRITE;
/*!40000 ALTER TABLE `maquinaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `maquinaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parcelas`
--

DROP TABLE IF EXISTS `parcelas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parcelas` (
  `id_parcela` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `tamano` decimal(10,2) DEFAULT NULL,
  `tipo_suelo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_parcela`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `parcelas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parcelas`
--

LOCK TABLES `parcelas` WRITE;
/*!40000 ALTER TABLE `parcelas` DISABLE KEYS */;
/*!40000 ALTER TABLE `parcelas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `siembras`
--

DROP TABLE IF EXISTS `siembras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `siembras` (
  `id_siembra` int NOT NULL AUTO_INCREMENT,
  `id_cultivo` int NOT NULL,
  `id_parcela` int NOT NULL,
  `fecha_siembra` date DEFAULT NULL,
  `densidad_siembra` decimal(10,2) DEFAULT NULL,
  `estado` enum('Germinando','En crecimiento','Listo para cosecha') DEFAULT 'Germinando',
  PRIMARY KEY (`id_siembra`),
  KEY `id_cultivo` (`id_cultivo`),
  KEY `id_parcela` (`id_parcela`),
  CONSTRAINT `siembras_ibfk_1` FOREIGN KEY (`id_cultivo`) REFERENCES `cultivos` (`id_cultivo`) ON DELETE CASCADE,
  CONSTRAINT `siembras_ibfk_2` FOREIGN KEY (`id_parcela`) REFERENCES `parcelas` (`id_parcela`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `siembras`
--

LOCK TABLES `siembras` WRITE;
/*!40000 ALTER TABLE `siembras` DISABLE KEYS */;
/*!40000 ALTER TABLE `siembras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(100) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `clave` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Ni√±o','7173783788','46e8b7ec9cc3a9b879021dd38d9f9851066940c7a63ed1d5543641dc3fb84a28'),(2,'Alvaro','73818727','35556426d11e18c513223bdc152afede83a154e6e8783df212ba41cc17ce56d3'),(3,'World34','73827728','0fcd687636a4493cbf584fa7415afd02ddb03d065cc594b07b45cd213ebe7fac'),(4,'user1','35454','3875034e17855bac03a3cc9e107b1d28a9b44313d381c3335588525b4e70b55b'),(5,'user2','7388837','9e56e2ff9b0cda81821524df739598640c16d4a4ea1d48be97ca331724773531'),(6,'user3','73827738','fb242d167f97683120ee4d6d2c633ea1602b60448309a8326d70a98144cdb108'),(7,'User4','72838728','c6a816ada8ddd86b56e26b967c3e3fdd7680c6f1d0a9e2834e9f1b024b017767');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-14 16:36:41
