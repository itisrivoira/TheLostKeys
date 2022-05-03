// Schermata Enigma

import { useContext, useEffect, useState } from "react";
import { Modal, Row, Col, Button } from "react-bootstrap";

import { Enigma, Run } from './components';
import puzzles from '../assets/puzzles/puzzles.json';

import '../style/enigma.css';

const EnimaModal = () => {
	const { enigma, setEnigma } = useContext(Enigma);
	const { setRun } = useContext(Run)
	const [tentativi, setTentativi] = useState(3);
	const [indizio, setIndizio] = useState(false);		// se il suggerimento è stato attivato
	const [text, setText] = useState(true);		// se mostrare il testo dell'enigma o il suggerimento

	const puzzle = puzzles['Chimica'];
	const { A, B, C, D } = puzzle;

	const close = () => {
		setEnigma(false);
		setRun(true);
	};

	const right = () => {
		alert('giusto :)');
		close();
	};

	const wrongs = () => {
		alert('sbagliato :(');
		setTentativi( prev => prev - 1 );
	};

	const check = key => {
		if (key == puzzle.right) {
			right();
		} else {
			wrongs();
		}
	};

	const activeIndizio = () => {
		setIndizio(true);
		setText(false);
	};

	const changeText = () => setText(prev => !prev);

	useEffect( () => {
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
					<Col xxl={4}>
						Immagine
					</Col>
					<Col xxl={8}>
						{ Object.keys({A,B,C,D}).map( key => (
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
				<Row className="my-2 p-5">
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