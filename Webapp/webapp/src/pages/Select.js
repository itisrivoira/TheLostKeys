// Selezione per i personaggi

import { useState, useContext } from "react";
import { Container, Row, Col, Button, Carousel, Image, ProgressBar } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { PgCtx } from "../components/components";
import players from "./players";

const Select = () => {
	const [index, setIndex] = useState(0);
	const { setPg } = useContext(PgCtx);
	let navigate = useNavigate();

	const handleSelect = eventKey => { setIndex(eventKey) };
	const confirmPg = () => {
		setPg({
			name: players[index].name,					// nome del personaggio
			img: players[index].img,					// immagine del personaggio
			speed: players[index].stats[9].value	// velocità del personaggio
		});
		navigate('../play', {replace: true});
	};

	const loadItems = () => (
		players.map( value => (
			<Carousel.Item className="text-center">
				<Image
					style={{imageRendering: "pixelated"}}
					src={value.img}
					width={450}
					height={650}
				/>
			</Carousel.Item>
		))
	);

	const loadStats = () => (
		players[index].stats.map( value => (
			<>
				<p className="text-white">
					{value.name}
				</p>
				<ProgressBar now={value.value} max={10} variant="primary" striped />
			</>
		))
	);

	return(
		<Container className="w-100 h-100 bg-dark" fluid>
			<Title />
			<Row>
				<Col xxl={5}>
					<PgLabel name={players[index].name} />
					<Row>
						<Col>
							<Carousel activeIndex={index} slide={false} onSelect={handleSelect}>
								{loadItems()}
							</Carousel>
						</Col>
					</Row>
				</Col>
				<Col xxl={7}>
					<StatsTitle />
					<Row>
						<Col>
							{loadStats()}
						</Col>
					</Row>
				</Col>
			</Row>
			<Confirm callback={confirmPg} />
		</Container>
	)
};

const Title = () => (
	<Row>
		<Col>
			<p className="text-white">
				SELECT YOUR CHARACTER
			</p>
		</Col>
	</Row>
);

const Confirm = ({callback}) => (
	<Row>
		<Col>
			<Button
				onClick={callback}
				variant="success"
			>
				Confirm
			</Button>
		</Col>
	</Row>
);

const StatsTitle = () => (
	<Row>
		<Col>
			<p className="text-white">
				Statistiche
			</p>
		</Col>
	</Row>
);

const PgLabel = ({name}) => (
	<Row>
		<Col>
			<p className="text-white">
				{name}
			</p>
		</Col>
	</Row>

)


export default Select;