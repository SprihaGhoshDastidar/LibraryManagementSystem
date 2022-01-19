-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: library_management
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
-- Table structure for table `librarym`
--

DROP TABLE IF EXISTS `librarym`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarym` (
  `Member` varchar(20) NOT NULL,
  `PRN` varchar(45) NOT NULL,
  `ID_no` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `PresentAddress` varchar(45) NOT NULL,
  `PermanentAddress` varchar(45) NOT NULL,
  `PostalCode` varchar(45) NOT NULL,
  `PhoneNumber` varchar(45) NOT NULL,
  `Bookid` varchar(45) NOT NULL,
  `BookTitle` varchar(45) NOT NULL,
  `AuthorName` varchar(45) NOT NULL,
  `DateOfIssue` varchar(45) NOT NULL,
  `DateDue` varchar(45) NOT NULL,
  `DaysOnBook` varchar(45) NOT NULL,
  `LateReturnFine` varchar(45) NOT NULL,
  `DateOverdue` varchar(45) NOT NULL,
  `Price` varchar(45) NOT NULL,
  PRIMARY KEY (`PRN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarym`
--

LOCK TABLES `librarym` WRITE;
/*!40000 ALTER TABLE `librarym` DISABLE KEYS */;
INSERT INTO `librarym` VALUES ('Admin','','','','','','','','','BKID5454','Python Programming','Paul Berry','2022-01-19 13:06:52.677604','2022-02-03 13:06:52.677604','15','25','NO','788'),('Student','001','457256','Kiran','Kejriwal','Pune','Pune','256763','8723459109','BKID4040','Introduction to Philosophy','Simon Blackburn','2022-01-19 13:50:30.480744','2022-02-03 13:50:30.480744','15','25','NO','235'),('Lecturer','002','526738','Swarup','Medha','Bangalore','Kolkata','700289','9830238471','BKID2022','Top 10 Project ideas','Paul Berry','2022-01-19 21:14:31.203182','2022-02-03 21:14:31.203182','15','25','NO','1099'),('Admin','003','268639','Sital','Sen','Kolkata','Kolkata','700029','9051348732','BKID5451','Basics of C++','Sunita Arora','2022-01-19 23:34:10.731079','2022-02-03 23:34:10.731079','15','25','NO','485'),('Student','004','268634','Aparna','Deshmukh','Delhi','Delhi','136728','9873422570','BKID5456','ML with python','D.Jules','2022-01-19 23:35:31.604270','2022-02-03 23:35:31.604270','15','25','NO','699'),('Student','005','268634','Steve','Rob','Mumbai','UK','200917','173590992','BKID5457','MySQL database','S.D.Kishore','2022-01-19 23:36:29.633259','2022-02-03 23:36:29.633259','15','25','NO','285'),('Student','006','268634','Sweet','Potato','Mumbai','Mumbai','200912','9981777023','BKID5854','Python Cookbook','S.K.Das','2022-01-19 23:37:14.495740','2022-02-03 23:37:14.495740','15','25','NO','199'),('Lecturer','007','236718','Taylor','Swift','Delhi','Canada','234234','87772209132','BKID5414','Netwotking','Rahul Bose','2022-01-19 23:43:20.407900','2022-02-03 23:43:20.407900','15','25','NO','788'),('Admin','09','dg678','akash','bera','dedd','jnm','12','567890','BKID5454','Python Programming','Paul Berry','2022-01-19 13:09:55.807834','2022-02-03 13:09:55.807834','15','25','NO','788');
/*!40000 ALTER TABLE `librarym` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-19 23:55:12
