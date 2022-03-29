// Pagina di Gioco

import { useRef, useCallback, useContext, useEffect } from 'react';
import { GameEngine } from 'react-game-engine';

import Player from '../entities/Player';
import Loop from '../system/Loop';
import Options from '../components/Options';
import { Pausa } from '../components/GlobalProvider';

import '../style/Play.css';

const Play = () => {
	const { pause, setPause } = useContext(Pausa);
	const engine = useRef();

	const togglePause = useCallback(ev => {
		if (ev.key === "e")
			setPause(true);
	}, [])

	useEffect(() => {
		document.addEventListener("keydown", togglePause, false);
		return () => {
			document.removeEventListener("keydown", togglePause, false);
		}
	}, []);

	return (
		<GameEngine
			ref={engine}
			className='Stage'
			systems={[Loop]}
			running={!pause}
			entities={{
				player: { x: 1000, y: 400, speed: 10, src: require('../assets/characters/Seima.png'), renderer: <Player /> }
			}}
		>
			<Options
				show={pause}
				onHide={() => setPause(false)}
				exit={true}
			/>
		</GameEngine>
	)
}

export default Play;