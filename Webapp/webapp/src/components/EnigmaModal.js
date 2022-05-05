/*
	UI Enigma
	Un solo componente per visualizzare tutti gli enigmi
*/

import { useContext, useEffect, useState } from "react";
import { Modal, Row, Col, Button, Image } from "react-bootstrap";

import { Enigma, Run, RoomName, Score } from './components';
import { narratore } from "../assets/img/img";
import puzzles from '../assets/puzzles/puzzles.json';

import '../style/enigma.css';

const EnimaModal = () => {
	const { enigma, setEnigma } = useContext(Enigma);		// Se la UI è attiva o meno
	const { room } = useContext(RoomName);			// Nome della stanza in cui sono (=nome enigma)
	const { setRun } = useContext(Run);			// per stoppare il gioco
	const { setScore } = useContext(Score);		// per modificare il punteggio totale
	const [tentativi, setTentativi] = useState(3);
	const [indizio, setIndizio] = useState(false);	// se il suggerimento è stato attivato
	const [text, setText] = useState(true);			// se mostrare il testo dell'enigma o il suggerimento

	const puzzle = puzzles[room];			// ottengo l'Enigma come Object Literal
	const { A, B, C, D } = puzzle;		// Estraggo le domande per poterle girare più facilmente (map())

	const [points, setPoints] = useState(puzzle.punti);			// punti locali dell'enigma

	// Chiudo la UI Enigma
	const close = () => {
		setEnigma(false);
		setRun(true);
	};

	// Risposta giusta
	const right = () => {
		alert('giusto :)');
		console.log(indizio);
		setScore(prev => indizio ? prev + points/2 : prev + points);
		close();
	};

	// Risposte sbagliate
	const wrongs = () => {
		alert('sbagliato :(');
		setTentativi( prev => prev - 1 );
	};

	// Controllo la risposta
	const check = key => {
		if (key == puzzle.right)
			right();
		else
			wrongs();
	};

	// Attivo l'indizio
	const activeIndizio = () => {
		setIndizio(true);
		setText(false);
	};

	// Cambio il testo dell'Enigma con il suggerimento e viceversa
	const changeText = () => setText(prev => !prev);

	useEffect( () => {
		if (tentativi < 3)	// quando l'utente sbaglia diminuisco i punti secondo le penalità dell'Enigma
			setPoints(puzzle.penalita[tentativi]);

		// quando l'utente esaurisce i tentativi gli rivelo la risposta corretta e chiude
		if (tentativi === 0) {
			alert('La risposta giusta era la: ' + puzzle.right);
			close();
		}
	}, [tentativi]);

	return(
		<Modal
			show={enigma}
			onHide={close}
			animation={false}
			fullscreen
		>
			<Modal.Body className="back">
				<Row className="my-3">
					<Col>
						<p className="text-center text-white txt-pixel fs-2" >
							N° Tentativi Rimasti: {tentativi}
						</p>
					</Col>
				</Row>
				<Row className="my-3">
					<Col xxl={4} className='d-flex justify-content-center'>
						<Image
							src={narratore}
							width={250}
							height={250}
						/>
					</Col>
					<Col xxl={8}>
						{
						// Genero per ogni domanda un bottone con funzione check e come parametro la lettera della risposta
						Object.keys({A,B,C,D}).map( key => (
							<Button
								onClick={() => check(key)}
								variant="success"
								className="txt-pixel fs-4 my-2 p-2"
								key={key}
							>
								{key}: {puzzle[key]}
							</Button>
						))}
					</Col>
				</Row>
				<Row className="my-2 mt-4 p-5 bg-secondary rounded-pill">
					<Col>
						<p className="text-white txt-pixel fs-3">
						{ text ?
							'Testo Enigma: ' + puzzle.text
						:
							'Suggerimento: ' + puzzle.indizio
						}
						</p>
					</Col>
				</Row>
				<Row className="my-2 p-3 text-center">
					<Col>
						<Button
							variant="warning"
							size="lg"
							onClick={activeIndizio}
							disabled={indizio}
							className="txt-pixel text-white mx-4 fs-4 p-3"
						>
							Suggerimento
						</Button>
						<Button
							variant="danger"
							size="lg"
							className="txt-pixel text-white mx-4 fs-4 p-3"
							onClick={close}
						>
							Rinuncia
						</Button>
						{
							// se indizio diventa true viene mostrato questo Button
							indizio &&
							<Button
								onClick={changeText}
								size="lg"
								className="txt-pixel text-white mx-4 fs-4 p-3"
							>
								Cambia
							</Button>
						}
					</Col>
				</Row>
			</Modal.Body>
		</Modal>
	)
}

export default EnimaModal;