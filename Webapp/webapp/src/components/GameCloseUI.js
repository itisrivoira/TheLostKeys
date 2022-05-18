/*
	Schermata Del Game Over
	Da cui potro uplodare il mio punteggio
*/

import { useContext } from "react";
import { Image, Modal, Row, Col, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { GameOverCtx, ScoreCtx, CloseCtx } from "./components";
import { Skull } from "../assets/img/img";

const GameCloseUI = () => {
	const { gameOver } = useContext(GameOverCtx);
	const { close } = useContext(CloseCtx);
	const { score } = useContext(ScoreCtx);
	const navigate = useNavigate();

	const restart = () => navigate('../select', {replace: true});
	const backToMenu = () => { navigate('../menu', {replace: true}) };

	const upload = () => {
		fetch('http://127.0.0.1:4000/upload', {
			method: 'POST',
			headers: {'Content-Type': 'application/json', 'Accept':'application/json'},
			body: JSON.stringify({
				nick: 'Seima',
				score: 2000,
				pg: 'Personaggio Giocabile'
			})
		})
	}

	return(
		<Modal
			show={close}
			animation={false}
			fullscreen
		>
			<Modal.Body className={`bg-dark w-100 h-100 ${!gameOver && 'win'}`}>
				{gameOver && <GameOverTitle />}
				<Row className={!gameOver && "position-absolute top-50 start-50 translate-middle w-75"}>
					{
						!gameOver
						&&
						<p className="fs-1 text-white text-center">
							You Win!!!
						</p>
					}
					<Row className="my-3">
						<Col className="text-center">
							<p className="fs-1 txt-pixel text-white">
								Your Final Score is: {score}
							</p>
						</Col>
					</Row>
					<Row className="my-3">
						<Restart callback={restart} />
						<Upload callback={upload} />
						<Exit callback={backToMenu} />
					</Row>
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

const GameOverTitle = () => (<>
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
</>)

const Upload = ({callback}) => (
	<Col xxl={2} className="text-center txt-pixel">
		<Button
			className="p-3 fs-3 text-white"
			variant="info"
			size="lg"
			onClick={callback}
		>
			Upload
		</Button>
	</Col>
);

const Exit = ({callback}) => (
	<Col xxl={5} className="text-start txt-pixel">
		<Button
			className="p-3 fs-3"
			variant="danger"
			size="lg"
			onClick={callback}
		>
			Exit The Game
		</Button>
	</Col>
);

const Restart = ({callback}) => (
	<Col xxl={5} className="text-end txt-pixel">
		<Button
			className="p-3 fs-3"
			variant="success"
			size="lg"
			onClick={callback}
		>
			Restart
		</Button>
	</Col>
);

export default GameCloseUI;