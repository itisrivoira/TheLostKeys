// Bottoni del menu Principale

import { useEffect, useState } from "react";
import { Button, Image } from "react-bootstrap";
import { MdMusicNote, MdMusicOff } from "react-icons/md";

import { useAudio, useRandomInterval } from '../utils/utils';		// Custom Hooks che facilitano il lavoro
import { penPlay, penOptions, penRank, penPlayWhite, penRankWhite, penOptionsWhite } from '../assets/img/img';
import { rainSound, thunderSound, thunderSound2 } from '../assets/sounds/sounds';

import '../style/Menu.css';

/*
	Questo componente fa da Bottone Generico
	Lo utilizzo negli altri tre bottoni
	Così evito di creare altri componenti e codice unico
*/

const Btn = ({callback, enterSrc, leaveSrc}) => {
	const [state, setState] = useState(false);	// stato per la transizione grafica

	const enter = () => setState(true);		// attiva la scritta bianca
	const leave = () => setState(false);	// disattiva la scritta bianca

	return(
		<Image
			src={state ? enterSrc : leaveSrc}	// se lo stato è true mi attiva la scritta bianca altrimenti la resetta
			onMouseEnter={enter}
			onMouseLeave={leave}
			height={175}
			width={325}
			onClick={callback}
			style={{imageRendering: "pixelated"}}
			fluid
		/>
	)
};

export const BtnPlay = ({callback}) => (	// la callback è la funzione da eseguire al click
	<Btn
		callback={callback}
		enterSrc={penPlayWhite}
		leaveSrc={penPlay}
	/>
)

export const BtnOptions = ({callback}) =>(
	<Btn
		callback={callback}
		enterSrc={penOptionsWhite}
		leaveSrc={penOptions}
	/>
)

export const BtnRank = ({callback}) => (
	<Btn
		callback={callback}
		enterSrc={penRankWhite}
		leaveSrc={penRank}
	/>
)

// Questo Bottone Attiva o Disattiva la musica
export const BtnMusic = () => {
	/*
		useAudio è un custom Hook molto utile per la gestione della musica
		dato la sorgente della musica e il Boolean per il loop
		mi ritorna un Bool e la funzione per attivare e mettere in pausa la musica
	*/

	const [playing, toggle, pause] = useAudio(rainSound, true);					// pioggia
	const [thunder, setThunder, pause1] = useAudio(thunderSound, false);		// Primo Fulmine
	const [thunder2, setThunder2, pause2] = useAudio(thunderSound2, false);	// Secondo Fulmine
	const [delay1, setDelay1] = useState([8000, 13000]);		// intervallo di tempo per attivare i fulmini
	const [delay2, setDelay2] = useState([4000, 8000]);

	// useRandomInterval mi attiva i fulmini a caso nell'intervallo di tempo stabilito
	useRandomInterval(() => setThunder(), ...delay1);
	useRandomInterval(() => setThunder2(), ...delay2);

	// attivo o disattivo la musica
	const toggleAudio = () => {
		toggle();
		if (thunder) setThunder();
		if (thunder2) setThunder2();
	}

	// Server per disattivare lo useRandomInterval
	useEffect( () => {
		setDelay1([8000, playing ? 13000 : null]);
		setDelay2([4000, playing ? 8000 : null]);
	}, [playing]);

	// quando esco dalla home Page devo disattivare la pioggia e i fulmini
	useEffect( () => {
		return () => {
			pause();
			pause1();
			pause2();
		}
	}, []);

	return(
		<Button variant="secondary" onClick={toggleAudio}>
			{ playing ? <MdMusicNote size={55} /> : <MdMusicOff size={55} />}
		</Button>
	)
}