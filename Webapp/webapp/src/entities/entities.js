// Tutte entita di gioco

import UHD from './UHD';
import Player from './Player';
import Room from './Room';

const entities = () => {

	return {
		room: {	// Posso inserire tutte le prop che voglio
			name: 'Piano2',	// Nome della stanza
			event: false,		// Da togliere
			evType: '',			// Tipo di evento
			evOptions: {},		// Opzioni dell'Evento
			renderer: <Room />	// La prop renderer contiene il Componente da renderizzare a schermo
		},

		player: {
			x: 700,		// coordinata X
			y: 200,		// coordinata Y
			speed: 5,	// velocità
			src: require('../assets/characters/Seima.png'),		// sprite
			renderer: <Player/>
		},

		uhd: {
			min: 10,		// minuti
			sec: 0,		// secondi
			gameOver: false,
			renderer: <UHD />
		}
	}
}

export default entities;