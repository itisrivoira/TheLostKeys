/*
	Splashscreen della Web App (work in progress)
	Probabilmente la modicherò
	Eseguo un animazione CSS con i @keyframes e poi nascondo l'intera schermata
*/

import { useEffect, useState } from "react";
import { Container, Row, Col, Image } from "react-bootstrap";

import { denina, logo } from '../assets/img/img';
import { useEventListener, useTimeout } from "../utils/utils";

const SplashScreen = () => {
	const [animate, setAnimate] = useState(true);
	const [first, setFirst] = useState(true);

	const skip = () => setAnimate(false);
	const change = () => setFirst(false);

	useTimeout(change, 3250);
	useTimeout(skip, 10000);
	useEventListener('keydown', skip);

	return( animate && (
		<Container fluid className="complete d-flex align-items-center justify-content-center p-0 m-0">
			{ first ? <FirstFade/> : <SecondFade /> }
			<SkipFade />
		</Container>
	))
};

const FirstFade = () => (
	<Row className="splash w-100">
		<Col className="d-flex justify-content-center">
			<Image src={denina} height={275} width={275} fluid />
		</Col>
		<Col xxl={8} className="d-flex d-flex align-items-center">
			<p className="fs-1 text-center text-white txt-pixel">
				Presented by <br/> IIS Denina Pellico Rivoira
			</p>
		</Col>
	</Row>
);

const SecondFade = () => (
	<Row className="secondSplash w-100">
		<Col className="d-flex justify-content-center">
			<Image src={logo} height={275} width={275} fluid />
		</Col>
		<Col xxl={8} className="d-flex d-flex align-items-center">
			<p className="fs-1 text-center text-white txt-pixel">
				Created and Developed by <br/> The Lost Key Teams
			</p>
		</Col>
	</Row>
);

const SkipFade = () => (
	<Row className="skip position-absolute bottom-0 start-50 translate-middle mb-4">
		<Col>
			<p className="fs-2 text-center text-white txt-pixel">
				Press any key to skip
			</p>
		</Col>
	</Row>
)


export default SplashScreen;