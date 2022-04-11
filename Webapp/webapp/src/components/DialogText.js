// testo del dialogo con vignetta

import { Col, Row } from "react-bootstrap";

const DialogText = ({i, now, text}) => {

	return(i === now && (
		<Row className="px-3">
			<Col
				xxl={3}
				className='bg-secondary bg-gradient rounded-pill d-flex align-items-center'
			>
				<Row>

				</Row>
				<Row>
					<p>
						Narratore
					</p>
				</Row>
			</Col>
			<Col xxl={9}>

					<p
						className="text-white fs-4 ms-4"
					>
						{text}
					</p>

			</Col>

		</Row>
		)
	)
}

export default DialogText;