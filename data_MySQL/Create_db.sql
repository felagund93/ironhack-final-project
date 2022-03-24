-- create DB
CREATE DATABASE IF NOT EXISTS covid_19_final_project;

USE covid_19_final_project;

-- create tables (table with only primary key)
DROP TABLE IF EXISTS vaccination_grouped_country;
CREATE TABLE vaccination_grouped_country (
  `vaccination_id` INT UNIQUE NOT NULL, -- AS PRIMARY KEY
  `YearWeekISO` VARCHAR(20) DEFAULT NULL,
  `ReportingCountry` CHAR(2) DEFAULT NULL, -- char() , varchar(255)
  `FirstDose` INT DEFAULT NULL,
  `SecondDose` INT DEFAULT NULL,
  `Population` INT DEFAULT NULL,
  CONSTRAINT PRIMARY KEY (vaccination_id)  -- constraint keyword is optional but its a good practice
);

DROP TABLE IF EXISTS vaccination_eu_eea;
CREATE TABLE vaccination_eu_eea (
  `vaccination_id` INT UNIQUE NOT NULL, -- AS PRIMARY KEY
  `YearWeekISO` VARCHAR(20) DEFAULT NULL,
  `ReportingCountry` CHAR(2) DEFAULT NULL, -- char() , varchar(255)
  `FirstDose` INT DEFAULT NULL,
  `SecondDose` INT DEFAULT NULL,
  `DoseAdditional1` INT DEFAULT NULL,
  `UnknownDose` INT DEFAULT NULL,
  `Region` INT DEFAULT NULL,
  `TargetGroup` INT DEFAULT NULL,
  `Vaccine` INT DEFAULT NULL,
  `Population` INT DEFAULT NULL,
  CONSTRAINT PRIMARY KEY (vaccination_id)  -- constraint keyword is optional but its a good practice
);

DROP TABLE IF EXISTS new_daily_cases;
CREATE TABLE new_daily_cases (
  `MyUnknownColumn` INT UNIQUE NOT NULL, -- AS PRIMARY KEY
  `dateRep` VARCHAR(20) DEFAULT NULL,
  `day` INT DEFAULT NULL, -- char() , varchar(255)
  `month` INT DEFAULT NULL,
  `year` INT DEFAULT NULL,
  `cases` DOUBLE DEFAULT NULL,
  `deaths` DOUBLE DEFAULT NULL,
  `countriesAndTerritories` VARCHAR(20) DEFAULT NULL,
  `geold` CHAR(2) DEFAULT NULL,
  `countryterritoryCode` VARCHAR(5) DEFAULT NULL,
  `popData2020` INT DEFAULT NULL,
  `continentExp` VARCHAR(5) DEFAULT NULL,
  CONSTRAINT PRIMARY KEY (MyUnknownColumn)  -- constraint keyword is optional but its a good practice
);

-- The following code only works if some safety settings are disabled
LOAD DATA INFILE '/Users/albertgh/Documents/Ironhack/Data_Analysis_Course/Final Project/datasets_Tableau_clean/vaccination_grouped_country.csv' 
INTO TABLE covid_19_final_project.vaccination_grouped_country
FIELDS TERMINATED BY ',';

-- Data eventually imported with Wizard

SELECT * FROM vaccination_grouped_country;
SELECT * FROM new_daily_cases;
SELECT * FROM vaccination_eu_eea;

-- Convert date columns to DATETIME

ALTER TABLE vaccination_grouped_country MODIFY YearWeekISO DATETIME;
ALTER TABLE vaccination_eu_eea MODIFY YearWeekISO DATETIME;
ALTER TABLE new_daily_cases MODIFY dateRep DATETIME;

-- JOIN of tables
SELECT * FROM vaccination_eu_eea AS vax
LEFT JOIN new_daily_cases AS cases ON vax.YearWeekISO=cases.dateRep AND vax.ReportingCountry=cases.geoId;