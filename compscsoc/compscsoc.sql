-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 27, 2020 at 10:16 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `QsnId` int(11) NOT NULL,
  `Name` varchar(35) NOT NULL,
  `EmailId` varchar(40) NOT NULL,
  `PhoneNum` bigint(17) NOT NULL,
  `Msg` text NOT NULL,
  `DT` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

CREATE TABLE `posts` (
  `PostId` int(11) NOT NULL,
  `PostTitle` varchar(50) NOT NULL,
  `PostContent` text NOT NULL,
  `ImgFile` varchar(30) NOT NULL,
  `PostedBy` varchar(50) NOT NULL,
  `Slug` varchar(50) NOT NULL,
  `DT` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`PostId`, `PostTitle`, `PostContent`, `ImgFile`, `PostedBy`, `Slug`, `DT`) VALUES
(1, 'Feynman', 'These are the lectures in physics that I gave last year and the year before to the freshman and sophomore classes at Caltech. The lectures are, of course, not verbatim—they have been edited, sometimes extensively and sometimes less so. The lectures form only part of the complete course. The whole group of 180 students gathered in a big lecture room twice a week to hear these lectures and then they broke up into small groups of 15 to 20 students in recitation sections under the guidance of a teaching assistant. In addition, there was a laboratory session once a week. The special problem we tried to get at with these lectures was to maintain the interest of the very enthusiastic and rather smart students coming out of the high schools and into Caltech. They have heard a lot about how interesting and exciting physics is—the theory of relativity, quantum mechanics, and other modern ideas. By the end of two years of our previous course, many would be very discouraged because there were really very few grand, new, modern ideas presented to them. They were made to study inclined planes, electrostatics, and so forth, and after two years it was quite stultifying. The problem was whether or not we could make a course which would save the more advanced and excited student by maintaining his enthusiasm. Thelecturesherearenotinanywaymeanttobeasurveycourse, butarevery serious. Ithoughttoaddressthemtothemostintelligentintheclassandtomake sure, if possible, that even the most intelligent student was unable to completely encompass everything that was in the lectures—by putting in suggestions of\r\n', 'post-bg.jpg', 'Me', 'hell', '2020-08-26 09:13:00'),
(2, 'Flask in Python', 'It is not possible to write front-end course every time user make changes in his/her profile. We use a template and it generates code according to the content.\r\n\r\nFlask is one of the web development frameworks written in Python. Through flask, a loop can be run in the HTML code using jinja template and automatically HTML code can be generated using this.\r\n\r\nThe code will be stored in Directories in the format of Flask. So we will be making two directories,\r\n\r\nstatic – For static Files like images, css, js\r\ntemplates – For Html templates\r\napp.py file which will contain all the Python file will be stored in the main directory and index.html file will be stored in templates.', 'about-bg-jpg', 'Mahaan', 'Flask', '2020-08-27 13:20:59'),
(3, 'ChempHY', 'say in water, and we put a big ball of something in the water, a ball much bigger than the atoms, the ball will jiggle around—much as in a push ball game, where a great big ball is pushed around by a lot of people. The people are pushing in various directions, and the ball moves around the ?eld in an irregular fashion. So, in the same way, the “large ball” will move because of the inequalities of the collisions on one side to the other, from one moment to the next. Therefore, if we look at very tiny particles (colloids) in water through an excellent microscope, we see a perpetual jiggling of the particles, which is the result of the bombardment of the atoms. This is called the Brownian motion. We can see further evidence for atoms in the structure of crystals. In many cases the structures deduced by x-ray analysis agree in their spatial “shapes” with the forms actually exhibited by crystals as they occur in nature. The angles between the various “faces” of a crystal agree, within seconds of arc, with angles deduced on the assumption that a crystal is made of many “layers” of atoms. Everything is made of atoms. Thatisthekeyhypothesis. Themostimportant hypothesisinallofbiology, forexample, isthat everything that animals do, atoms\r\n1-8\r\ndo. Inotherwords, there is nothing that living things do that cannot be understood from the point of view that they are made of atoms acting according to the laws of physics. This was not known from the beginning: it took some experimenting and theorizing to suggest this hypothesis, but now it is accepted, and it is the most useful theory for producing new ideas in the ?eld of biology. If a piece of steel or a piece of salt, consisting of atoms one next to the other, can have such interesting properties; if water—which is nothing but these little blobs, mile upon mile of the same thing over the earth—can form waves and foam, and make rushing noises and strange patterns as it runs over cement; if all of this, all the life of a stream of water, can be nothing but a pile of atoms, how much more is possible? If instead of arranging the atoms in some de?nite pattern, again and again repeated, on and on, or even forming little lumps of complexity like the odor of violets, we make an arrangement which is always di?erent from place to place, with di?erent kinds of atoms arranged in many ways, continually changing, notrepeating, how muchmore marvelously is itpossible thatthis thing might behave? Is it possible that that “thing” walking back and forth in front of you, talking to you, is a great glob of these atoms in a very complex arrangement, such that the sheer complexity of it staggers the imagination as to what it can do? When we say we are a pile of atoms, we do not mean we are merely a pile of atoms, because a pile of atoms which is not repeated from one to the other might well have the possibilities which you see before you in the mirror.\r\n', '', 'NOONE', '110', '2020-08-27 13:24:54'),
(4, 'Citric and cycle', 'branches out into ?ne little things, connected to a structure near a muscle, called an endplate. For reasons which are not exactly understood, when the impulse reaches the end of the nerve, little packets of a chemical called acetylcholine are shoto?(?veortenmoleculesatatime)andtheya?ectthemuscle?berandmake it contract—how simple! What makes a muscle contract? A muscle is a very large number of ?bers close together, containing two di?erent substances, myosin and actomyosin, but the machinery by which the chemical reaction induced by acetylcholinecan modifythedimensionsofthemuscleisnotyetknown. Thusthe fundamentalprocessesinthemusclethatmakemechanicalmotionsarenotknown. Biologyissuchanenormouslywide?eldthattherearehostsofotherproblems that we cannot mention at all—problems on how vision works (what the light does in the eye), how hearing works, etc. (The way in which thinking works we shall discuss later under psychology.) Now, these things concerning biology which we have just discussed are, from a biological standpoint, really not fundamental, at the bottom of life, in the sense that even if we understood them we still would not understand life itself. To illustrate: the men who study nerves feel their work is very important, because after all you cannot have animals without nerves. But you can have life without nerves. Plants have neither nerves nor muscles, but they are working, they are alive, just the same. So for the fundamental problems of biology we must look deeper; when we do, we discover that all living things have a great many characteristics in common. The most common feature is that they are made of cells, within each of which is complex machinery for doing things chemically. In plant cells, for example, there is machinery for picking up light and generating glucose, which is consumed in the dark to keep the plant alive. When the plant is eaten the glucose itself generates in the animal a series of chemical reactions very closely related to photosynthesis (and its opposite e?ect in the dark) in plants. In the cells of living systems there are many elaborate chemical reactions, in which one compound is changed into another and another. To give some impression of the enormous e?orts that have gone into the study of biochemistry, the chart in Fig. 3-1 summarizes our knowledge to date on just one small part of the many series of reactions which occur in cells, perhaps a percent or so of it. Here we see a whole series of molecules which change from one to another in a sequenceorcycleofrathersmallsteps. ItiscalledtheKrebscycle,therespiratory cycle. Each of the chemicals and each of the steps is fairly simple, in terms of what change is made in the molecule, but—and this is a centrally important discoveryin biochemistry—thesechangesare relatively di?cult to accomplish in a laboratory. If we have one substance and another very similar substance, the ', '', 'Ravi', 'CandC', '2020-08-27 13:26:23'),
(5, 'NueWaves', 'This fact also has an interesting consequence in the case of piles which make neutrons (these are obviously particles, for anybody’s money!). If we take these neutrons and let them into a long block of graphite, the neutrons di?use and work their way along (Fig. 2-7). They di?use because they are bounced by the atoms, but strictly, in the wave theory, they are bounced by the atoms because of di?raction from the crystal planes. It turns out that if we take a very long piece of graphite, the neutrons that come out the far end are all of long wavelength! In fact, if one plots the intensity as a function of wavelength, we get nothing except for wavelengths longer than a certain minimum (Fig. 2-8). In other words, we can get very slow neutrons that way. Only the slowest neutrons come through; they are not di?racted or scattered by the crystal planes of the graphite, but keep going right through like light through glass, and are not scattered out the sides. There are many other demonstrations of the reality of neutron waves and waves of other particles', '', 'BKP', 'Wave', '2020-08-27 13:27:49'),
(6, 'Mecha uni', 'drop will land on our nose. This appears to be completely random, yet such a behavior would be predicted by purely classical laws. The exact position of all the drops depends upon the precise wigglings of the water before it goes over the dam. How? The tiniest irregularities are magni?ed in falling, so that we get complete randomness. Obviously, we cannot really predict the position of the drops unless we know the motion of the water absolutely exactly. Speaking more precisely, given an arbitrary accuracy, no matter how precise, one can ?nd a time long enough that we cannot make predictions valid for that long a time. Now the point is that this length of time is not very large. It is not that the time is millions of years if the accuracy is one part in a billion. The time goes, in fact, only logarithmically with the error, and it turns out that in only a very, very tiny time we lose all our information. If the accuracy is taken to be one part in billions and billions and billions—no matter how many billions we wish, provided we do stop somewhere—then we can ?nd a time less than the time it took to state the accuracy—after which we can no longer predict what is going to happen! It is therefore not fair to say that from the apparent freedom and indeterminacy of the human mind, we should have realized that classical “deterministic” physics could not ever hope to understand it, and to welcome quantum mechanics as a release from a “completely mechanistic” universe', '', 'UNIT', 'uniy', '2020-08-27 13:28:50');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Sno` int(11) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `EmailId` varchar(40) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Contact` int(11) NOT NULL,
  `College` varchar(60) NOT NULL,
  `DT` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`QsnId`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`PostId`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `QsnId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `PostId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `Sno` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
