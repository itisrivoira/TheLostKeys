// Componente Dialogo

import { Modal } from "react-bootstrap";
import { useState, useContext, useEffect } from "react";

import { DialogOpen, DialogText, Run } from "./components";
import { useEventListener } from '../utils/utils';
import primo from '../assets/dialogs/primo.json';

import '../style/Dialog.css';

const Dialog = () => {
	const [ n, setN ] = useState(0);
	const { dialog, setDialog } = useContext(DialogOpen);
	const { run, setRun } = useContext(Run);

	const handleClose = () => {
		setDialog(false);
		if ( !run ) setRun(true);
		setN(0);
	};

	useEffect( () => {
		if (n == primo.length) {
			handleClose();
		}
	}, [n]);

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
				animation={false}
				size='lg'
				dialogClassName="position-absolute bottom-0 start-50 translate-middle-x customw"
				backdrop="static"
			>
				<Modal.Body
					className="bg-secondary"
				>
					{
						primo.map( (val, index) => {
							return(
							<DialogText
								key={index}
								i={index}
								now={n}
								text={val.text}
								people={val.people}
							/>

						)})
					}
				</Modal.Body>
			</Modal>
   	</>
	)
}

export default Dialog;