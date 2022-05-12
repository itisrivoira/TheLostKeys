/*
	Schermata Del Game Over
	Da cui potro uplodare il mio punteggio
*/

import { useContext } from "react";
import { Image, Modal, Row, Col, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { GameOverCtx, ScoreCtx } from "./components";
import { Skull } from "../assets/img/img";

const GameOverUI = () => {
	const { gameOver } = useContext(GameOverCtx);
	const { score } = useContext(ScoreCtx);
	let navigate = useNavigate();

	const restart = () => { window.location.reload() };
	const backToMenu = () => { navigate('../menu', {replace: true}) };

	return(
		<Modal
			show={gameOver}
			animation={false}
			fullscreen
		>
			<Modal.Body className="bg-dark w-100 h-100">
				<Row>
					<Col className="d-flex justify-content-center">
						<Image
							style={{imageRendering: "pixelated"}}
							src={Skull}
							height={225}
							width={225}
						/>
					</Col>
				</Row>
				<Row className="my-3">
					<CustomText color="warning">
						GAME
					</CustomText>
					<CustomText color="danger">
						OVER
					</CustomText>
				</Row>
				<Row className="my-3">
					<Col className="text-center">
						<p className="fs-1 txt-pixel text-white">
							Your Score is: {score}
						</p>
					</Col>
				</Row>
				<Row className="my-3">
					<Col xxl={5} className="text-end txt-pixel">
						<Button
							className="p-3 fs-3"
							variant="success"
							size="lg"
							onClick={restart}
						>
							Restart
						</Button>
					</Col>
					<Col xxl={2} className="text-center txt-pixel">
						<Button
							className="p-3 fs-3 text-white"
							variant="info"
							size="lg"
						>
							Upload
						</Button>
					</Col>
					<Col xxl={5} className="text-start txt-pixel">
						<Button
							className="p-3 fs-3"
							variant="danger"
							size="lg"
							onClick={backToMenu}
						>
							Exit The Game
						</Button>
					</Col>
				</Row>
			</Modal.Body>
		</Modal>
	)
}

const CustomText = ({children, color}) => (
	<Row>
		<Col className="text-center">
			<p className={`txt-pixel display-3 text-${color} my-1`}>
				{children}
			</p>
		</Col>
	</Row>
)

export default GameOverUI;