// Pagina di Gioco

import { useRef, useCallback, useContext, useEffect } from 'react';
import { GameEngine } from 'react-game-engine';
import useEntities from '../entities/useEntities';

import Timer from '../system/Timer';
import Loop from '../system/Loop';
import Options from '../components/Options';
import Dialog from '../components/Dialog';
import { Pausa, DialogOpen } from '../components/GlobalProvider';

import '../style/Play.css';

const Play = () => {
	const { pause, setPause } = useContext(Pausa);
	const { dialog, setDialog } = useContext(DialogOpen);
	const engine = useRef();

	const togglePause = useCallback(ev => {
		if (ev.key === "e")
			setPause(true);
		else if (ev.key === 'q')
			setDialog(true);
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
			systems={[Loop, Timer]}
			running={!pause}
			entities={useEntities()}
		>
			<Options
				show={pause}
				onHide={() => setPause(false)}
				exit={true}
			/>
			<Dialog />
		</GameEngine>
	)
}

export default Play;