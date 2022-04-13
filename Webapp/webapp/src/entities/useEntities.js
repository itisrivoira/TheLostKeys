// tutte entita di gioco

import { useEffect, useState } from 'react';
import CountDown from './CountDown';
import Player from './Player';

const useEntities = () => {

	return {
		player: {
			x: 1100,
			y: 400,
			speed: 8,
			src: require('../assets/characters/Seima.png'),
			renderer: <Player />
		},

		countdown: {
			x: 700,
			y: 50,
			min: 25,
			sec: 0,
			renderer: <CountDown />
		}
	}
}

export default useEntities;