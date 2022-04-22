-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 192.168.0.144    Database: management
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `clientlist`
--

DROP TABLE IF EXISTS `clientlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientlist` (
  `cid` varchar(5) NOT NULL,
  `tel` varchar(10) DEFAULT NULL,
  `addr` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientlist`
--

LOCK TABLES `clientlist` WRITE;
/*!40000 ALTER TABLE `clientlist` DISABLE KEYS */;
INSERT INTO `clientlist` VALUES ('C1','1111','Tuen Mun'),('C2','2222','Diamond Hill'),('C3','3333','Tai Wai'),('admin',NULL,NULL);
/*!40000 ALTER TABLE `clientlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemlist`
--

DROP TABLE IF EXISTS `itemlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itemlist` (
  `iid` varchar(5) DEFAULT NULL,
  `iname` varchar(20) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `kw1` varchar(20) DEFAULT NULL,
  `kw2` varchar(20) DEFAULT NULL,
  `kw3` varchar(20) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `sid` varchar(5) DEFAULT NULL,
  `compid` varchar(45) NOT NULL,
  PRIMARY KEY (`compid`),
  KEY `sid` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemlist`
--

LOCK TABLES `itemlist` WRITE;
/*!40000 ALTER TABLE `itemlist` DISABLE KEYS */;
INSERT INTO `itemlist` VALUES ('I1','Apple',10,'Red','Sweet',NULL,200,'S1','I1S1'),('I2','Orange',8,'Yellow','Fresh','Australia',100,'S1','I2S1'),('I3','Apple',8000,'Red','256G',NULL,50,'S2','I3S2'),('I6','AI',400,'Paperback','Deep learning','Python',95,'S3','I3S3'),('I4','Samsung',7000,'Black','128G','Folding',20,'S2','I4S2'),('I5','DB',500,'Paperback','Relational','SQL',90,'S3','I5S3');
/*!40000 ALTER TABLE `itemlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderlist`
--

DROP TABLE IF EXISTS `orderlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderlist` (
  `oid` varchar(5) NOT NULL,
  `cid` varchar(5) DEFAULT NULL,
  `odate` date DEFAULT NULL,
  `compid1` varchar(45) DEFAULT NULL,
  `oqty1` int DEFAULT NULL,
  `compid2` varchar(45) DEFAULT NULL,
  `oqty2` int DEFAULT NULL,
  `compid3` varchar(45) DEFAULT NULL,
  `oqty3` int DEFAULT NULL,
  PRIMARY KEY (`oid`),
  KEY `compid1` (`compid1`),
  KEY `compid2` (`compid2`),
  KEY `compid3` (`compid3`),
  CONSTRAINT `orderlist_ibfk_1` FOREIGN KEY (`compid1`) REFERENCES `itemlist` (`compid`),
  CONSTRAINT `orderlist_ibfk_2` FOREIGN KEY (`compid2`) REFERENCES `itemlist` (`compid`),
  CONSTRAINT `orderlist_ibfk_3` FOREIGN KEY (`compid3`) REFERENCES `itemlist` (`compid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderlist`
--

LOCK TABLES `orderlist` WRITE;
/*!40000 ALTER TABLE `orderlist` DISABLE KEYS */;
INSERT INTO `orderlist` VALUES ('O1','C1','2022-04-18','I1S1',1,'I2S1',5,'I3S2',1),('O2','C2','2022-04-19','I2S1',2,'I3S2',4,'I4S2',1),('O3','C3','2022-04-20','I3S2',3,'I4S2',3,'I5S3',1),('O4','C1','2022-04-21','I4S2',4,'I5S3',2,'I3S3',1),('O5','C2','2022-04-22','I5S3',5,'I3S3',1,'I1S1',1);
/*!40000 ALTER TABLE `orderlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoplist`
--

DROP TABLE IF EXISTS `shoplist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoplist` (
  `sid` varchar(5) NOT NULL,
  `sname` varchar(20) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoplist`
--

LOCK TABLES `shoplist` WRITE;
/*!40000 ALTER TABLE `shoplist` DISABLE KEYS */;
INSERT INTO `shoplist` VALUES ('S1','Fruit shop',5,'Lok Fu'),('S2','Phone shop',5,'Mong Kok'),('S3','Book shop',4,'Kowloon Tong');
/*!40000 ALTER TABLE `shoplist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-18  3:55:06
