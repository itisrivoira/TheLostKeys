/*
	Pagina di Gioco
	Forse il componente più importante di tutti
*/

import { useCallback, useContext, useEffect } from 'react';
import { GameEngine } from 'react-game-engine';		// Motore di Gioco

import { Options, Dialog, DialogCtx, SettingCtx, RunCtx, EnigmaModal } from '../components/components';
import { useEventListener } from '../utils/utils';
import entities from '../entities/entities';		// Entita di Gioco
import system from '../system/system';		// Funzioni di Logica del Gioco

import '../style/Play.css';
import '../style/Font.css';

const Play = () => {
	const { setSetting } = useContext(SettingCtx);		// aprire le impostazioni
	const { setDialog } = useContext(DialogCtx);	// aprire dialoghi di prova
	const { run, setRun } = useContext(RunCtx);			// mettere in pausa il Gioco

	useEffect( () => setRun(true), []);		// se il run era false diventa true

	/*
		useCallback server per memorizzare l'esecuzione di una funzione
		la funzione viene ricostruita ed rieseguita al cambiamento delle variabili nell'array
		(Come useEffetc)
	*/
	const togglePause = useCallback( ev => {
		if (ev.key === "e"){		// vado in pausa
			setSetting(true);
			setRun(false);
		}

		/*else if (ev.key === 'q') {		// Dialogo di pausa
			setDialog(true);
			setRun(false);
		}*/
	}, [setDialog, setRun, setSetting]);

	// questo probabilmento lo toglierò
	const click = ({x,y}) => {		// stampo x e y di dove tocco
		console.log('click x: ' + x + ' click y: ' + y);
	}

	useEventListener('keydown', togglePause);
	useEventListener('click', click);

	return (
		<GameEngine
			running={run}				// imposto l'esecuzione del gioco con un Boolean Globale
			systems={system}			// Array di funzioni che vengono eseguite in loop
			entities={entities()}	// Entita di gioco
			className='Stage'
		>
			<Options	exit={true} />
			<Dialog /* Per i Dialoghi */ />
			<EnigmaModal /* UI degli enigmi */ />
		</GameEngine>
	)
}

export default Play;