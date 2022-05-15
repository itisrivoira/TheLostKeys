// Server Node js The Lost Keys

const express = require('express');
const mysql = require('mysql');
const cors = require('cors');//necessario per i permessi
const res = require('express/lib/response');
const app = express();
app.use(cors({
	origin: '*'
}));


app.use(express.urlencoded({extended: true}));//necessario per il funzionamento del post

/*
app.get('/login', (req, res) => {
	const arrayUser = [];

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'thelostkeys'
	});

	const query = "SELECT * FROM utente"; 

	con.query(query, (err, result) => {
		if (err) {
			console.log(err.message);
			throw err;
		}

		result.map( value => {
			arrayUser.push({
				name: value.Nickname,
				email: value.Email,
			
			})
		});

		res.send(JSON.stringify(arrayUser));
	});
})*/

//1 endpoint per l'invio al client dell'id, punteggio e nome del giocatore
app.get('/rank', (req, res) => {
	const array = [];

	const con = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '',
		database: 'thelostkeys'
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
})

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


app.listen(3000);

