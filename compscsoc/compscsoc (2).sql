-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 26, 2020 at 03:46 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `compscsoc`
--
CREATE DATABASE IF NOT EXISTS `compscsoc` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `compscsoc`;

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--
-- Creation: Aug 25, 2020 at 02:36 PM
--

DROP TABLE IF EXISTS `contact`;
CREATE TABLE IF NOT EXISTS `contact` (
  `QsnId` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(35) NOT NULL,
  `EmailId` varchar(40) NOT NULL,
  `PhoneNum` bigint(17) NOT NULL,
  `Msg` text NOT NULL,
  `DT` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`QsnId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `contact`:
--

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`QsnId`, `Name`, `EmailId`, `PhoneNum`, `Msg`, `DT`) VALUES
(1, 'who create it', 'Ebsn@hg.com', 728391837, 'Hello This is a test message', '2020-08-25 15:57:18'),
(4, 'Bill Gate', 'newbloger@yahoo.com', 68534678558, 'I Like this blog really ', '2020-08-25 22:19:27'),
(5, 'ww', 'hjk2jk@s', 68523735726, '2werg', '2020-08-25 22:55:50'),
(6, 'ys', '526@t678', 2345678, 'w', '2020-08-25 23:18:50'),
(7, 'ys', '526@t678', 2345678, 'w', '2020-08-25 23:23:43'),
(8, 'Harsh bindal', 'sf@vbhjk', 456789, 's', '2020-08-26 18:12:55');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--
-- Creation: Aug 26, 2020 at 01:30 PM
--

DROP TABLE IF EXISTS `posts`;
CREATE TABLE IF NOT EXISTS `posts` (
  `PostId` int(11) NOT NULL AUTO_INCREMENT,
  `PostTitle` varchar(50) NOT NULL,
  `PostContent` text NOT NULL,
  `ImgFile` varchar(30) NOT NULL,
  `PostedBy` varchar(50) NOT NULL,
  `Slug` varchar(50) NOT NULL,
  `DT` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`PostId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `posts`:
--

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`PostId`, `PostTitle`, `PostContent`, `ImgFile`, `PostedBy`, `Slug`, `DT`) VALUES
(1, 'Feynman', 'These are the lectures in physics that I gave last year and the year before to the freshman and sophomore classes at Caltech. The lectures are, of course, not verbatim—they have been edited, sometimes extensively and sometimes less so. The lectures form only part of the complete course. The whole group of 180 students gathered in a big lecture room twice a week to hear these lectures and then they broke up into small groups of 15 to 20 students in recitation sections under the guidance of a teaching assistant. In addition, there was a laboratory session once a week. The special problem we tried to get at with these lectures was to maintain the interest of the very enthusiastic and rather smart students coming out of the high schools and into Caltech. They have heard a lot about how interesting and exciting physics is—the theory of relativity, quantum mechanics, and other modern ideas. By the end of two years of our previous course, many would be very discouraged because there were really very few grand, new, modern ideas presented to them. They were made to study inclined planes, electrostatics, and so forth, and after two years it was quite stultifying. The problem was whether or not we could make a course which would save the more advanced and excited student by maintaining his enthusiasm. Thelecturesherearenotinanywaymeanttobeasurveycourse, butarevery serious. Ithoughttoaddressthemtothemostintelligentintheclassandtomake sure, if possible, that even the most intelligent student was unable to completely encompass everything that was in the lectures—by putting in suggestions of\r\n', 'post-bg.jpg', 'Me', 'hell', '2020-08-26 09:13:00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--
-- Creation: Aug 23, 2020 at 02:34 PM
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `Sno` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(40) NOT NULL,
  `EmailId` varchar(40) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Contact` int(11) NOT NULL,
  `College` varchar(60) NOT NULL,
  `DT` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONSHIPS FOR TABLE `users`:
--
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
