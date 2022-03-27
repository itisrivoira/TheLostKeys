// Pannello delle Opzioni

import { useState } from "react";
import { Col, Button, Modal, Row, ProgressBar, Container } from "react-bootstrap";
import { BsPlusLg, BsDashLg } from "react-icons/bs";
import { useNavigate } from "react-router-dom";

import useFullScreen from "../utils/useFullScreen";

import '../style/App.css';

const Options = props => {
	const { fullScreen, toggle } = useFullScreen();
	const [primo, setPrimo] = useState(50);
	const [secondo, setSecondo] = useState(50);
	let navigate = useNavigate();

	const backToMenu = () => {
		navigate('../menu', {replace: true});
		props.onHide();
	}

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
				<Container fluid>
					<Row className="text-center">
						<Col>
							<p className="txt-pixel fs-3">
								Musica
							</p>
						</Col>
					</Row>
					<Row className="mb-3 text-center d-flex justify-content-center">
							<Row className="w-75 mb-3">
								<Col>
									<ProgressBar striped variant="dark" now={primo} min={0} max={100} />
								</Col>
							</Row>
							<Row className="w-75">
								<Col>
									<Button variant="dark" onClick={() => setPrimo(prev => prev - 10)}>
										<BsDashLg size={20} />
									</Button>
								</Col>
								<Col>
									<Button variant="dark" onClick={() => setPrimo(prev => prev + 10)}>
										<BsPlusLg size={20} />
									</Button>
								</Col>
							</Row>
					</Row>
					<Row className="text-center">
						<Col>
							<p className="txt-pixel fs-3">
								Effetti Audio
							</p>
						</Col>
					</Row>
					<Row className="mb-3 text-center d-flex justify-content-center">
							<Row className="w-75 mb-3">
								<Col>
									<ProgressBar striped variant="dark" now={secondo} min={0} max={100} />
								</Col>
							</Row>
							<Row className="w-75">
								<Col>
									<Button variant="dark" onClick={() => setSecondo(prev => prev -10)}>
										<BsDashLg size={20} />
									</Button>
								</Col>
								<Col>
									<Button variant="dark" onClick={() => setSecondo(prev => prev +10 )}>
										<BsPlusLg size={20} />
									</Button>
								</Col>
							</Row>
					</Row>
					<Row className="text-center">
						<Col>
							<Button className="txt-pixel" onClick={toggle} variant="dark" >
								{fullScreen ? ' FullScreen Off' : 'FullScreen On'}
							</Button>
						</Col>
						{
							props.exit
							&&
							<Col className="">
								<Button className="txt-pixel" onClick={backToMenu} variant='danger'>
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