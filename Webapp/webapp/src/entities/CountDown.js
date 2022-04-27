// conto alla rovescia

import { useContext } from "react";
import { Col, Row } from "react-bootstrap";
import { BsPauseFill, BsPlayFill } from "react-icons/bs";

import { Run } from "../components/components";

const CountDown = ({ x, y, min, sec}) => {
	const { run } = useContext(Run);

	return(
		<Row className="position-absolute top-0 start-50 translate-middle-x">
			<Col xxl={5} className="text-start">
			{
				run ?
					<BsPauseFill size={65} className="text-white ms-4 mt-1" />
				:
					<BsPlayFill size={65} className="text-white ms-4 mt-1" />
			}
			</Col>
			<Col xxl={7}>
				<p className="text-white fs-1 text-start me-5 mt-2 txt-pixel">
					{min}:{sec}
				</p>
			</Col>
		</Row>
	)
}

export default CountDown;