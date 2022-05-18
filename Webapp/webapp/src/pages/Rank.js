// Classifica del Gioco con record del giocatore

import { useNavigate } from "react-router-dom";
import { Container, Row, Col, Button, ListGroup } from "react-bootstrap";
import { useEffect, useState } from "react";

const Rank = () => {
	const navigate = useNavigate();
	const [data, setData] = useState([]);

	const backToMenu = () => navigate('../menu', {replace: true});

	useEffect( () => {
		fetch('http://127.0.0.1:4000/rank', {
			method: "GET",
			headers: {"Content-Type": "application/json"}
		})
		.then( res => res.json())
		.then( data => setData(data));
	}, []);

	const loadItems = () => (
		data.map( (value, index) => (
			<ListGroup.Item variant="dark">
				<Row className="txt-pixel fs-2 text-center">
					<Col xxl={2}>
						{index}
					</Col>
					<Col xxl={5}>
						{value.player}
					</Col>
					<Col xxl={5}>
						{value.points}
					</Col>
				</Row>
			</ListGroup.Item>
		))
	);

	return(
		<Container className="w-100 h-100 bg-dark" fluid>
			<Title />
			<Row className="my-4">
				<Col xxl={4}>
					Your HighScore is
				</Col>
				<Col xxl={8} className="pe-5">
					<ListHead />
					<ListGroup variant="flush">
						{loadItems()}
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
		<Col xxl={2}>
			#
		</Col>
		<Col xxl={5}>
			Nickname
		</Col>
		<Col xxl={5}>
			Points
		</Col>
	</Row>
);

export default Rank;