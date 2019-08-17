-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 17, 2019 at 04:25 AM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diu`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `img_file` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'First <<Blog>>', 'ee', 'first-blog', 'Alhumdulillah!The first blog is being tested!!!', '2019-08-15 23:12:27', 'home-bg.jpg'),
(4, 'AI BD edited', 'CHATBOT', 'CHAT-BOT', 'Search Results\r\nFeatured snippet from the web\r\nRecently, a commercial bank in Bangladesh has launched country\'s first AI-based banking chatbot. ... In Bangladesh, AI can play an effective role in traffic monitoring and management system, national security system, healthcare system, manufacturing and service sectors.', '2019-08-15 23:09:19', ''),
(5, 'AI', 'With proper implementation, AI can greatly catalyze our development', 'AI-DB', 'AI is one of the most impactful and transformational technology in this era of the fourth industrial revolution. Its development started from the 1940s and boosted up in 1950s with some significant milestones. The gradual development of AI continued for the next several decades. \r\n\r\nHowever, the journey was not always that smooth. Initial hype created by the emergence of AI in the late 50s attracted a lot of government and industry funding during the 60s; which quickly dried out in the 70s as expected success was not coming in this field. \r\n\r\n', '2019-08-15 12:41:00', ''),
(9, 'WQkjh', 'jkh ', 'jkh ', 'kjhjk ', '2019-08-16 01:25:04', 'j'),
(11, 'addsad', 'asdsad', 'eer', 'adasd hgas g asajdgj jhgs d jh', '2019-08-16 02:08:20', ''),
(12, 'sdasiu uasd  ', 'sdjh-sad', 'asd-asd', 'sdh a coi usch ucgau cauccc jcchuch hcjh c', '2019-08-16 02:08:47', ''),
(16, 'qwe', 'ewrewwrew', 'ehewr-were-werewr', 'hewhjfhe kjh jewkf hj wejfhwek fj wejkfhwe fe ', '2019-08-17 06:54:53', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(200) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int(20) NOT NULL,
  `job` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `full_name`, `email`, `phone`, `job`, `password`) VALUES
(1, 'tester', 'terter@gmail.com', 238293829, 'Student', '123456'),
(2, 'ami', '123123.sh14@gmail.com', 17, 'DIU Student', '12345'),
(3, 'testter 2', 'tester2@gmail.com', 17, 'Student', '12341'),
(4, 'KHan khan', 'khan@gmail.com', 17, 'Student', '12345'),
(5, 'hey', 'man@gmail.com', 17, 'DIU Student', '12345'),
(6, 'ban', 'ban@gmail.com', 17, 'DIU Student', '23434'),
(7, '', '', 17, 'Select job type', '12345'),
(8, 'weewqe', '', 17, 'Select job type', '12345'),
(9, '2323', '', 17, 'Student', '12345'),
(10, 'ami', 'ami@gmail.com', 17, 'Student', '12345'),
(11, 'JEWEL', 'jewel101020@yahoo.com', 17, 'DIU Student', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `visitor`
--

CREATE TABLE `visitor` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `visitor`
--

INSERT INTO `visitor` (`id`, `name`, `email`, `message`) VALUES
(1, 'sal', 'sal@gmail.com', 'yah testing'),
(2, 'eeerer', '123123.sh14@gmail.com', 'rerh erer eeu '),
(3, 'salman', 'salmanh1101@gmail.comdammm', 'I wanna join here'),
(4, 'JEWEL', 'salmanh1101@gmail.com', 'DJJD SHJS KDH DSK DKJKD ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `visitor`
--
ALTER TABLE `visitor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `visitor`
--
ALTER TABLE `visitor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
