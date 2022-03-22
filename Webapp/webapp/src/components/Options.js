// Pannello delle Opzioni
import { useState } from "react";
import { Button, Modal } from "react-bootstrap";

import '../style/App.css';

const Options = props => {
	const [full, setFull] = useState(false);
	// vero --> schermo intero attivo
	// falso --> schermo intero spento
	// https://github.com/Darth-Knoppix/example-react-fullscreen/blob/master/src/utils/useFullscreenStatus.js
	// da modificare

	return(
		<Modal
			{...props}
			size="lg"
			centered
			keyboard
		>
			<Modal.Header
				closeButton
				className="bg-secondary"
			>
				<Modal.Title className="w-100">
					<p className="txt-pixel text-center fs-2 m-0">
						Options
					</p>
				</Modal.Title>
			</Modal.Header>
			<Modal.Body className="bg-secondary">
				<p>
					Queste sono le opzioni
				</p>

				<Button variant="outline-secondary">
					Toggle FullScreen
				</Button>
			</Modal.Body>
		</Modal>
	)
}

export default Options;