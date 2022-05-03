// Pannello delle Setting

import { useContext } from "react";
import { Col, Button, Modal, Row,  Container } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { BsKeyboard } from "react-icons/bs";

import { useFullScreen } from "../utils/utils";
import { Audio, Music, Sfx, Setting, Run, Comandi, Commands } from './components';

const Options = ({exit}) => {
	const { fullScreen, toggle } = useFullScreen();
	const { setting, setSetting } = useContext(Setting);
	const { run, setRun } = useContext(Run);
	const { music, setMusic } = useContext(Music);
	const { sfx, setSfx } = useContext(Sfx);
	const { setComandi } = useContext(Comandi);
	let navigate = useNavigate();

	const handleCommands = () => setComandi(true);

	const backToMenu = () => {
		navigate('../menu', {replace: true});
		setSetting(false);
	}

	const HandleClose = () => {
		setSetting(false);
		if ( !run ) setRun(true);
	}

	return(
		<Modal
			show={setting}
			onHide={HandleClose}
			backdrop="static"
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
					<hr/>
					<Row className="text-center">
						<Col>
							<Button className="txt-pixel fs-5 p-2 px-3 my-2" onClick={handleCommands}>
								<BsKeyboard size={45}/> Comandi
							</Button>
						</Col>
					</Row>
					<hr/>
					<Row className="text-center">
						<Col>
							<Button className="txt-pixel p-3 my-3" onClick={toggle} variant="dark" >
								{ fullScreen ? ' FullScreen Off' : 'FullScreen On' }
							</Button>
						</Col>
						{
							exit
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
			<Commands />
		</Modal>
	)
}

export default Options;