// Pagina Menu Principale

import { Col, Container, Row } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";

import { SplashScreen, Title, Footer, Options, BtnPlay, BtnOptions, BtnLogin, BtnMusic, Setting } from '../components/components';

import '../style/App.css';
import '../style/Font.css';

const Menu = () => {
	const { setSetting } = useContext(Setting);
	let navigate = useNavigate();

	const openSettings = () => setSetting(true);
	const play = () => navigate('../play', {replace: true});

	return (
		<>
			<Container fluid>
				<Row className='w-100 mt-5 position-absolute top-0 start-50 translate-middle-x'>
					<Title />
				</Row>
				<Row className="p-3 w-75 position-absolute top-50 start-50 translate-middle">
					<Col className="d-flex justify-content-start" xxl={4}>
						<BtnOptions callback={openSettings} />
					</Col>
					<Col className="d-flex justify-content-center" xxl={4}>
						<BtnPlay callback={play} />
					</Col>
					<Col className="d-flex justify-content-end" xxl={4}>
						<BtnLogin />
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
			<Options exit={false} />
			<SplashScreen />
		</>
	);
}

export default Menu;