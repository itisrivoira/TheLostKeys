// Pagina di Gioco

import { useRef, useCallback, useContext, useEffect } from 'react';
import { GameEngine } from 'react-game-engine';
import useEntities from '../entities/useEntities';

import { Options , Dialog, DialogOpen, Opzioni, Run } from '../components/components';
import { useEventListener } from '../utils/utils';
import Timer from '../system/Timer';
import LoopRiserva from '../system/LoopRiserva';

import '../style/Play.css';

const Play = () => {
	const { setting, setSetting } = useContext(Opzioni);
	const { setDialog } = useContext(DialogOpen);
	const { run, setRun } = useContext(Run);
	const engine = useRef();

	const togglePause = useCallback(ev => {
		if (ev.key === "e"){
			setSetting(true);
			setRun(false);
		}
		else if (ev.key === 'q') {
			setDialog(true);
			setRun(false);
		}

	}, []);

	const click = ({x,y}) => {
		console.log('click x: ' + x + ' click y: ' + y);
	}

	useEventListener('keydown', togglePause);
	useEventListener('click', click);

	return (
		<GameEngine
			ref={engine}
			className='Stage'
			systems={[LoopRiserva, Timer]}
			running={run}
			entities={useEntities()}
		>
			<Options
				exit={true}
			/>
			<Dialog />
		</GameEngine>
	)
}

export default Play;