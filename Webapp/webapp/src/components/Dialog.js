// Componente Dialogo

import { Modal } from "react-bootstrap";
import { useState, useContext, useEffect } from "react";

import DialogText from "./DialogText";
import { DialogOpen } from "./GlobalProvider";
import primo from '../assets/dialogs/primo.json';

import '../style/Dialog.css';

const Dialog = () => {
	const [n, setN] = useState(0);
	const { dialog, setDialog } = useContext(DialogOpen);

	useEffect( () => {
		if (n == primo.length) {
			setDialog(false);
			setN(0);
		}
	}, [n])

	const next = e => {
		if (e.key === 'Enter') {
			setN(prev => prev + 1);
		}
	}

	const handleClose = () => {
		setDialog(false);
		setN(0);
	}

	useEffect( () => {
		document.addEventListener('keydown', next, false);

		return () => {
			document.removeEventListener('keydown', next, false);
		}
	}, []);

	return(
		<>
			<Modal
				show={dialog}
				onHide={handleClose}
				animation={false}
				size='lg'
				dialogClassName="position-absolute bottom-0 start-50 translate-middle-x customw"
			>
				<Modal.Body
					className="bg-secondary"
				>
					{
						primo.map( (val, index) => {
							return(
							<DialogText
								i={index}
								now={n}
								text={val.text}
								key={index}
							/>

						)})
					}
				</Modal.Body>
			</Modal>
   	</>
	)
}

export default Dialog;