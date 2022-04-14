// Pagina di Gioco

import { useRef, useCallback, useContext } from 'react';
import { GameEngine } from 'react-game-engine';
import useEntities from '../entities/useEntities';

import { Options , Dialog, Pausa, DialogOpen, } from '../components/components';
import { useEventListener } from '../utils/utils';
import Timer from '../system/Timer';
import LoopRiserva from '../system/LoopRiserva';

import '../style/Play.css';

const Play = () => {
	const { pause, setPause } = useContext(Pausa);
	const { setDialog } = useContext(DialogOpen);
	const engine = useRef();

	const togglePause = useCallback(ev => {
		if (ev.key === "e")
			setPause(true);
		else if (ev.key === 'q')
			setDialog(true);
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