// Pannello delle Opzioni

import { Col, Button, Modal, Row } from "react-bootstrap";
import useFullScreen from "../utils/useFullScreen";

import '../style/App.css';

const Options = props => {
	const { fullScreen, toggle } = useFullScreen();

	return(
		<Modal
			{...props}
			size="lg"
			centered
			keyboard
		>
			<Modal.Header
				closeButton
				className="bg-secondary border border-dark border-4"
			>
				<Modal.Title className="w-100">
					<p className="txt-pixel text-center fs-2 m-0">
						Options
					</p>
				</Modal.Title>
			</Modal.Header>
			<Modal.Body className="bg-secondary">
				<Row className="text-center">
					<Col>
						<p>
							Queste sono le opzioni
						</p>
					</Col>
				</Row>
				<Row className="text-center">
					<Col>
						<Button onClick={toggle} size='lg' variant="dark" >
							{fullScreen ? 'Exit FullScreen' : 'Toggle FullScreen'}
						</Button>
					</Col>
				</Row>

			</Modal.Body>
		</Modal>
	)
}

export default Options;