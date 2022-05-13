// Classifica del Gioco con record del giocatore

import { useNavigate } from "react-router-dom";
import { Container, Row, Col, Button, ListGroup } from "react-bootstrap";

const Rank = () => {
	let navigate = useNavigate();

	const backToMenu = () => navigate('../menu', {replace: true});

	return(
		<Container className="w-100 h-100 bg-dark" fluid>
			<Title />
			<Row className="my-4">
				<Col xxl={4}>
					Your HighScore is
				</Col>
				<Col xxl={8} className="pe-5">
					<ListHead />
					<ListGroup>

					</ListGroup>
				</Col>
			</Row>
			<Back callback={backToMenu} />
		</Container>
	)
};

// Titolo Della Classifica
const Title = () => (
	<Row>
		<Col className="text-center mt-3">
			<p className="display-3 txt-pixel text-white">
				RANK OF THE GAME
			</p>
		</Col>
	</Row>
);

// Pulsante per tornare al menu
const Back = ({callback}) => (
	<Row className="mb-5 position-absolute bottom-0 start-50 translate-middle-x">
		<Col>
			<Button
				className="txt-pixel fs-1 p-3"
				onClick={callback}
				variant="danger"
				size="lg"
			>
				Back
			</Button>
			</Col>
	</Row>
);

// Intestazione della classifica
const ListHead = () => (
	<Row className="text-white fw-bold fs-2 txt-pixel border-bottom border-3 text-center pb-2">
		<Col xxl={1}>
			#
		</Col>
		<Col xxl={4}>
			Nickname
		</Col>
		<Col xxl={3}>
			Points
		</Col>
		<Col xxl={4}>
			Date
		</Col>
	</Row>
)

export default Rank;