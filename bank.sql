/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 8.0.13 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `account` int(11) NOT NULL,
  `username` char(50) DEFAULT NULL,
  `password` char(50) DEFAULT NULL,
  `country` char(50) DEFAULT NULL,
  `province` char(50) DEFAULT NULL,
  `street` char(50) DEFAULT NULL,
  `door` char(50) DEFAULT NULL,
  `money` int(11) DEFAULT NULL,
  `registerDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `bankname` char(50) DEFAULT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`account`,`username`,`password`,`country`,`province`,`street`,`door`,`money`,`registerDate`,`bankname`) values 
(12345577,'王为','123456','中国','吉林省','怒火街道','481室',9000,'2021-11-20 17:09:47','中国建设银行'),
(12345670,'李四','123456','中国','安徽省','和平街道','461室',230,'2021-11-19 00:00:00','中国农业银行'),
(12345677,'王五','123456','中国','吉林省','怒火街道','481室',8900,'2021-11-19 00:00:00','中国建设银行'),
(12345679,'张三','123456','中国','黑龙江省','苏家屯街道','501室',9000,'2021-11-19 00:00:00','中国银行'),
(12345690,'李二麻子','123456','中国','陕西省','龚华街道','901室',9000,'2021-11-19 00:00:00','招商银行'),
(34377813,'a','a','a','a','a','a',11,'2021-11-20 17:13:40','中国工商银行昌平支行'),
(52050650,'3','3','3','3','3','3',3,'2021-11-20 00:00:00','中国工商银行昌平支行'),
(52358022,'2','2','2','2','2','2',2,'2021-11-19 00:00:00','中国工商银行昌平支行'),
(64852394,'q','1','q','q','q','q',111,'2021-11-01 00:00:00','中国工商银行昌平支行'),
(74239444,'w','w','w','w','w','w',111,'2021-11-20 17:10:17','中国工商银行昌平支行'),
(76399237,'1','1','1','1','1','1',11,'2021-11-09 00:00:00','中国工商银行昌平支行'),
(77342664,'ss','s','s','s','s','s',211,'2021-11-20 17:18:21','中国工商银行昌平支行'),
(81062015,'崔鹏飞','123456','中国','辽宁','昌平','355',10003,'2021-11-19 00:00:00','中国工商银行昌平支行'),
(89888443,'r','r','r','r','r','r',123,'2021-11-20 17:20:04','中国工商银行昌平支行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
