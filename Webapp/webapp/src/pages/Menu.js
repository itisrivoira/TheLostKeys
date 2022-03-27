// Pagina Menu Principale

import { Col, Container, Row } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useContext, useState } from "react";

import SplashScreen from "../components/SplashScreen";
import Title from "../components/Title";
import Footer from "../components/Footer";
import Options from "../components/Options";
import { BtnPlay, BtnOptions, BtnLogin, BtnMusic} from "../components/Buttons";
import { Pausa } from "../components/GlobalProvider";

import '../style/App.css';

const Menu = () => {
	const {pause, setPause} = useContext(Pausa);
	let navigate = useNavigate();

	return (
		<>
			<Container fluid>
				<Row className='w-100 mt-5 position-absolute top-0 start-50 translate-middle-x'>
					<Title />
				</Row>
				<Row className="p-3 w-75 position-absolute top-50 start-50 translate-middle">
					<Col className="d-flex justify-content-start" xxl={4}>
						<BtnOptions callback={() => setPause(true)} />
					</Col>
					<Col className="d-flex justify-content-center" xxl={4}>
						<BtnPlay callback={() => navigate('../play', {replace: true})} />
					</Col>
					<Col className="d-flex justify-content-end" xxl={4}>
						<BtnLogin callback={() => alert('Opzioni')} />
					</Col>
				</Row>
				<Row className="mb-5 w-100 position-absolute bottom-0 start-50 translate-middle-x ">
					<Footer />
				</Row>
				<Row className="mb-3 position-absolute bottom-0 start-50 translate-middle">
					<Col>
						<BtnMusic />
					</Col>
				</Row>
			</Container>
			<Options show={pause} onHide={() => setPause(false)} exit={false} />
			<SplashScreen />
		</>
	);
}

export default Menu;