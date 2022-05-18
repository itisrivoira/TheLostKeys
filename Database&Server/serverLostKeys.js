// Server Node js The Lost Keys

const express = require('express');
const mysql = require('mysql');
const cors = require('cors');//necessario per i permessi
const app = express();
app.use(cors({
	origin: '*'
}));


app.use(express.urlencoded({extended: true}));//necessario per il funzionamento del post

//1 endpoint per l'invio al client dell'id, punteggio e nome del giocatore
app.get('/rank', (req, res) => {
	const array = [];

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'TheLostKeys'
	});

	const query = "SELECT * FROM partita ORDER BY punteggioMassimo DESC"; // la query viene fatta in background quindi siamo obbligati a mandare il json nella funzione

	con.query(query, (err, result) => {
		if (err) {
			console.log(err.message);
			throw err;
		}

		result.map( value => {
			array.push({
				id: value.Id,
				points: value.PunteggioMassimo,
				player: value.Nick
			})
		});

		res.send(JSON.stringify(array));
	});
});

//2 endpoint per l'invio al server del punteggio Massimo
app.post('/upload', (req, res) => {
	const nick = req.body.nick;
	const score = req.body.score;
	let highscore;

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'thelostkeys'
	});

	const	check = `SELECT PunteggioMassimo FROM partita WHERE Nick = '${nick}'`;
	con.query(check, (err, result) => {
		if (err) {
			console.log(err.message);
			throw err;
		}

		let highscore = result[0].PunteggioMassimo;
		if (score > highscore) {
			const load = `UPDATE partita SET PunteggioMassimo = '${score}' WHERE Nick = '${nick}'`;
			con.query(load, (err, result) => {
				if (err) {
					console.log(err.message);
					throw err;
				}
			});
		}
	})




})


app.post('/controllo', (req, res) => {
	const arrayUtenti = [];
	const nick = req.body.nick;
	const score = req.body.score;

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'thelostkeys'
	});

	const elencoUtenti = "SELECT Nickname FROM utente"; // la query ritorna tutti i nomi degli utenti nel DB

	con.query(elencoUtenti, (err, result) => {
		if (err) {
			console.log(err.message);
			throw err;
		}


		result.map( value => {
			arrayUtenti.push({
				utente:value.Nickname//array con tutti i nomi degli utenti
			})
		});

		res.send(JSON.stringify(arrayUtenti));

		arrayUtenti.forEach(el => {
			if(el.utente != $utente){

				const inserisciNuovoUtente =  `INSERT INTO utente (Nickname) VALUES ('${nick}')`;//inserisco l'utente
				const inserisciNuovaPartita =  `INSERT INTO partita (Tempo,PunteggioMassimo,Nick) VALUES ('${score}','${nick}')`; //inserisco la partita relativa
				con.query(inserisciNuovoUtente, (err, result) => {
					if (err) {
						console.log(err.message);
						throw err;
					}

				});

				con.query(inserisciNuovaPartita, (err, result) => {
					if (err) {
						console.log(err.message);
						throw err;
					}

				});

				
			}



		});
	});
})


app.listen(3000);
