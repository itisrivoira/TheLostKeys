// Componente Dialogo

import { Modal, Row, Col, Image } from "react-bootstrap";
import { useContext } from "react";

import { DialogCtx, RunCtx, PgCtx } from "./components";
import { useEventListener } from '../utils/utils';
import imgDialogs from "../assets/characters/Dialog/Dialog";

const DialogUI = () => {
	const { dialog, setDialog } = useContext(DialogCtx);		// per aprire il modal del Dialogo
	const { run, setRun } = useContext(RunCtx);		// per stoppare il gioco
	const { pg } = useContext(PgCtx);

	// chiudere il modal del dialogo
	const handleClose = () => {
		setDialog(false);
		if ( !run ) setRun(true);
	};

	// Quando premo Invio il testo deve andare avanti
	const next = e => {
		if (e.key === 'Enter')
			handleClose();
	};

	useEventListener('keydown', next);

	return(
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
				<Row className="px-3">
					<Col
						xxl={3}
						className='bg-secondary bg-gradient rounded-pill'
					>
						<Row className="bg-white rounded-pill text-center" xxl={12}>
							<Col>
								<Image
									src={imgDialogs[`${pg.name}`]}
									style={{imageRendering: "pixelated"}}
									height={150}
									width={150}
								/>
							</Col>
						</Row>
						<Row className="mt-1" xxl={12}>
							<p className="text-center fs-3 text-white txt-pixel">
								{pg.name}
							</p>
						</Row>
					</Col>
					<Text />
				</Row>
			</Modal.Body>
		</Modal>
	)
}

const Text = () => (
	<Col xxl={9} className="d-flex align-items-center">
		<p className="text-white fs-3 ms-4 txt-pixel">
			Questa porta non si apre. Forse devo andare da qualche altra parte
		</p>
	</Col>
);

export default DialogUI;