// testo del dialogo con vignetta

import { Col, Row } from "react-bootstrap";

const DialogText = ({i, now, text, people}) => {

	return( i === now && (
		<Row className="px-3">
			<Col
				xxl={3}
				className='bg-secondary bg-gradient rounded-pill'
			>
				<Row className="h-75 bg-white rounded-pill" xxl={12}>
				</Row>
				<Row className="" xxl={12}>
					<p className="text-center fs-3 text-white">
						{people}
					</p>
				</Row>
			</Col>
			<Col xxl={9}>
				<p className="text-white fs-4 ms-4">
					{text}
				</p>
			</Col>
		</Row>
	))
}

export default DialogText;