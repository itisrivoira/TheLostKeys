// Pagina di Gioco

import { useCallback, useEffect, useState } from 'react';
import { GameEngine } from 'react-game-engine';
import { useNavigate } from 'react-router-dom';

import Box from '../entities/Box';
import Loop from '../system/Loop';

import '../style/Play.css';

const Play = () => {
	let navigate = useNavigate();
	const [x] = useState(850);
	const [y] = useState(300);

	const backToMenu = useCallback( ev => {
		if ( ev.key === "Escape")
			navigate('../menu', {replace: true});
	}, [])

	useEffect( () => {
		document.addEventListener("keydown", backToMenu, false);
		return () => {
			document.removeEventListener("keydown", backToMenu, false);
		}
	}, []);

	return(
		<GameEngine
			className='Stage'
			systems={[Loop]}
			entities={{
				box1: {x: x, y: y, speed: 100, renderer: <Box x={x} y={y} />}
			}}
		>
		</GameEngine>
	)
}

export default Play;