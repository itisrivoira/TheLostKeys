// Pannello delle Opzioni

import { useContext } from "react";
import { Col, Button, Modal, Row,  Container } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { useFullScreen } from "../utils/utils";
import { Audio, Music, Sfx } from './components';

import '../style/App.css';

const Options = props => {
	const { fullScreen, toggle } = useFullScreen();
	const { music, setMusic } = useContext(Music);
	const { sfx, setSfx } = useContext(Sfx);
	let navigate = useNavigate();

	const backToMenu = () => {
		navigate('../menu', {replace: true});
		props.onHide();
	}

	return(
		<Modal
			show={props.show}
			onHide={props.onHide}
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
				<Container fluid>
					<Audio
						title='Musica'
						volume={music}
						changer={setMusic}
					/>
					<Audio
						title='Effetti Sonori'
						volume={sfx}
						changer={setSfx}
					/>
					<Row className="text-center">
						<Col>
							<Button className="txt-pixel p-3 my-3" onClick={toggle} variant="dark" >
								{fullScreen ? ' FullScreen Off' : 'FullScreen On'}
							</Button>
						</Col>
						{
							props.exit
							&&
							<Col className="">
								<Button className="txt-pixel p-3 my-3" onClick={backToMenu} variant='danger'>
									Exit The Game
								</Button>
							</Col>
						}
					</Row>
				</Container>
			</Modal.Body>
		</Modal>
	)
}

export default Options;