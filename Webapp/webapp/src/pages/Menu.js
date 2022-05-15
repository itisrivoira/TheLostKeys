// Pagina Menu Principale

import { Col, Container, Row } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";
/*
	Con i File Export posso fare cose di questro tipo
	cioè importare decine di componenti in una sola riga
*/
import { SplashScreen, SettingsUI, BtnPlay, BtnOptions, BtnRank, BtnMusic, SettingCtx } from '../components/components';

import '../style/Menu.css';
import '../style/Font.css';

const Menu = () => {
	const { setSetting } = useContext(SettingCtx);		// recupero funzione globale
	let navigate = useNavigate();			// questo serve per navigare fra gli EndPoint


	const openSettings = () => setSetting(true);		// Aprire le impostazioni
	const play = () => navigate('../select', {replace: true});		// Passare alla pagina di gioco
	const rank = () => navigate('../rank', {replace: true});		// Passare alla classifica

	/*
		Row e Col sono dei componenti Bootstrap che permettono di suddividere le pagine in righe e colonne
		Le classi CSS dei componenti sono identiche a quelle di Bootstrap 5
	*/

	return (
		<>
			<Container fluid>
				<Title />
				<Row className="p-3 w-75 position-absolute top-50 start-50 translate-middle">
					<Col className="d-flex justify-content-start" xxl={4}>
						<BtnOptions callback={openSettings} /* la prop callback è la funzione che voglio eseguire */ />
					</Col>
					<Col className="d-flex justify-content-center" xxl={4}>
						<BtnPlay callback={play} />
					</Col>
					<Col className="d-flex justify-content-end" xxl={4}>
						<BtnRank callback={rank}  />
					</Col>
				</Row>
				<Footer />
				<Row className="mb-3 position-absolute bottom-0 start-50 translate-middle">
					<Col>
						<BtnMusic />
					</Col>
				</Row>
			</Container>
			<SettingsUI exit={false} /* Exit è false perchè siamo nella Home */ />
			<SplashScreen /* Questo serve per l'animazione di caricamento del menu */ />
		</>
	);
}

const Title = () => (
	<Row className='w-100 mt-5 position-absolute top-0 start-50 translate-middle-x'>
		<p className='text-black display-1 fw-bold text-center txt-pixel'>
			The Lost Keys
		</p>
	</Row>
);

const Footer = () => (
	<Row className="mb-5 w-100 position-absolute bottom-0 start-50 translate-middle-x ">
		<Col className="mt-5">
			<p className="text-center text-white fs-2 txt-pixel">
				The Lost Key Team
			</p>
		</Col>
		<Col className="mt-5" >
			<p className="text-center text-white fs-2 txt-pixel">
				Alpha 7.0
			</p>
		</Col>
	</Row>
);


export default Menu;