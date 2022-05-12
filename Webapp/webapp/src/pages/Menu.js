// Pagina Menu Principale

import { Col, Container, Row } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";

/*
	Con i File Export posso fare cose di questro tipo
	cioè importare decine di componenti in una sola riga
*/
import { SplashScreen, Title, Footer, Options, BtnPlay, BtnOptions, BtnRank, BtnMusic, Setting } from '../components/components';

import '../style/Menu.css';
import '../style/Font.css';

const Menu = () => {
	const { setSetting } = useContext(Setting);		// recupero funzione globale
	let navigate = useNavigate();			// questo serve per navigare fra gli EndPoint

	const openSettings = () => setSetting(true);		// Aprire le impostazioni
	const play = () => navigate('../play', {replace: true});		// Passare alla pagina di gioco

	/*
		Row e Col sono dei componenti Bootstrap che permettono di suddividere le pagine in righe e colonne
		Le classi CSS dei componenti sono identiche a quelle di Bootstrap 5
	*/

	return (
		<>
			<Container fluid>
				<Row className='w-100 mt-5 position-absolute top-0 start-50 translate-middle-x'>
					<Title />
				</Row>
				<Row className="p-3 w-75 position-absolute top-50 start-50 translate-middle">
					<Col className="d-flex justify-content-start" xxl={4}>
						<BtnOptions callback={openSettings} /* la prop callback è la funzione che voglio eseguire */ />
					</Col>
					<Col className="d-flex justify-content-center" xxl={4}>
						<BtnPlay callback={play} />
					</Col>
					<Col className="d-flex justify-content-end" xxl={4}>
						<BtnRank /*Per ora questo è senza funzioni */  />
					</Col>
				</Row>
				<Row className="mb-5 w-100 position-absolute bottom-0 start-50 translate-middle-x ">
					<Footer />
				</Row>
				<Row className="mb-3 position-absolute bottom-0 start-50 translate-middle">
					<Col>
						<BtnMusic />
					</Col>
				</Row>
			</Container>
			<Options exit={false} /* Exit è false perchè siamo nella Home */ />
			<SplashScreen /* Questo serve per l'animazione di caricamento del menu */ />
		</>
	);
}

export default Menu;