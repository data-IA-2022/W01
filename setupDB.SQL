set global local_infile=true;

CREATE TABLE `name_basics` (
  `nconst` VARCHAR(10),
  `primaryName` text,
  `birthYear` int DEFAULT NULL,
  `deathYear` int DEFAULT NULL,
  `primaryProfession` text,
  `knownForTitles` text
);
delete from name_basics;
load data local infile 'name.basics.tsv' into table name_basics;

CREATE TABLE `title_akas` (
  `titleId` VARCHAR(10),
  `ordering` int DEFAULT NULL,
  `title` text,
  `region` text,
  `language` text,
  `types` text,
  `attributes` text,
  `isOriginalTitle` bigint DEFAULT NULL
);
delete from title_akas;
load data local infile 'title.akas.tsv' into table title_akas;

CREATE TABLE `title_basics` (
  `tconst` VARCHAR(10),
  `titleType` text,
  `primaryTitle` text,
  `originalTitle` text,
  `isAdult` int DEFAULT NULL,
  `startYear` int DEFAULT NULL,
  `endYear` INT,
  `runtimeMinutes` INT,
  `genres` text
);
delete from title_basics;
load data local infile 'title.basics.tsv' into table title_basics;

CREATE TABLE `title_crew` (
  `tconst` varchar(10) NOT NULL,
  `directors` text,
  `writers` text
);
delete from title_crew;
load data local infile 'title.crew.tsv' into table title_crew;

CREATE TABLE `title_episode` (
  `tconst` varchar(10) DEFAULT NULL,
  `parentTconst` varchar(10) DEFAULT NULL,
  `seasonNumber` int DEFAULT NULL,
  `episodeNumber` int DEFAULT NULL
);
delete from title_episode;
load data local infile 'title.episode.tsv' into table title_episode;

CREATE TABLE `title_principals` (
  `tconst` varchar(10) DEFAULT NULL,
  `ordering` int DEFAULT NULL,
  `nconst` varchar(10) DEFAULT NULL,
  `category` text,
  `job` text,
  `characters` text,
  UNIQUE KEY `title_principals_UN` (`tconst`,`ordering`)
);
delete from title_principals;
load data local infile 'title.principals.tsv' into table title_principals;

CREATE TABLE `title_ratings` (
  `tconst` varchar(10) NOT NULL,
  `averageRating` decimal(5,1) DEFAULT NULL,
  `numVotes` int DEFAULT NULL,
  PRIMARY KEY (`tconst`)
);
delete from title_ratings;
load data local infile 'title.ratings.tsv' into table title_ratings;




CREATE TABLE `name_basics` (
  `index` bigint DEFAULT NULL,
  `nconst` text,
  `primaryName` text,
  `birthYear` text,
  `deathYear` text,
  `primaryProfession` text,
  `knownForTitles` text,
  KEY `ix_name_basics_index` (`index`)
);

ALTER TABLE name_basics MODIFY COLUMN nconst VARCHAR (10) NOT NULL;
ALTER TABLE name_basics DROP `index`;
alter table name_basics add primary key (nconst);

CREATE INDEX idx1 ON name_basics (`nconst`);

ALTER TABLE title_crew MODIFY COLUMN tconst VARCHAR (10) NOT NULL;
ALTER TABLE `title_crew`
ADD CONSTRAINT `fk_title_crew_title_basics`
  FOREIGN KEY (`tconst`)
  REFERENCES `test`.`title_basics` (`tconst`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;





ALTER TABLE name_basics ADD CONSTRAINT name_basics_PK PRIMARY KEY (nconst);
DELETE FROM name_basics WHERE nconst="nconst";
CREATE FULLTEXT INDEX name_basics_primaryName_IDX ON name_basics (primaryName);
CREATE INDEX name_basics_birthYear_IDX USING BTREE ON name_basics (birthYear);

ALTER TABLE title_basics ADD CONSTRAINT title_basics_PK PRIMARY KEY (tconst);
DELETE FROM title_basics WHERE tconst="tconst";
CREATE FULLTEXT INDEX title_basics_primaryTitle_IDX ON title_basics (primaryTitle,originalTitle);
CREATE INDEX title_basics_startYear_IDX USING BTREE ON title_basics (startYear);

delete from title_akas where titleId="titleId";
ALTER TABLE title_akas ADD CONSTRAINT title_akas_PK PRIMARY KEY (titleId,`ordering`);
SELECT * from title_akas A LEFT JOIN title_basics T ON (A.titleId=T.tconst) WHERE T.tconst IS NULL;

--ALTER TABLE title_akas ADD CONSTRAINT title_akas_FK FOREIGN KEY (titleId) REFERENCES title_basics(tconst);

ALTER TABLE title_episode ADD CONSTRAINT title_episode_PK PRIMARY KEY (tconst);
ALTER TABLE title_episode ADD CONSTRAINT title_episode_FK FOREIGN KEY (tconst) REFERENCES title_basics(tconst);
--ALTER TABLE title_episode ADD CONSTRAINT title_episode_FK_1 FOREIGN KEY (parentTconst) REFERENCES title_basics(tconst);

ALTER TABLE title_crew ADD CONSTRAINT title_crew_PK PRIMARY KEY (tconst);
ALTER TABLE title_crew ADD CONSTRAINT title_crew_FK FOREIGN KEY (tconst) REFERENCES title_basics(tconst);

SELECT * from title_principals T LEFT JOIN name_basics N ON (T.nconst=T.nconst) WHERE N.nconst IS NULL limit 10;
--ALTER TABLE title_principals ADD CONSTRAINT title_principals_FK FOREIGN KEY (nconst) REFERENCES name_basics(nconst);
ALTER TABLE title_principals ADD CONSTRAINT title_principals_FK_1 FOREIGN KEY (tconst) REFERENCES title_basics(tconst);

ALTER TABLE title_principals ADD CONSTRAINT title_principals_FK FOREIGN KEY (tconst) REFERENCES title_basics(tconst);
ALTER TABLE title_principals ADD CONSTRAINT title_principals_FK_1 FOREIGN KEY (nconst) REFERENCES name_basics(nconst);
