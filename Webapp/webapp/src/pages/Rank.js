// Classifica del Gioco con record del giocatore

import { useNavigate } from "react-router-dom";
import { Container, Row, Col, Button, ListGroup, Image } from "react-bootstrap";
import { useEffect, useState } from "react";

import { useAudio, useFetch } from "../utils/utils";
import { menuSound } from "../assets/sounds/sounds";

import imgDialogs from "../assets/characters/Dialog/Dialog";

const Rank = () => {
	const [data, setData] = useState([]);
	const [play, toggle] = useAudio(menuSound);
	const navigate = useNavigate();

	const backToMenu = () => navigate('../menu', {replace: true});

	useEffect( toggle, []);

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
					<Col xxl={1}>
						{index}
					</Col>
					<Col xxl={4}>
						{value.player}
					</Col>
					<Col xxl={4}>
						<Image
							height={70}
							width={70}
							src={imgDialogs[value.pg]}
							style={{imageRendering: "pixelated"}}
						/>
					</Col>
					<Col xxl={3}>
						{value.points}
					</Col>
				</Row>
			</ListGroup.Item>
		))
	);

	return(
		<Container className="w-100 h-100 bg-dark px-3" fluid>
			<Title />
			<Row className="my-4 px-3">
				<Col className="pe-5">
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
		<Col xxl={1}>
			#
		</Col>
		<Col xxl={4}>
			Nickname
		</Col>
		<Col xxl={4}>
			Character
		</Col>
		<Col xxl={3}>
			Points
		</Col>
	</Row>
);

export default Rank;