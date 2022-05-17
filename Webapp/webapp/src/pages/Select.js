// Selezione per i personaggi

import { useState, useContext } from "react";
import { Container, Row, Col, Button, Carousel, Image, ProgressBar } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { charSound } from "../assets/sounds/sounds";
import { useAudio } from "../utils/utils";
import { PgCtx } from "../components/components";
import players from "./players";

const Select = () => {
	const [index, setIndex] = useState(0);
	const [play, toggle] = useAudio(charSound);
	const { setPg } = useContext(PgCtx);
	const navigate = useNavigate();

	const backToMenu = () => navigate('../menu', {replace: true});
	const handleSelect = eventKey => {
		if (!play) toggle();
		setIndex(eventKey);
	};
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
					height={600}
				/>
			</Carousel.Item>
		))
	);

	const loadStats = () => (
		players[index].stats.map( value => (
			<>
				<p className="text-white fs-5 txt-pixel mb-2 mt-2">
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
					<Row className="d-flex justify-content-center">
						<Col xxl={10} className="px-5">
							{loadStats()}
						</Col>
					</Row>
				</Col>
			</Row>
			<Row className="mt-2">
				<Confirm callback={confirmPg} />
				<Back callback={backToMenu} />
			</Row>
		</Container>
	)
};

const Title = () => (
	<Row>
		<Col>
			<p className="text-white text-center txt-pixel display-5 mt-3">
				SELECT YOUR CHARACTER
			</p>
		</Col>
	</Row>
);

const Confirm = ({callback}) => (
	<Col className="d-flex justify-content-center">
		<Button
			className="txt-pixel fs-4 p-3"
			onClick={callback}
			variant="success"
			size="lg"
		>
			Confirm
		</Button>
	</Col>
);

const Back = ({callback}) => (
	<Col className="d-flex justify-content-center">
		<Button
			className="txt-pixel fs-4 p-3"
			onClick={callback}
			variant="danger"
			size="lg"
		>
			Back
		</Button>
	</Col>
);

const StatsTitle = () => (
	<Row>
		<Col>
			<p className="text-white text-center txt-pixel fs-2">
				Stats
			</p>
		</Col>
	</Row>
);

const PgLabel = ({name}) => (
	<Row>
		<Col>
			<p className="text-white text-center txt-pixel fs-2">
				{name}
			</p>
		</Col>
	</Row>

)


export default Select;