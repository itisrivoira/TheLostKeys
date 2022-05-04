// Schermata delle Istruzioni del Gioco

import { useContext } from "react";
import { Col, Modal, Row } from "react-bootstrap";

import { Comandi } from './components';

const Commands = () => {
	const { comandi, setComandi } = useContext(Comandi);		// Indica se il modal dei comandi è attivo oppure no

	const close = () => setComandi(false);		// chiudo il modal

	return(
		<Modal
			show={comandi}		// flag per l'attivazione del modal
			onHide={close}		// callback richiamata alla chiusura della modal
			centered				// centrato a schermo
		>
			<Modal.Header closeButton>
				<Modal.Title>
					Instruzioni
				</Modal.Title>
			</Modal.Header>
			<Modal.Body>
				{/*Qui giro il vettore ListaComandi e ritorno una riga per ogni comando*/}
				{listaComandi.map( value => (<>
					<Row key={value.key}>
						<Col xxl={4}>
							<p>
								{value.key}
							</p>
						</Col>
						<Col xxl={8}>
							<p>
								{value.funzione}
							</p>
						</Col>
					</Row>
					<hr/>
				</>))}
			</Modal.Body>
		</Modal>
	)
}

// Tutti i comandi del Gioco
const listaComandi = [
	{
		key: 'W',
		funzione: "Muovi il Giocatore verso l'alto"
	},
	{
		key: 'A',
		funzione: "Muovi il Giocatore verso destra"
	},
	{
		key: 'S',
		funzione: "Muovi il Giocatore verso il basso"
	},
	{
		key: 'D',
		funzione: "Muovi il Giocatore verso sinistra"
	},
	{
		key: 'E',
		funzione: "Metti in Pausa il Gioco e apri le Opzioni"
	},
	{
		key: 'Q',
		funzione: "Interagisci in giro per la mappa"
	},
	{
		key: 'Enter',
		funzione: "Continua i dialoghi"
	}
];

export default Commands;