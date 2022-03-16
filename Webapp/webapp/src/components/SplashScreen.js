import { useEffect, useState } from "react";
import { Container, Row, Col, Image } from "react-bootstrap";

import '../style/App.css';
import denina from '../img/denina.png';

const SplashScreen = () => {
	const [animate, setAnimate] = useState(true);

	useEffect( () => {
		const dissappear = setTimeout(() => {
			setAnimate(false);
		}, 3500)

		return () => clearInterval(dissappear);
	}, []);

	return(
		<>
		{
			animate && (
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
			)
		}</>
	)
}

export default SplashScreen;