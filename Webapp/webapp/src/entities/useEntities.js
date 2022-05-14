// Tutte entita di gioco

import { useContext } from 'react';
import { PgCtx } from '../components/components';

import UHD from './UHD';
import Player from './Player';
import Room from './Room';

const useEntities = () => {
	const { pg } = useContext(PgCtx);

	const entities = {
		player: {
			x: 100,					// coordinata X iniziale
			y: 450,					// coordinata Y iniziale
			name: pg.name,			// nome del pg che sto usando
			speed: pg.speed * 2,	// velocità
			src: pg.img,			// sprite
			renderer: <Player/>
		},

		room: {	// Posso inserire tutte le prop che voglio
			name: 'PianoT',		// Nome della stanza
			event: false,			// Da togliere
			evType: '',				// Tipo di evento
			evOptions: {},			// Opzioni dell'Evento
			renderer: <Room />	// La prop renderer contiene il Componente da renderizzare a schermo
		},

		uhd: {
			min: 10,		// minuti
			sec: 0,		// secondi
			gameOver: false,
			renderer: <UHD />
		}
	};

	return entities;
}

export default useEntities;