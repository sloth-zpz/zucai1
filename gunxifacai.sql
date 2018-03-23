/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : gunxifacai

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-03-23 13:27:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gunqiu
-- ----------------------------
DROP TABLE IF EXISTS `gunqiu`;
CREATE TABLE `gunqiu` (
  `id` varchar(20) NOT NULL,
  `jingcai_id` varchar(30) DEFAULT NULL,
  `duiwu` varchar(255) DEFAULT NULL,
  `goal_z` int(10) DEFAULT NULL,
  `goal_k` int(10) DEFAULT NULL,
  `pankou` varchar(255) DEFAULT NULL,
  `goal_detail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
