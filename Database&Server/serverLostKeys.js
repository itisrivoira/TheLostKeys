// Server Node js The Lost Keys
const express = require('express');
const mysql = require('mysql');
const cors = require('cors');//necessario per i permessi
const app = express();
app.use(cors({
	origin: '*'
}));


app.use(express.urlencoded({extended: true}));//necessario per il funzionamento del post
app.use(express.json());//necessario per recuperare il json

//1 endpoint per l'invio della classifica alla pagina rank.js
app.get('/rank', (req, res) => {
	const array = [];

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'TheLostKeys'
	});

	const query = "SELECT * FROM partita ORDER BY Punteggio DESC";

	con.query(query, (err, result) => {
		if (err) {
			console.log(err.message);
			throw err;
		}

		result.map( value => {
			array.push({
				id: value.Id,
				points: value.Punteggio,
				player: value.Nick,
				pg: value.Personaggio
			})
		});

		res.send(JSON.stringify(array));
	});
});

//2 endpoint per il caricamento della partita
app.post('/upload', (req, res) => {
	const nick = req.body.nick;
	const score = req.body.score;
	const personaggio = req.body.pg;
	const arrayUtenti = [];

	console.log('nick: ' + nick + ' score: ' + score);

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'TheLostKeys'
	});
	const elencoUtenti = "SELECT Nickname FROM utente";
	con.query(elencoUtenti, (err, result) => {
		if (err) {
			console.log(err.message);
			throw err;
		}

		result.map( value => {
			arrayUtenti.push({
				utente:value.Nickname
			})
		});

		if (!arrayUtenti.includes(nick)) {
			const inserisciNuovoUtente =  `INSERT INTO utente (Nickname) VALUES ('${nick}')`;
				const inserisciNuovaPartita =  `INSERT INTO partita (Punteggio, Nick, Personaggio) VALUES ('${score}','${nick}', '${personaggio}')`;
				con.query(inserisciNuovoUtente, (err, result) => {
					if (err) {
						console.log(err.message);
						throw err;
					}
				});
				con.query(inserisciNuovaPartita, (err, result) => {
					if (err){
						console.log(err.message);
						throw err;
					}
				});
		} else {
			const	check = `SELECT Punteggio FROM partita WHERE Nick = '${nick}'`;
				con.query(check, (err, result) => {
					if (err) {
						console.log(err.message);
						throw err;
					}
					let highscore = result[0].Punteggio;
					if (score > highscore){
						const load = `UPDATE partita SET Punteggio = '${score}' WHERE Nick = '${nick}'`;
						con.query(load, (err, result) => {
							if(err) {
								console.log(err.message);
								throw err;
							}
						});
					}
				})

		}


	});
})

app.listen(4000);