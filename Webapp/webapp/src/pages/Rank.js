// Classifica del Gioco con record del giocatore

import { Container, Row, Col } from "react-bootstrap";


const Rank = () => {

	return(
		<Container className="w-100 h-100 bg-dark" fluid>
			<Row>
				<Col>
					<p className="display-3 txt-pixel text-white">
						RANK OF THE GAME
					</p>
				</Col>
			</Row>
		</Container>
	)
}

export default Rank;