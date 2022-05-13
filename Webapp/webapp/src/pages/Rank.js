// Classifica del Gioco con record del giocatore

import { useNavigate } from "react-router-dom";
import { Container, Row, Col, Button } from "react-bootstrap";

const Rank = () => {
	let navigate = useNavigate();

	const backToMenu = () => navigate('../menu', {replace: true});

	return(
		<Container className="w-100 h-100 bg-dark" fluid>
			<Row>
				<Col className="text-center mt-3">
					<p className="display-3 txt-pixel text-white">
						RANK OF THE GAME
					</p>
				</Col>
			</Row>
			<Row>
				<Col>
					my Highscore
				</Col>
				<Col>
					all ranks
				</Col>
			</Row>
			<Row className="mb-5 position-absolute bottom-0 start-50 translate-middle-x">
				<Col>
					<Button
						className="txt-pixel fs-1 p-3"
						onClick={backToMenu}
						variant="danger"
						size="lg"
					>
						Back
					</Button>
				</Col>
			</Row>
		</Container>
	)
}

export default Rank;