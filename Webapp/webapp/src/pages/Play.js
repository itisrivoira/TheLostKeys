// Pagina di Gioco

import { useCallback, useContext, useEffect, useState } from 'react';
import { GameEngine } from 'react-game-engine';

import Box from '../entities/Box';
import Loop from '../system/Loop';
import Options from '../components/Options';
import { Pausa } from '../components/GlobalProvider';

import '../style/Play.css';

const Play = () => {
	const [x] = useState(850);
	const [y] = useState(300);
	const {pause, setPause} = useContext(Pausa);
	const [run, setRun] = useState(true);

	const togglePause = useCallback( ev => {
		if ( ev.key === "Escape")
			setPause(true);
	}, [])

	useEffect( () => {
		document.addEventListener("keydown", togglePause, false);
		return () => {
			document.removeEventListener("keydown", togglePause, false);
		}
	}, []);

	return(
		<GameEngine
			className='Stage'
			systems={[Loop]}
			entities={{
				box1: {x: x, y: y, speed: 5, renderer: <Box x={x} y={y} />}
			}}
		>\
			<Options show={pause} onHide={() => setPause(false)} exit={true} />
		</GameEngine>
	)
}

export default Play;