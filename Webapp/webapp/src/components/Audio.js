// Controller volume audio di Gioco
// Permette di abbassare/diminuire la musica del gioco

import { useEffect, useState } from "react";
import { Row, Col, Button, ProgressBar } from "react-bootstrap";
import { BsPlusLg, BsDashLg } from "react-icons/bs";		// queste sono le icone della libreria React-Icons

// Title: Titolo della barra
// Volume: Livello del volume
// Changer: Funzione di Callback per modificare lo Stato Globale

const Audio = ({title, volume, changer}) => {
	const [dash, setDash] = useState(false);		// flag di disabilitazione tasto +
	const [plus, setPlus] = useState(false);		// flag di disabilitazione tasto -

	const increase = () => {changer(prev => prev + 0.1)}		// aumento il volume
	const reduce = () => {changer(prev => prev - 0.1)}			// diminuisce il volume

	// Questa funzione si esegue ogni volta che cambia il volume
	useEffect( () => {
		if (volume <= 0.1) {
			setDash(true);		// Disabilito il tasto +
		} else if (volume >= 0.9) {
			setPlus(true);		// Disabilito il tasto -
		} else {
			setDash(false);	// Li attivo entrambi
			setPlus(false);
		}
	}, [volume]);

	return(
		<>
			<Row className="text-center">
				<Col>
					<p className="txt-pixel fs-3">
						{title}
					</p>
				</Col>
			</Row>
			<Row className="mb-3 text-center d-flex justify-content-center">
				<Row className="w-75 mb-3">
					<Col>
						<ProgressBar striped variant="dark" now={volume} min={0} max={1} />
					</Col>
				</Row>
				<Row className="w-75">
					<Col>
						<Button variant="dark" onClick={reduce} disabled={dash} /*Disable se è true disabilita il button */ >
							<BsDashLg size={20} />
						</Button>
					</Col>
					<Col>
						<Button variant="dark" onClick={increase} disabled={plus}>
							<BsPlusLg size={20} />
						</Button>
					</Col>
				</Row>
			</Row>
		</>
	)
}

export default Audio;