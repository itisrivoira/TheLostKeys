
CREATE DATABASE IF NOT EXISTS TheLostKeys;
USE TheLostKeys;

CREATE TABLE IF NOT EXISTS utente(
	Nickname varchar(25) NOT NULL,
	Password varchar(32) NOT NULL,
	Email varchar(70) NOT NULL,
	PRIMARY KEY (Nickname)
	);

CREATE TABLE IF NOT EXISTS partita(
	Id INT  NOT NULL AUTO_INCREMENT,
	Tempo TIME NOT NULL,
	PunteggioMassimo INT NOT NULL,
	Nick varchar(25),
	PRIMARY KEY (Id),
	FOREIGN KEY (Nick) REFERENCES utente(Nickname)
	);

