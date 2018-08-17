CREATE TABLE IF NOT EXISTS `user_info` (
  `fname` varchar(64) NOT NULL COMMENT 'user name',
  `fwork_id` int NOT NULL COMMENT 'work id',
  `fdept_id` int NOT NULL COMMENT 'department id',
  `flevel_id` int NOT NULL COMMENT 'level id',
  `fpassword` varchar(64) NOT NULL COMMENT 'password',
  `fadd_time` timestamp DEFAULT NULL COMMENT 'add time',
  `fupdate_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'update time'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COMMENT='user info';

CREATE TABLE IF NOT EXISTS `auth_table` (
  `ftable_name` varchar(64) NOT NULL COMMENT 'table name',
  `flevel_id` int NOT NULL COMMENT 'level id',
  `fadd_time` timestamp DEFAULT NULL COMMENT 'add time',
  `fupdate_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'update time'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COMMENT='auth table';

CREATE TABLE IF NOT EXISTS `level_info` (
  `flevel_id` int NOT NULL COMMENT 'level id',
  `flevel_name` varchar(64) NOT NULL COMMENT 'level name',
  `fadd_time` timestamp DEFAULT NULL COMMENT 'add time',
  `fupdate_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'update time'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COMMENT='level info';

