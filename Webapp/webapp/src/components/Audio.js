// Controller volume audio di Gioco

import { useEffect, useState } from "react";
import { Row, Col, Button, ProgressBar } from "react-bootstrap";
import { BsPlusLg, BsDashLg } from "react-icons/bs";

const Audio = ({title, volume, changer}) => {
	const [dash, setDash] = useState(false);
	const [plus, setPlus] = useState(false);

	const increase = () => {changer(prev => prev + 0.1)}
	const reduce = () => {changer(prev => prev - 0.1)}

	useEffect( () => {
		if (volume <= 0.1) {
			setDash(true);
		} else if (volume >= 0.9) {
			setPlus(true);
		} else {
			setDash(false);
			setPlus(false);
		}
	}, [volume]);

	return(
		<>
			<Row className="text-center">
				<Col>
					<p className="txt-pixel fs-3">
						{title}
					</p>
				</Col>
			</Row>
			<Row className="mb-3 text-center d-flex justify-content-center">
				<Row className="w-75 mb-3">
					<Col>
						<ProgressBar striped variant="dark" now={volume} min={0} max={1} />
					</Col>
				</Row>
				<Row className="w-75">
					<Col>
						<Button variant="dark" onClick={reduce} disabled={dash}>
							<BsDashLg size={20} />
						</Button>
					</Col>
					<Col>
						<Button variant="dark" onClick={increase} disabled={plus}>
							<BsPlusLg size={20} />
						</Button>
					</Col>
				</Row>
			</Row>
		</>
	)
}

export default Audio;