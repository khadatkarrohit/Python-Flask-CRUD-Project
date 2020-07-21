# Python-Flask-CRUD-Project with MySQL Database

## MySQL connection information

###### Create table query:

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

###### MySQL Connection Parameter as per your local database setup: 

mydb = mysql.connector.connect(
    host="localhost",
    port="3309",
    user="root",
    passwd="root",
    database="crud_project"
 )
 
 ###### Install Below Python packages
 
 pip install flask,
 pip install mysql
 
 
 
