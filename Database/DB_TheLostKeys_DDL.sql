
CREATE DATABASE IF NOT EXISTS TheLostKey;
USE TheLostKey;

CREATE TABLE IF NOT EXISTS utente(
	Nickname varchar(25) NOT NULL,
	Password varchar(32) NOT NULL,
	Email varchar(70) NOT NULL,
	PRIMARY KEY (Nickname)
	);

CREATE TABLE IF NOT EXISTS partita(
	Id CHAR(16) NOT NULL,
	Data DATETIME,
	Tempo TIME NOT NULL,
	Punteggio INT NOT NULL,
	Nick varchar(25),
	PRIMARY KEY (Id),
	FOREIGN KEY (Nick) REFERENCES utente(Nickname)
	);

