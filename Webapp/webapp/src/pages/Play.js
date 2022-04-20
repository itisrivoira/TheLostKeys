// Pagina di Gioco

import { useRef, useCallback, useContext } from 'react';
import { GameEngine } from 'react-game-engine';

import { Options , Dialog, DialogOpen, Opzioni, Run, EnigmaModal } from '../components/components';
import { useEventListener } from '../utils/utils';
import useEntities from '../entities/useEntities';
import useSystem from '../system/useSystem';

import '../style/Play.css';
import '../style/Font.css';

const Play = () => {
	const { setSetting } = useContext(Opzioni);
	const { setDialog } = useContext(DialogOpen);
	const { run, setRun } = useContext(Run);
	const engine = useRef();

	const togglePause = useCallback( ev => {
		if (ev.key === "e"){
			setSetting(true);
			setRun(false);
		} else if (ev.key === 'q') {
			setDialog(true);
			setRun(false);
		}
	}, [setDialog, setRun, setSetting]);

	const click = ({x,y}) => {
		console.log('click x: ' + x + ' click y: ' + y);
	}

	useEventListener('keydown', togglePause);
	useEventListener('click', click);

	return (
		<GameEngine
			ref={engine}
			running={run}
			systems={useSystem()}
			entities={useEntities()}
			className='Stage'
		>
			<Options	exit={true} />
			<Dialog />
			<EnigmaModal />
		</GameEngine>
	)
}

export default Play;