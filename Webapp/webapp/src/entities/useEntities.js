// Tutte entita di gioco

import { useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { PgCtx } from '../components/components';

import UHD from './UHD';
import Player from './Player';
import Room from './Room';

const useEntities = () => {
	const { pg } = useContext(PgCtx);
	const navigate = useNavigate();

	useEffect( () => {
		// controllo se l'utente non ha scelto giocatori (quindi pg rimane vuoto)
		if (Object.keys(pg).length === 0)
			navigate('../menu', {replace: true});
	}, [pg]);

	const entities = {
		player: {
			x: 100,					// coordinata X iniziale
			y: 450,					// coordinata Y iniziale
			pg: pg.name,			// nome del pg che sto usando
			speed: pg.speed + parseInt(pg.speed/3),	// velocità
			src: pg.img,			// sprite
			renderer: <Player/>
		},

		room: {	// Posso inserire tutte le prop che voglio
			name: 'PianoT',		// Nome della stanza
			evType: '',				// Tipo di evento
			evOptions: {},			// Opzioni dell'Evento
			renderer: <Room />	// La prop renderer contiene il Componente da renderizzare a schermo
		},

		uhd: {
			min: 10,		// minuti
			sec: 0,		// secondi
			gameOver: false,
			gameWin: false,
			renderer: <UHD />
		}
	};

	return entities;
}

export default useEntities;