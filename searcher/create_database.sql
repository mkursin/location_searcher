create database Locations CHARACTER SET utf8 COLLATE utf8_general_ci;
create table geoip_table
(
ID int not null auto_increment primary key,
IP int not null,
Latitude double,
Longitude double,
City varchar(50),
Region varchar(50),
Bistrict varchar(50),
Datetime datetime) CHARACTER SET utf8 COLLATE utf8_general_ci;
