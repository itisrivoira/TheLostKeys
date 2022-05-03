// conto alla rovescia

import { useContext } from "react";
import { Col, Row } from "react-bootstrap";
import { BsPauseFill, BsPlayFill } from "react-icons/bs";

import { Run, Score } from "../components/components";

const CountDown = ({ x, y, min, sec}) => {
	const { run } = useContext(Run);
	const { score } = useContext(Score);

	return(
		<Row className="position-absolute top-0 start-50 translate-middle-x w-50">
			<Col xxl={4} className="w-30 p-0 mt-3">
				<p className="fs-2 text-white text-center txt-pixel">
					Score: {score}
				</p>
			</Col>
			<Col xxl={2} className="text-center w-25">
			{
				run ?
					<BsPauseFill size={65} className="text-white ms-4 mt-1" />
				:
					<BsPlayFill size={65} className="text-white ms-4 mt-1" />
			}
			</Col>
			<Col xxl={6} className="w-25">
				<p className="text-white fs-1 text-center me-5 mt-2 txt-pixel">
					{min}:{sec}
				</p>
			</Col>
		</Row>
	)
}

export default CountDown;