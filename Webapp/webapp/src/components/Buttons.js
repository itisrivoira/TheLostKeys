// Bottoni del menu Principale

import { useEffect, useState } from "react";
import { Button, Image } from "react-bootstrap";
import { MdMusicNote, MdMusicOff } from "react-icons/md";

import {useAudio, useRandomInterval} from '../utils/utils';
import { penPlay, penOptions, penLogin, penPlayWhite, penLoginWhite, penOptionsWhite } from '../assets/img/img';
import { rainSound, thunderSound, thunderSound2 } from '../assets/sounds/sounds';

import '../style/App.css';

const Btn = ({callback, enterSrc, leaveSrc}) => {
	const [state, setState] = useState(false);	// stato per la transizione grafica

	const enter = () => setState(true);
	const leave = () => setState(false);

	return(
		<Image
			src={state ? enterSrc : leaveSrc}
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

export const BtnPlay = ({callback}) => (
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

export const BtnLogin = ({callback}) => (
	<Btn
		callback={callback}
		enterSrc={penLoginWhite}
		leaveSrc={penLogin}
	/>
)

export const BtnMusic = () => {
	const [playing, toggle, pause] = useAudio(rainSound, true);
	const [thunder, setThunder, pause1] = useAudio(thunderSound, false);
	const [thunder2, setThunder2, pause2] = useAudio(thunderSound2, false);
	const [delay1, setDelay1] = useState([8000, 13000]);
	const [delay2, setDelay2] = useState([4000, 8000]);

	useRandomInterval(() => setThunder(), ...delay1);
	useRandomInterval(() => setThunder2(), ...delay2);

	const toggleAudio = () => {
		toggle();
		if (thunder) setThunder();
		if (thunder2) setThunder2();
	}

	useEffect( () => {
		setDelay1([8000, playing ? 13000 : null]);
		setDelay2([4000, playing ? 8000 : null]);
	}, [playing])

	useEffect( () => {
		return () => {
			pause();
			pause1();
			pause2();
		}
	}, [])

	return(
		<Button variant="secondary" onClick={toggleAudio}>
			{ playing ? <MdMusicNote size={55} /> : <MdMusicOff size={55} />}
		</Button>
	)
}