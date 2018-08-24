-- MySQL dump 10.13  Distrib 8.0.12, for Linux (x86_64)
--
-- Host: localhost    Database: hpshSystem
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_table`
--

DROP TABLE IF EXISTS `auth_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_table` (
  `ftable_name` varchar(64) NOT NULL COMMENT 'table name',
  `flevel_id` int(11) NOT NULL COMMENT 'level id',
  `fadd_time` timestamp NULL DEFAULT NULL COMMENT 'add time',
  `fupdate_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'update time'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='auth table';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_table`
--

LOCK TABLES `auth_table` WRITE;
/*!40000 ALTER TABLE `auth_table` DISABLE KEYS */;
INSERT INTO `auth_table` VALUES ('game_activity',1,NULL,NULL);
/*!40000 ALTER TABLE `auth_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_activity`
--

DROP TABLE IF EXISTS `game_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `game_activity` (
  `fdate` varchar(64) DEFAULT NULL,
  `fgame_name` varchar(64) DEFAULT NULL,
  `fcount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_activity`
--

LOCK TABLES `game_activity` WRITE;
/*!40000 ALTER TABLE `game_activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_user_age`
--

DROP TABLE IF EXISTS `game_user_age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `game_user_age` (
  `fdate` varchar(64) DEFAULT NULL,
  `fgame_time` int(11) DEFAULT NULL,
  `fage` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_user_age`
--

LOCK TABLES `game_user_age` WRITE;
/*!40000 ALTER TABLE `game_user_age` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_user_age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `level_info`
--

DROP TABLE IF EXISTS `level_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `level_info` (
  `flevel_id` int(11) NOT NULL COMMENT 'level id',
  `flevel_name` varchar(64) NOT NULL COMMENT 'level name',
  `fadd_time` timestamp NULL DEFAULT NULL COMMENT 'add time',
  `fupdate_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'update time'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='level info';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level_info`
--

LOCK TABLES `level_info` WRITE;
/*!40000 ALTER TABLE `level_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `level_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_info` (
  `fname` varchar(64) NOT NULL COMMENT 'user name',
  `fwork_id` int(11) NOT NULL COMMENT 'work id',
  `fdept_id` int(11) NOT NULL COMMENT 'department id',
  `flevel_id` int(11) NOT NULL COMMENT 'level id',
  `fpassword` varchar(64) NOT NULL COMMENT 'password',
  `fadd_time` timestamp NULL DEFAULT NULL COMMENT 'add time',
  `fupdate_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'update time'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='user info';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES ('章三',1001,1,1,'password',NULL,NULL);
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-24 21:04:54
