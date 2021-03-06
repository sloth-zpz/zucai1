/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : gunxifacai

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-06-14 18:17:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for shijiebei
-- ----------------------------
DROP TABLE IF EXISTS `shijiebei`;
CREATE TABLE `shijiebei` (
  `id` varchar(255) NOT NULL,
  `game` varchar(255) DEFAULT NULL,
  `changci` varchar(255) DEFAULT NULL,
  `name_zhu` varchar(255) DEFAULT NULL,
  `name_ke` varchar(255) DEFAULT NULL,
  `half` varchar(255) DEFAULT NULL,
  `whole` varchar(255) DEFAULT NULL,
  `first_goal_team` varchar(255) DEFAULT NULL,
  `first_goal_time` int(10) DEFAULT NULL,
  `goal_decs` varchar(255) DEFAULT NULL,
  `ouzhi` varchar(255) DEFAULT NULL,
  `yazhi` varchar(255) DEFAULT NULL,
  `daxiao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shijiebei
-- ----------------------------
INSERT INTO `shijiebei` VALUES ('422192', '世界杯', '小组赛', '巴西', '克罗地亚', '1 - 1', '3-1', '客队', '11', '11分 0-1,29分 1-1,71分 2-1,91分 3-1,', ' 1.29,5.50, 9.50|1.33,5.00,13.00|0.94,1.02,0.80|0.97,0.93,1.10|', '0.950,球半,0.975|1.075↑,球半,0.850↓|', '1.02,2.5/3,0.88|0.90↑,2/2.5,1.00↓|');
INSERT INTO `shijiebei` VALUES ('422193', '世界杯', '小组赛', '墨西哥', '喀麦隆', '0 - 0', '1-0', '主队', '61', '61分 1-0,', ' 2.15,3.10, 3.60|2.20,3.20,3.90|0.93,0.94,0.95|0.95,0.97,1.03|', '1.149,半球,0.800|0.875↓,平手/半球,1.049↑|', '0.88,2,1.02|0.98↑,2,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422194', '世界杯', '小组赛', '巴西', '墨西哥', '0-0', '0 - 0', null, null, null, ' 1.33,5.00, 8.50|1.36,5.25,10.00|0.95,0.91,0.87|0.97,0.96,1.02|', '1.100,球半/两球,0.825|0.899↓,一球/球半,1.024↑|', '0.75,2.5,1.05|0.93↓,2.5/3,0.98↑|');
INSERT INTO `shijiebei` VALUES ('422195', '世界杯', '小组赛', '喀麦隆', '克罗地亚', '0 - 1', '0-4', '客队', '11', '11分 0-1,48分 0-2,61分 0-3,73分 0-4,', ' 4.20,3.30, 1.91|5.75,4.00,1.67|0.74,0.82,1.10|1.01,0.99,0.96|', '0.925,受半球,1.000|1.049↓,受半球/一球,0.875↑|', '1.10,2.5,0.70|0.98↑,2.5,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422196', '世界杯', '小组赛', '巴西', '喀麦隆', '2 - 1', '4-1', '主队', '17', '17分 1-0,26分 1-1,34分 2-1,49分 3-1,84分 4-1,', ' 1.20,6.50, 13.00|1.13,10.00,26.00|1.01,0.72,0.62|0.95,1.11,1.23|', '1.100,两球,0.825|0.875↓,两球半,1.049↑|', '0.90,2.5/3,1.00|0.93↓,3.5,0.98↑|');
INSERT INTO `shijiebei` VALUES ('422197', '世界杯', '小组赛', '克罗地亚', '墨西哥', '0 - 0', '1-3', '客队', '72', '72分 0-1,75分 0-2,82分 0-3,87分 1-3,', ' 2.40,3.30, 2.88|2.75,3.60,2.63|0.86,0.94,1.02|0.99,1.03,0.93|', '1.049,平手/半球,0.875|0.975↓,平手,0.950↑|', '1.02,2/2.5,0.88|1.00↑,2.5↑,0.80↓|');
INSERT INTO `shijiebei` VALUES ('422198', '世界杯', '小组赛', '西班牙', '荷兰', '1 - 1', '1-5', '主队', '27', '27分 1-0,44分 1-1,53分 1-2,64分 1-3,72分 1-4,80分 1-5,', ' 2.10,3.25, 3.60|1.85,3.40,5.25|1.09,0.92,0.72|0.96,0.97,1.05|', '1.049,半球,0.875|0.875,半球,1.049|', '1.08,2/2.5,0.82|1.05↓,2/2.5,0.85↑|');
INSERT INTO `shijiebei` VALUES ('422199', '世界杯', '小组赛', '智利', '澳大利亚', '2 - 1', '3-1', '主队', '12', '12分 1-0,14分 2-0,35分 2-1,92分 3-1,', ' 1.53,3.75, 7.00|1.44,4.50,9.00|1.01,0.84,0.82|0.95,1.00,1.05|', '0.925,一球,1.000|1.049↓,一球/球半,0.875↑|', '0.85,2/2.5,1.05|0.98↑,2.5,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422200', '世界杯', '小组赛', '西班牙', '智利', '0 - 2', '0-2', '客队', '19', '19分 0-1,43分 0-2,', ' 1.73,3.30, 5.50|1.60,4.50,5.50|1.05,0.73,0.94|0.97,1.00,0.94|', '1.000,半球/一球,0.925|1.049↑,一球,0.875↓|', '0.90,2.5,0.90|0.88↑,2.5/3,1.02↑|');
INSERT INTO `shijiebei` VALUES ('422201', '世界杯', '小组赛', '澳大利亚', '荷兰', '1 - 1', '2-3', '客队', '20', '20分 0-1,21分 1-1,54分 2-1,58分 2-2,68分 2-3,', ' 11.00,5.00, 1.29|13.00,7.00,1.25|0.80,0.74,1.01|0.95,1.03,0.97|', '0.850,受球半,1.075|0.980↓,受球半,0.830↑|', '0.65,2.5,1.20|1.05↑,3↑,0.85↓|');
INSERT INTO `shijiebei` VALUES ('422202', '世界杯', '小组赛', '澳大利亚', '西班牙', '0 - 1', '0-3', '客队', '36', '36分 0-1,69分 0-2,82分 0-3,', ' 15.00,6.50, 1.18|9.00,5.50,1.36|1.89,1.25,0.80|1.13,1.06,0.93|', '1.000,受球半/两球,0.925|0.975↑,受球半,0.950↓|', '0.90,2.5/3,1.00|0.88↓,3/3.5,1.02↑|');
INSERT INTO `shijiebei` VALUES ('422203', '世界杯', '小组赛', '荷兰', '智利', '0 - 0', '2-0', '主队', '77', '77分 1-0,92分 2-0,', ' 2.20,3.40, 3.20|2.75,3.60,2.60|0.81,0.95,1.12|1.02,1.01,0.91|', '1.000,平手/半球,0.925|1.049↑,平手,0.875↓|', '1.00,2.5,0.90|0.88↑,2.5,1.02↓|');
INSERT INTO `shijiebei` VALUES ('422204', '世界杯', '小组赛', '哥伦比亚', '希腊', '1 - 0', '3-0', '主队', '5', '5分 1-0,58分 2-0,93分 3-0,', ' 1.67,3.50, 5.50|1.85,3.30,5.50|0.86,1.02,1.05|0.96,0.96,1.05|', '0.975,半球/一球,0.925|0.875↑,半球,1.024↓|', '0.82,2,1.08|0.88↓,1.5/2,1.02↑|');
INSERT INTO `shijiebei` VALUES ('422205', '世界杯', '小组赛', '科特迪瓦', '日本', '0 - 1', '2-1', '客队', '16', '16分 0-1,64分 1-1,66分 2-1,', ' 2.63,3.00, 2.88|2.63,3.20,3.00|0.96,0.90,0.97|0.96,0.96,1.01|', '0.850,平手,1.075|0.850↑,平手,1.075↓|', '0.90,2,1.00|0.98↓,2/2.5,0.93↑|');
INSERT INTO `shijiebei` VALUES ('422206', '世界杯', '小组赛', '哥伦比亚', '科特迪瓦', '0 - 0', '2-1', '主队', '64', '64分 1-0,70分 2-0,73分 2-1,', ' 1.91,3.40, 4.00|2.05,3.60,3.80|0.88,0.95,1.03|0.95,1.00,0.98|', '1.000,半球,0.925|1.024↓,半球,0.899↑|', '1.20,2.5,0.65|0.95↓,2.5,0.95↑|');
INSERT INTO `shijiebei` VALUES ('422207', '世界杯', '小组赛', '日本', '希腊', '0-0', '0 - 0', null, null, null, ' 2.50,3.30, 2.75|2.50,3.40,3.00|1.04,0.95,0.81|1.04,0.98,0.89|', '0.825,平手,1.100|1.149↑,平手/半球,0.800↓|', '1.50,2.5,0.50|0.85↓,2/2.5,1.05↑|');
INSERT INTO `shijiebei` VALUES ('422208', '世界杯', '小组赛', '日本', '哥伦比亚', '1 - 1', '1-4', '客队', '17', '17分 0-1,46分 1-1,55分 1-2,82分 1-3,89分 1-4,', ' 4.33,3.50, 1.83|3.50,3.80,2.10|1.18,0.93,0.84|0.96,1.01,0.97|', '1.000,受半球,0.925|0.770↓,受半球,1.020↑|', '1.05,2/2.5,0.85|0.95↓,2.5/3,0.95↑|');
INSERT INTO `shijiebei` VALUES ('422209', '世界杯', '小组赛', '希腊', '科特迪瓦', '1 - 0', '2-1', '主队', '42', '42分 1-0,74分 1-1,93分 2-1,', ' 3.00,3.25, 2.38|4.10,3.70,1.95|0.75,0.88,1.14|1.02,1.00,0.93|', '0.825,受平手/半球,1.100|0.950↑,受半球,0.975↓|', '1.08,2/2.5,0.82|1.02↓,2.5,0.88↑|');
INSERT INTO `shijiebei` VALUES ('422210', '世界杯', '小组赛', '乌拉圭', '哥斯达黎加', '1 - 0', '1-3', '主队', '24', '24分 1-0,54分 1-1,57分 1-2,84分 1-3,', ' 1.33,4.50, 11.00|1.44,4.33,9.50|0.88,1.01,1.24|0.95,0.98,1.07|', '0.875,一球/球半,1.049|0.850↑,一球,1.075↓|', '1.00,2.5,0.80|1.05↓,2/2.5,0.85↑|');
INSERT INTO `shijiebei` VALUES ('422211', '世界杯', '小组赛', '英格兰', '意大利', '1 - 1', '1-2', '', '-1', '', ' 3.00,3.00, 2.50|2.50,3.00,3.40|1.06,0.96,0.82|0.88,0.96,1.12|', '0.730,受平手/半球,1.080|1.100↑,平手/半球,0.825↓|', '1.00,2,0.90|0.85↑,2,1.05↓|');
INSERT INTO `shijiebei` VALUES ('422212', '世界杯', '小组赛', '乌拉圭', '英格兰', '1 - 0', '2-1', '主队', '39', '39分 1-0,75分 1-1,85分 2-1,', ' 2.38,3.25, 3.00|3.90,3.90,1.95|0.63,0.87,1.41|1.03,1.04,0.91|', '1.100,平手/半球,0.825|0.975↑,受半球,0.950↓|', '1.05,2.5,0.75|0.93↓,2.5/3,0.98↑|');
INSERT INTO `shijiebei` VALUES ('422213', '世界杯', '小组赛', '意大利', '哥斯达黎加', '0 - 1', '0-1', '客队', '44', '44分 0-1,', ' 1.33,5.00, 9.00|1.62,4.00,6.50|0.83,1.17,1.29|1.01,0.94,0.93|', '1.075,球半,0.850|1.100↑,一球,0.825↓|', '0.90,2.5,0.90|0.93↑,2/2.5,0.98↓|');
INSERT INTO `shijiebei` VALUES ('422214', '世界杯', '小组赛', '意大利', '乌拉圭', '0 - 0', '0-1', '客队', '81', '81分 0-1,', ' 2.50,3.30, 2.75|2.60,3.60,2.75|0.93,0.94,0.94|0.97,1.03,0.94|', '0.875,平手,1.049|0.950↑,平手,0.975↓|', '0.83,2/2.5,0.98|1.00↑,2.5,0.90↓|');
INSERT INTO `shijiebei` VALUES ('422215', '世界杯', '小组赛', '哥斯达黎加', '英格兰', '0-0', '0 - 0', null, null, null, ' 7.00,4.33, 1.44|4.75,4.10,1.75|1.53,1.08,0.77|1.04,1.02,0.93|', '0.850,受一球/球半,1.075|0.950↑,受半球/一球,0.975↓|', '0.80,2.5,1.00|0.83↑,2.5,0.98↓|');
INSERT INTO `shijiebei` VALUES ('422216', '世界杯', '小组赛', '瑞士', '厄瓜多尔', '0 - 1', '2-1', '客队', '22', '22分 0-1,48分 1-1,93分 2-1,', ' 2.25,3.00, 3.50|2.55,3.20,3.10|0.89,0.91,1.05|1.01,0.97,0.93|', '0.975,平手/半球,0.950|1.149↑,平手/半球,0.800↓|', '0.98,2,0.93|1.02↑,2/2.5,0.88↓|');
INSERT INTO `shijiebei` VALUES ('422217', '世界杯', '小组赛', '法国', '洪都拉斯', '1 - 0', '3-0', '主队', '45', '45分 1-0,48分 2-0,72分 3-0,', ' 1.25,5.25, 13.00|1.25,6.50,14.00|0.92,0.93,1.10|0.92,1.15,1.19|', '0.950,球半,0.975|1.020↑,球半/两球,0.770↓|', '1.00,2.5,0.80|1.00↑,2.5/3,0.90↓|');
INSERT INTO `shijiebei` VALUES ('422218', '世界杯', '小组赛', '瑞士', '法国', '0 - 3', '2-5', '客队', '17', '17分 0-1,18分 0-2,40分 0-3,67分 0-4,73分 0-5,81分 1-5,87分 2-5,', ' 3.50,3.30, 2.10|4.50,3.60,1.91|0.72,0.89,1.10|0.93,0.98,1.00|', '0.925,受半球,1.000|1.049↑,受半球,0.875↓|', '1.10,2.5,0.70|1.05↓,2/2.5,0.85↑|');
INSERT INTO `shijiebei` VALUES ('422219', '世界杯', '小组赛', '洪都拉斯', '厄瓜多尔', '1 - 1', '1-2', '主队', '31', '31分 1-0,34分 1-1,65分 1-2,', ' 4.75,3.60, 1.73|6.00,4.25,1.60|0.81,0.86,1.02|1.03,1.02,0.94|', '0.925,受半球/一球,1.000|0.899↓,受一球,1.024↑|', '0.90,2.5,0.90|0.98↑,2.5/3↑,0.83↓|');
INSERT INTO `shijiebei` VALUES ('422220', '世界杯', '小组赛', '洪都拉斯', '瑞士', '0 - 2', '0-3', '客队', '6', '6分 0-1,31分 0-2,71分 0-3,', ' 6.50,3.80, 1.53|7.50,4.50,1.50|0.85,0.82,1.00|0.98,0.97,0.98|', '0.925,受一球,1.000|0.774↓,受一球/球半,1.174↑|', '1.02,2.5,0.88|0.98↑,2.5/3,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422221', '世界杯', '小组赛', '厄瓜多尔', '法国', '0-0', '0 - 0', null, null, null, ' 4.33,3.50, 1.83|6.00,4.20,1.62|0.79,0.84,1.06|1.09,1.00,0.94|', '1.000,受半球,0.925|1.000↓,受半球/一球,0.800↑|', '0.80,2/2.5,1.00|1.05↑,3↑,0.75↓|');
INSERT INTO `shijiebei` VALUES ('422222', '世界杯', '小组赛', '阿根廷', '波黑', '1 - 0', '2-1', '', '-1', '', ' 1.40,4.50, 8.00|1.30,5.75,12.00|0.99,0.84,0.86|0.92,1.08,1.28|', '0.950,一球/球半,0.975|0.975↑,球半,0.950↓|', '1.02,2.5/3,0.88|1.00↑,3,0.90↓|');
INSERT INTO `shijiebei` VALUES ('422223', '世界杯', '小组赛', '伊朗', '尼日利亚', '0-0', '0 - 0', null, null, null, ' 4.20,3.10, 2.00|5.00,3.50,1.85|0.95,0.88,0.98|1.13,1.00,0.90|', '0.925,受半球,1.000|1.075↑,受半球,0.850↓|', '1.00,2,0.90|1.08↑,2/2.5,0.82↓|');
INSERT INTO `shijiebei` VALUES ('422224', '世界杯', '小组赛', '阿根廷', '伊朗', '0 - 0', '1-0', '主队', '91', '91分 1-0,', ' 1.17,7.00, 15.00|1.14,9.00,23.00|0.98,0.79,0.71|0.96,1.02,1.09|', '1.000,两球,0.925|1.075↑,两球,0.850↓|', '0.55,2.5,1.38|1.08↑,3,0.82↓|');
INSERT INTO `shijiebei` VALUES ('422225', '世界杯', '小组赛', '尼日利亚', '波黑', '1 - 0', '1-0', '', '-1', '', ' 3.00,3.25, 2.38|4.50,3.60,1.91|0.68,0.88,1.20|1.01,0.97,0.97|', '1.100,平手,0.825|1.049↑,受半球,0.875↓|', '0.90,2.5,0.90|0.85↓,2.5,1.05↑|');
INSERT INTO `shijiebei` VALUES ('422226', '世界杯', '小组赛', '尼日利亚', '阿根廷', '1 - 2', '2-3', '客队', '3', '3分 0-1,4分 1-1,46分 1-2,47分 2-2,50分 2-3,', ' 9.00,5.00, 1.33|10.00,4.33,1.44|1.00,1.18,0.87|1.11,1.03,0.94|', '0.899,受球半,1.024|1.075↑,受一球/球半,0.850↓|', '0.95,2.5/3,0.95|0.93↓,2.5/3,0.98↑|');
INSERT INTO `shijiebei` VALUES ('422227', '世界杯', '小组赛', '波黑', '伊朗', '1 - 0', '3-1', '', '-1', '', ' 1.57,3.80, 6.00|2.20,3.60,3.40|0.70,1.05,1.65|0.99,0.99,0.94|', '1.075,一球,0.850|0.875↓,平手/半球,1.049↑|', '1.00,2/2.5,0.90|0.93↓,2/2.5,0.98↑|');
INSERT INTO `shijiebei` VALUES ('422228', '世界杯', '小组赛', '德国', '葡萄牙', '3 - 0', '4-0', '主队', '12', '12分 1-0,32分 2-0,46分 3-0,78分 4-0,', ' 1.91,3.40, 4.00|2.15,3.50,3.60|0.90,0.94,1.02|1.01,0.96,0.92|', '0.925,半球,1.000|0.800↑,平手/半球,1.000↓|', '1.00,2.5,0.80|0.95↑,2.5,0.95↓|');
INSERT INTO `shijiebei` VALUES ('422229', '世界杯', '小组赛', '加纳', '美国', '0 - 1', '1-2', '', '-1', '', ' 2.50,3.20, 2.88|2.50,3.40,3.00|0.97,0.93,0.93|0.97,0.98,0.97|', '1.149,平手/半球,0.800|1.149↑,平手/半球,0.800↓|', '0.88,2,1.02|0.98↑,2/2.5,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422230', '世界杯', '小组赛', '德国', '加纳', '0 - 0', '2-2', '主队', '51', '51分 1-0,54分 1-1,63分 1-2,71分 2-2,', ' 1.36,4.75, 8.50|1.36,5.50,9.50|0.99,0.82,0.87|0.99,0.95,0.97|', '1.000,球半,0.925|0.770↓,一球/球半,1.020↑|', '0.65,2.5,1.20|1.00↓,3,0.90↑|');
INSERT INTO `shijiebei` VALUES ('422231', '世界杯', '小组赛', '美国', '葡萄牙', '0 - 1', '2-2', '', '-1', '', ' 5.50,3.50, 1.67|4.50,4.00,1.80|1.16,0.87,0.90|0.95,1.00,0.97|', '0.975,受半球/一球,0.950|0.899↓,受半球/一球,1.024↑|', '0.85,2.5,0.95|1.00↑,2.5/3,0.90↓|');
INSERT INTO `shijiebei` VALUES ('422232', '世界杯', '小组赛', '美国', '德国', '0 - 0', '0-1', '', '-1', '', ' 7.50,4.50, 1.40|9.00,3.20,1.67|0.84,1.42,0.80|1.01,1.01,0.95|', '0.925,受一球/球半,1.000|0.770↓,受一球,1.020↑|', '0.95,2.5/3,0.95|0.98↑,2.5,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422233', '世界杯', '小组赛', '葡萄牙', '加纳', '1 - 0', '2-1', '主队', '30', '30分 1-0,57分 1-1,80分 2-1,', ' 1.80,3.50, 4.50|1.73,5.00,4.00|0.92,0.78,1.21|0.88,1.11,1.07|', '0.825,半球,1.100|1.080↑,一球,0.730↓|', '1.05,2.5,0.85|0.93↓,3.5,0.88↑|');
INSERT INTO `shijiebei` VALUES ('422234', '世界杯', '小组赛', '比利时', '阿尔及利亚', '0 - 1', '2-1', '客队', '24', '24分 0-1,70分 1-1,80分 2-1,', ' 1.36,4.75, 8.50|1.33,5.50,11.00|0.95,0.92,0.90|0.93,1.07,1.17|', '0.950,一球/球半,0.975|1.100↑,球半,0.825↓|', '1.00,2.5,0.80|0.95↑,2.5/3,0.95↓|');
INSERT INTO `shijiebei` VALUES ('422235', '世界杯', '小组赛', '俄罗斯', '韩国', '0 - 0', '1-1', '', '-1', '', ' 2.00,3.20, 4.00|1.85,3.60,4.75|1.02,0.87,0.88|0.94,0.98,1.04|', '1.000,半球,0.925|1.020↑,半球/一球,0.770↓|', '0.88,2,1.02|0.98↑,2/2.5,0.93↓|');
INSERT INTO `shijiebei` VALUES ('422236', '世界杯', '小组赛', '比利时', '俄罗斯', '0 - 0', '1-0', '主队', '88', '88分 1-0,', ' 2.10,3.30, 3.50|2.25,3.40,3.50|0.94,0.95,0.93|1.00,0.98,0.93|', '0.925,平手/半球,1.000|0.950↓,平手/半球,0.975↑|', '1.10,2.5,0.70|1.05↑,2/2.5,0.75↓|');
INSERT INTO `shijiebei` VALUES ('422237', '世界杯', '小组赛', '韩国', '阿尔及利亚', '0 - 3', '2-4', '', '-1', '', ' 2.10,3.30, 3.50|2.50,3.40,3.00|0.82,0.97,1.10|0.98,1.00,0.95|', '0.875,平手/半球,1.049|0.800↓,平手,1.149↑|', '1.20,2.5,0.65|1.02↑,2,0.88↓|');
INSERT INTO `shijiebei` VALUES ('422238', '世界杯', '小组赛', '韩国', '比利时', '0 - 0', '0-1', '', '-1', '', ' 5.50,3.50, 1.67|4.75,3.60,1.85|1.13,0.92,0.89|0.97,0.94,0.99|', '0.950,受半球/一球,0.975|0.730↓,受半球/一球,1.080↑|', '1.08,2.5,0.82|1.00↑,2.5,0.90↓|');
INSERT INTO `shijiebei` VALUES ('422239', '世界杯', '小组赛', '阿尔及利亚', '俄罗斯', '0 - 1', '1-1', '客队', '6', '6分 0-1,60分 1-1,', ' 6.50,3.80, 1.53|3.80,3.80,2.00|1.71,1.01,0.72|1.00,1.01,0.94|', '0.850,受一球,1.075|0.925↑,受半球,1.000↓|', '0.95,2/2.5,0.95|0.95↑,2/2.5,0.95↓|');
INSERT INTO `shijiebei` VALUES ('435089', '世界杯', '十六强', '巴西', '智利', '1 - 1', '1-1', '主队', '18', '18分 1-0,32分 1-1,', ' 1.70,4.00, 5.50|1.53,4.50,6.50|1.06,0.89,0.85|0.95,1.00,1.01|', '0.800,半球/一球,1.000|0.850↓,一球,1.075↑|', '0.83,2.5,0.98|1.02↓,2.5/3,0.88↑|');
INSERT INTO `shijiebei` VALUES ('435090', '世界杯', '十六强', '荷兰', '墨西哥', '0 - 0', '2-1', '客队', '48', '48分 0-1,88分 1-1,94分 2-1,', ' 2.10,3.50, 3.80|2.20,3.30,3.80|0.96,1.00,0.97|1.01,0.94,0.97|', '1.020,半球,0.770|0.875↓,平手/半球,1.049↑|', '0.83,2/2.5,0.98|0.98↓,2/2.5,0.93↑|');
INSERT INTO `shijiebei` VALUES ('437127', '世界杯', '十六强', '哥伦比亚', '乌拉圭', '1 - 0', '2-0', '主队', '28', '28分 1-0,50分 2-0,', ' 2.20,3.30, 3.30|2.15,3.40,3.75|1.02,0.94,0.83|1.00,0.97,0.94|', '0.899,平手/半球,1.024|0.875↓,平手/半球,1.049↑|', '0.95,2/2.5,0.95|1.05↑,2/2.5↑,0.75↓|');
INSERT INTO `shijiebei` VALUES ('437128', '世界杯', '十六强', '哥斯达黎加', '希腊', '0 - 0', '1-1', '主队', '52', '52分 1-0,91分 1-1,', ' 2.50,3.10, 2.90|2.80,3.10,2.90|0.93,0.96,0.92|1.04,0.96,0.92|', '0.925,平手,1.000|0.925↓,平手,1.000↑|', '1.05,2,0.85|0.82↑,1.5/2,1.08↓|');
INSERT INTO `shijiebei` VALUES ('437129', '世界杯', '十六强', '法国', '尼日利亚', '0 - 0', '2-0', '主队', '79', '79分 1-0,91分 2-0,', ' 1.50,4.00, 7.00|1.44,4.75,8.50|1.00,0.85,0.83|0.96,1.01,1.01|', '0.950,一球,0.950|0.975↑,一球/球半,0.950↓|', '0.95,2.5,0.95|1.02↓,2.5/3,0.88↑|');
INSERT INTO `shijiebei` VALUES ('437130', '世界杯', '十六强', '阿根廷', '瑞士', '0-0', '0 - 0', null, null, null, ' 1.44,4.33, 7.00|1.57,4.20,6.50|0.90,1.00,1.02|0.98,0.97,0.95|', '0.875,一球,0.975|1.024↓,一球,0.899↑|', '0.88,2.5,1.02|0.85↓,2.5↓,1.05↑|');
INSERT INTO `shijiebei` VALUES ('437131', '世界杯', '十六强', '德国', '阿尔及利亚', '0-0', '0 - 0', null, null, null, ' 1.30,5.00, 11.00|1.33,5.75,10.00|0.95,0.86,1.04|0.98,0.99,0.94|', '0.975,球半,0.950|1.049↑,球半,0.875↓|', '0.98,3,0.93|0.85↓,2.5/3↓,1.05↑|');
INSERT INTO `shijiebei` VALUES ('437132', '世界杯', '十六强', '比利时', '美国', '0-0', '0 - 0', null, null, null, ' 1.83,3.60, 4.20|2.00,3.40,4.33|0.87,1.02,1.00|0.96,0.97,1.03|', '0.875,半球,1.049|1.024↑,半球,0.899↓|', '1.00,2/2.5,0.90|0.98↑,2/2.5,0.93↓|');
INSERT INTO `shijiebei` VALUES ('437856', '世界杯', '八强', '巴西', '哥伦比亚', '1 - 0', '2-1', '主队', '7', '7分 1-0,68分 2-0,80分 2-1,', ' 1.80,3.80, 4.75|1.75,3.90,5.00|0.95,1.00,0.99|0.92,1.03,1.04|', '1.000,半球/一球,0.925|0.975↑,半球/一球,0.950↓|', '1.05,2.5,0.85|1.02↓,2/2.5,0.88↑|');
INSERT INTO `shijiebei` VALUES ('437859', '世界杯', '八强', '荷兰', '哥斯达黎加', '0-0', '0 - 0', null, null, null, ' 1.50,4.00, 7.00|1.53,4.20,7.50|0.95,0.92,0.94|0.97,0.97,1.01|', '0.899,一球,1.024|0.975↑,一球,0.950↓|', '0.98,2.5,0.93|0.88↓,2/2.5,1.02↑|');
INSERT INTO `shijiebei` VALUES ('440308', '世界杯', '八强', '法国', '德国', '0 - 1', '0-1', '客队', '12', '12分 0-1,', ' 3.00,3.25, 2.38|2.80,3.20,2.80|0.98,0.99,0.88|0.92,0.97,1.03|', '0.875,受平手/半球,1.049|0.950↑,平手,0.975↓|', '0.90,2/2.5,0.90|0.98↓,2/2.5,0.93↑|');
INSERT INTO `shijiebei` VALUES ('440312', '世界杯', '八强', '阿根廷', '比利时', '1 - 0', '1-0', '主队', '8', '8分 1-0,', ' 2.10,3.40, 3.60|2.00,3.40,4.33|0.97,0.99,0.89|0.93,0.99,1.07|', '1.100,半球,0.825|1.000,半球,0.925|', '0.90,2/2.5,1.00|0.88↓,2/2.5,1.02↑|');
INSERT INTO `shijiebei` VALUES ('442997', '世界杯', '半决赛', '巴西', '德国', '0 - 5', '1-7', '客队', '11', '11分 0-1,23分 0-2,24分 0-3,26分 0-4,29分 0-5,69分 0-6,79分 0-7,90分 1-7,', ' 2.50,3.25, 2.80|2.63,3.25,3.00|0.89,0.98,0.96|0.93,0.98,1.03|', '0.925,平手,0.925|0.800↓,平手,1.149↑|', '0.98,2/2.5,0.88|0.80↓,2,1.05↑|');
INSERT INTO `shijiebei` VALUES ('442999', '世界杯', '半决赛', '荷兰', '阿根廷', '0-0', '0 - 0', null, null, null, ' 2.40,3.20, 3.00|2.50,3.25,3.20|0.94,0.96,0.93|0.98,0.98,0.99|', '0.725,平手,1.250|1.100↑,平手/半球,0.825↓|', '1.17,2/2.5,0.75|0.88↓,2,1.02↑|');
INSERT INTO `shijiebei` VALUES ('445346', '世界杯', '决赛', '德国', '阿根廷', '0-0', '0 - 0', null, null, null, ' 2.30,3.25, 3.50|2.45,3.25,3.20|0.97,0.96,0.99|1.04,0.96,0.90|', '0.975,平手/半球,0.950|1.075↑,平手/半球,0.850↓|', '0.98,2,0.93|0.82↓,2,1.05|');
INSERT INTO `shijiebei` VALUES ('445371', '世界杯', '季军赛', '巴西', '荷兰', '0 - 2', '0-3', '客队', '3', '3分 0-1,16分 0-2,91分 0-3,', ' 2.38,3.40, 2.88|2.10,3.75,3.60|1.03,0.90,0.87|0.91,0.99,1.09|', '0.950,平手/半球,0.975|0.850↓,平手/半球,1.075↑|', '0.95,3,0.95|0.90↓,2.5/3,1.00↑|');
