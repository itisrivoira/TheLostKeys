// Schermata Enigma

import { useContext } from "react";
import { Modal, Button, Row, Col } from "react-bootstrap";

import { Enigma } from './components';

import '../style/enigma.css';

const EnimaModal = () => {
	const { enigma, setEnigma } = useContext(Enigma);

	const giusto = () => {
		alert('giusto :)');
		setEnigma(false);
	};

	const sbagliato = () => {
		alert('sbagliato :(');
		setEnigma(false);
	}

	return(
		<Modal
			show={enigma}
			onHide={() => setEnigma(false)}
			animation={false}
			keyboard
			onEscapeKeyDown={e => e.preventDefault()}
			fullscreen

		>
			<Modal.Body className="back">
				<Row>
					<Col>
						<p className="fs-3 txt-pixel">
							Ecco qui l'enigma <br/>
							Risolvi lo schema per il passaggio di stato: da una sostanza solida
							come il ghiaccio qual è il giusto ordine per passare allo stato
							gassoso, e poi a quello liquido come l’acqua e poi di nuovo allo
							stato solido
						</p>
					</Col>
				</Row>
				<hr />
				<Button variant="success" onClick={sbagliato} className='my-2'>
					<p className="txt-pixel fs-4">
						Liquefazione - Sublimazione - Solidificazione
					</p>
				</Button>
				<br/>
				<Button variant="success" onClick={sbagliato} className='my-2'>
					<p className="txt-pixel fs-4">
						Non si può determinare
					</p>
				</Button>
				<br/>
				<Button variant="success" onClick={giusto} className='my-2'>
					<p className="txt-pixel fs-4">
						Sublimazione - Liquefazione - Solidificazione
					</p>

				</Button>
				<br/>
				<Button variant="success" onClick={sbagliato} className='my-2'>
					<p className="txt-pixel fs-4">
							Sublimazione - Solidificazion - Liquefazione
					</p>

				</Button>
				<br/>
				<hr />
				<Button variant="danger" onClick={() => setEnigma(false)}>
					<p className="txt-pixel fs-3">
						Rinuncia
					</p>
				</Button>
				<Button variant="warning" className="mx-3">
					<p className="txt-pixel fs-3">
						Suggerimento
					</p>
				</Button>
			</Modal.Body>
		</Modal>
	)
}

export default EnimaModal;