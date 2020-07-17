# Python-Flask-CRUD-Project

MySQL table query for crud operation. 

CREATE TABLE employee_details (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `designation` VARCHAR(45) NULL,
  `total_experiance` INT(11) NULL,
  `created_on` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `email` VARCHAR(200) NOT NULL,
  `active` TINYINT(1) NULL DEFAULT '1',
  PRIMARY KEY (`id`));
