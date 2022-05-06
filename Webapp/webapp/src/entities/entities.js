// Tutte entita di gioco

import UHD from './UHD';
import Player from './Player';
import Room from './Room';

const entities = () => {

	return {
		room: {	// Posso inserire tutte le prop che voglio
			name: 'Chimica',	// Nome della stanza
			event: false,
			evType: '',			// Tipo di evento
			evOptions: {},		// Opzioni dell'Evento
			renderer: <Room />	// La prop renderer contiene il Componente da renderizzare a schermo
		},

		player: {
			x: 1200,		// coordinata X
			y: 400,		// coordinata Y
			speed: 4,	// velocità
			src: require('../assets/characters/Seima.png'),		// sprite
			renderer: <Player />
		},

		uhd: {
			min: 25,		// minuti
			sec: 0,		// secondi
			renderer: <UHD />
		}
	}
}

export default entities;