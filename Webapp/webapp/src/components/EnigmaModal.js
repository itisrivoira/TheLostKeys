// Schermata Enigma

import { useContext, useState } from "react";
import { Modal, Row, Col } from "react-bootstrap";

import { Enigma } from './components';
import puzzles from '../assets/puzzles/puzzles.json';

import '../style/enigma.css';

const EnimaModal = () => {
	const { enigma, setEnigma } = useContext(Enigma);
	const [tentativi, setTentativi] = useState(3);
	const [disable1, setDisable1] = useState(false);
	const [disable2, setDisable2] = useState(false);
	const [disable3, setDisable3] = useState(false);
	const [disable4, setDisable4] = useState(false);

	const close = () => setEnigma(false);
	const right = () => alert('giusto :)');
	const wrongs = () => {
		alert('sbagliato :(');
		setTentativi( prev => prev - 1 );
	};

	const check = () => {
	};

	return(
		<Modal
			show={enigma}
			onHide={close}
			animation={false}
			fullscreen
		>
			<Modal.Body className="back">
				<Row>
					<Col>
						<p>
							N° Tentativi Rimasti: {tentativi}
						</p>
					</Col>
				</Row>
				<Row className="">
					<Col>
						Immagine
					</Col>
					<Col>
						Risposte
					</Col>
				</Row>
				<Row>
					<Col>
						<p>
							{puzzles.Chimica.text}
						</p>
					</Col>
					<Col>
						Bottoni
					</Col>
				</Row>
			</Modal.Body>
		</Modal>
	)
}

export default EnimaModal;