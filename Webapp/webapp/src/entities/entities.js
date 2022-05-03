// tutte entita di gioco

import CountDown from './CountDown';
import Player from './Player';
import Room from './Room';

const entities = () => {

	return {
		room: {
			name: 'Chimica',
			event: false,
			evType: '',
			evOptions: {},
			renderer: <Room />
		},

		player: {
			x: 1200,
			y: 400,
			speed: 4,
			src: require('../assets/characters/Seima.png'),
			renderer: <Player />
		},

		countdown: {
			min: 25,
			sec: 0,
			renderer: <CountDown />
		}
	}
}

export default entities;