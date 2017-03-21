# imp sql querry
CREATE TABLE user (
  use_id int(6) NOT NULL AUTO_INCREMENT,
  use_name varchar(50) NOT NULL,
  use_email varchar(50) NOT NULL,
  use_mobile int(16) NOT NULL,
  use_Address varchar(100) NOT NULL,
  use_isused int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (use_id)
)


CREATE TABLE Events (
  eve_id int(6) NOT NULL AUTO_INCREMENT,
  eve_name varchar(50) NOT NULL,
  eve_location varchar(50) NOT NULL,
  eve_date varchar(30) NOT NULL,
  eve_entry_fee int(9) NULL DEFAULT '0',
  eve_discription varchar(900) NOT NULL,
  eve_isused int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (eve_id)
)

Alter table user add column use_pwd varchar(100) after use_Address;
Alter table user add column use_login_id varchar(10) after use_name;
