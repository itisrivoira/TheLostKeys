// Componente Dialogo

import { Modal } from "react-bootstrap";
import { useState, useContext, useEffect } from "react";

import { DialogOpen, DialogText, Run } from "./components";
import { useEventListener } from '../utils/utils';
import primo from '../assets/dialogs/primo.json';		// file di dialogo di prova

const Dialog = () => {
	const [ n, setN ] = useState(0);		// indica il numero della parte di dialogo da visualizzare
	const { dialog, setDialog } = useContext(DialogOpen);		// per aprire il modal del Dialogo
	const { run, setRun } = useContext(Run);		// per stoppare il gioco

	// chiudere il modal del dialogo
	const handleClose = () => {
		setDialog(false);
		if ( !run ) setRun(true);
		setN(0);
	};

	useEffect( () => {
		// verifico di essere arrivato alla fine
		if (n == primo.length) {
			handleClose();
		}
	}, [n]);

	// Quando premo Invio il testo deve andare avanti
	const next = e => {
		if (e.key === 'Enter')
			setN(prev => prev + 1);
	};

	useEventListener('keydown', next);

	return(
		<>
			<Modal
				show={dialog}
				onHide={handleClose}
				animation={false}		// Modal senza animazione
				size='lg'
				dialogClassName="position-absolute bottom-0 start-50 translate-middle-x customw"
				backdrop="static"
			>
				<Modal.Body
					className="bg-secondary"
				>
					{
						// Giro il JSON e ritorno le sequenze di dialogo
						primo.map( (val, index) => {
							return(
							<DialogText
								key={index}
								i={index}		// Il numero di ogni sequenza di dialogo
								now={n}			// Il numero al quale deve essere visualizzata
								text={val.text}	// testo da visuallizzare
								people={val.people}	// persona che parla
							/>
						)})
					}
				</Modal.Body>
			</Modal>
   	</>
	)
}

export default Dialog;