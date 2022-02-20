-- 
-- SQL script
--
CREATE TABLE IF NOT EXISTS `user` ( 
  `uuid` TEXT NOT NULL UNIQUE PRIMARY KEY, 
  `namename` TEXT NOT NULL,
  `password` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  `first_name` TEXT DEFAULT '',
  `middle_name` TEXT DEFAULT '',
  `last_name` TEXT DEFAULT ''
);

CREATE INDEX IF NOT EXISTS `user_idx_name` ON `user`(`namename`);


CREATE TABLE IF NOT EXISTS `group` (
  `uuid` TEXT NOT NULL UNIQUE PRIMARY KEY, 
  `name` TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS `group_idx_name` ON `group`(`name`);


CREATE TABLE IF NOT EXISTS `user_has_group` (
  `user_uuid` TEXT NOT NULL,
  `group_uuid` TEXT NOT NULL,
  PRIMARY KEY(`user_uuid`, `group_uuid`),
  FOREIGN KEY(`user_uuid`) REFERENCES `user`(`uuid`), 
  FOREIGN KEY(`group_uuid`) REFERENCES `group`(`uuid`)
);

CREATE INDEX IF NOT EXISTS `user_has_group_idx_user_uuid` ON `user_has_group`(`user_uuid`);
CREATE INDEX IF NOT EXISTS `user_has_group_idx_group_uuid` ON `user_has_group`(`group_uuid`);


CREATE TABLE IF NOT EXISTS `device` (
  `uuid` TEXT NOT NULL UNIQUE PRIMARY KEY,
  `serial_number` TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS `device_idx_serial_number` ON `device`(`serial_number`);


CREATE TABLE IF NOT EXISTS `device_data` (
  `device_uuid` TEXT NOT NULL,
  `telemetry_data` TEXT NOT NULL,
  `timestamp` INTEGER NOT NULL,
  FOREIGN KEY(`device_uuid`) REFERENCES `device`(`uuid`),
  PRIMARY KEY (`device_uuid`, `timestamp`)
);

CREATE INDEX IF NOT EXISTS `device_data_idx_device_uuid` ON `device_data`(`device_uuid`);
CREATE INDEX IF NOT EXISTS `device_data_idx_timestamp` ON `device_data`(`timestamp`);


CREATE TABLE IF NOT EXISTS `user_has_access` (
  `user_uuid` TEXT NOT NULL,
  `device_uuid` TEXT NOT NULL,
  PRIMARY KEY(`user_uuid`, `device_uuid`),
  FOREIGN KEY(`user_uuid`) REFERENCES `user`(`uuid`), 
  FOREIGN KEY(`device_uuid`) REFERENCES `device`(`uuid`)
);

CREATE INDEX IF NOT EXISTS `user_has_access_idx_user_uuid` ON `user_has_access`(`user_uuid`);
CREATE INDEX IF NOT EXISTS `user_has_access_idx_device_uuid` ON `user_has_access`(`device_uuid`);