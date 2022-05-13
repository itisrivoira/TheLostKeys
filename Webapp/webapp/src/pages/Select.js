// Selezione per i personaggi

import { Container, Row, Col, Button } from "react-bootstrap";


const Select = () => {



	return(
		<Container fluid>
			<Title />

			<Confirm />
		</Container>
	)
};

const Title = () => (
	<Row>
		<Col>
			<p>
				SELECT YOUR CHARACTER
			</p>
		</Col>
	</Row>
);

const Confirm = () => (
	<Row>
		<Col>
			<Button
				variant="success"
			>
				Confirm
			</Button>
		</Col>
	</Row>
)

export default Select;