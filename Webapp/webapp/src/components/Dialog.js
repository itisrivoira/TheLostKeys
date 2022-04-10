// Componente Dialogo

import { Modal, Button } from "react-bootstrap";
import { useState, useContext, useEffect } from "react";

import DialogText from "./DialogText";
import { DialogOpen } from "./GlobalProvider";

import '../style/Dialog.css';

const Dialog = () => {
	const [n, setN] = useState(0);
	const { dialog, setDialog } = useContext(DialogOpen);

	useEffect( () => {
		if (n == 3) setDialog(false);
	}, [n])

	return(
		<>
			<Modal
				show={dialog}
				onHide={() => setDialog(false)}
				animation={false}
				dialogClassName="position-absolute bottom-0 start-50 translate-middle-x"
			>
				<Modal.Body>
					{
						['cioa', 'sono', 'bello'].map( (val, index) => {
							return(
							<DialogText
								i={index}
								now={n}
								text={val}
								key={index}
							/>
						)})
					}
					<Button variant="primary" onClick={() => setN(prev => prev + 1)}>
						Avanti
					</Button>
				</Modal.Body>
			</Modal>
   	</>
	)
}

export default Dialog;