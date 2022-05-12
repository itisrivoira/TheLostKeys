/*
	UI Enigma
	Un solo componente per visualizzare tutti gli enigmi
*/

import { useContext, useEffect, useState } from "react";
import { Modal, Row, Col, Button, Image } from "react-bootstrap";

import { EnigmaCtx, RunCtx, RoomNameCtx, ScoreCtx, DoneCtx } from './components';
import { Documento } from "../assets/img/img";
import puzzles from '../assets/puzzles/puzzles.js';

const EnimaModal = () => {
	const { enigma, setEnigma } = useContext(EnigmaCtx);		// Se la UI è attiva o meno
	const { room } = useContext(RoomNameCtx);			// Nome della stanza in cui sono (=nome enigma)
	const { setRun } = useContext(RunCtx);			// per stoppare il gioco
	const { setScore } = useContext(ScoreCtx);		// per modificare il punteggio totale
	const { setDone } = useContext(DoneCtx);					// Per aggiungere l'enigma come fatto
	const [tentativi, setTentativi] = useState(3);
	const [indizio, setIndizio] = useState(false);	// se il suggerimento è stato attivato
	const [text, setText] = useState(true);			// se mostrare il testo dell'enigma o il suggerimento

	const puzzle = puzzles[room];			// ottengo l'Enigma come Object Literal
	const { A, B, C, D } = puzzle;		// Estraggo le domande per poterle girare più facilmente (map())

	const [points, setPoints] = useState(puzzle.punti[tentativi]);			// punti locali dell'enigma
	// i punti nel JSON sono in ordine descrescente perchè li cambio in base ai tentativi (40 -> 20 -> 10 -> 0)

	// Chiudo la UI Enigma
	const close = () => {
		setEnigma(false);			// Chiudo la UI
		setRun(true);				// Tolgo la pausa dal gioco
	};

	// Risposta giusta
	const right = () => {
		alert('giusto :)');
		setDone(prev => [...prev, room]);	// Aggiungo il nome dell'enigma fra quelli già fatt
		setTentativi(3);			// Resetto il numero di Tentativi
		setIndizio(false);		// Resetto l'indizio
		setText(true);				// Resetto il testo dell'enigma
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
			setPoints(puzzle.punti[tentativi]);

		// quando l'utente esaurisce i tentativi gli rivelo la risposta corretta e chiude
		if (tentativi === 0) {
			alert('La risposta giusta era la: ' + puzzle.right);
			setTentativi(0);
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
							src={!puzzle.img ? Documento: puzzle.img}
							width={350}
							height={350}
						/>
					</Col>
					<Col xxl={8} className='d-flex align-items-center'>
						<Row>
							{
							// Genero per ogni domanda un bottone con funzione check e come parametro la lettera della risposta
							Object.keys({A,B,C,D}).map( key => (
								<BtnAnswer
									indice={key}
									text={puzzle[key]}
									click={() => check(key)}
								/>
							))}
						</Row>
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

// Pulsante per una riposta
const BtnAnswer = ({indice, text, click}) => (
	<Col className="mx-3">
		<Button
			onClick={click}
			variant="success"
			className="txt-pixel fs-4 my-2 p-3"
			key={indice}
		>
			{indice}: {text}
		</Button>
	</Col>
)


export default EnimaModal;