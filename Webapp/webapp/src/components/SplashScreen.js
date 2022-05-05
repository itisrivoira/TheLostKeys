/*
	Splashscreen della Web App (work in progress)
	Probabilmente la modicherò
	Eseguo un animazione CSS con i @keyframes e poi nascondo l'intera schermata
*/

import { useEffect, useState } from "react";
import { Container, Row, Col, Image } from "react-bootstrap";

import { denina } from '../assets/img/img';

const SplashScreen = () => {
	const [animate, setAnimate] = useState(true);

	// Nascondo la schermata dopo 4,2 secondi
	useEffect( () => {
		const dissappear = setTimeout(() => {
			setAnimate(false);
		}, 4200)

		return () => clearInterval(dissappear);
	}, []);

	return( animate && (
		<Container fluid className="complete d-flex align-items-center justify-content-center p-0 m-0">
			<Row className="splash">
				<Col className="d-flex justify-content-end">
					<Image src={denina} fluid />
				</Col>
				<Col xxl={9} className="d-flex d-flex align-items-center">
					<p className="fs-1 text-center text-white txt-pixel">
						Presented by IIS Denina Pellico Rivoira
					</p>
				</Col>
			</Row>
		</Container>
	))
}

export default SplashScreen;