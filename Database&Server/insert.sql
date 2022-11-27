USE TheLostKeys;

INSERT INTO `utente` (`Nickname`, `Password`, `Email`) VALUES ('admin', 'admin', NULL), ('admin1', 'admin1', NULL), ('admin2', 'admin2', NULL);
INSERT INTO `partita` (`Id`, `Punteggio`, `Personaggio`, `Nick`) VALUES (NULL, '100', 'Aleks', 'admin') ,  (NULL, '200', 'Beppe', 'admin1'),  (NULL, '1000', 'Senex', 'admin2'); 