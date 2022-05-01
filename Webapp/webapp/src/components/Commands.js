// Schermata delle Istruzioni del Gioco

import { useContext } from "react";
import { Col, Modal, Row } from "react-bootstrap";

import { Comandi } from './components';

const Commands = () => {
	const { comandi, setComandi } = useContext(Comandi);

	const close = () => setComandi(false);

	return(
		<Modal
			show={comandi}
			onHide={close}
			centered
		>
			<Modal.Header closeButton>
				<Modal.Title>
					Instruzioni
				</Modal.Title>
			</Modal.Header>
			<Modal.Body>
				{listaComandi.map( (value, index) => (<>
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
	}
];

export default Commands;