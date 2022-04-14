// Bottoni del menu Principale

import { useEffect, useState } from "react";
import { Button, Image } from "react-bootstrap";
import { MdMusicNote, MdMusicOff } from "react-icons/md";

import {useAudio, useRandomInterval} from '../utils/utils';
import { penPlay, penOptions, penLogin, penPlayWhite, penLoginWhite, penOptionsWhite } from '../assets/img/img';
import { rainSound, thunderSound, thunderSound2 } from '../assets/sounds/sounds';

import '../style/App.css';

export const BtnPlay = ({callback}) => {
	const [state, setState] = useState(false);	// stato per la transizione

	const enter = () => setState(true);
	const leave = () => setState(false);

	return(
		<Image
			src={state ? penPlayWhite: penPlay}
			onMouseEnter={enter}
			onMouseLeave={leave}
			height={175}
			width={325}
			onClick={callback}
			fluid
		/>
	)
}

export const BtnOptions = ({callback}) => {
	const [state, setState] = useState(false);

	const enter = () => setState(true);
	const leave = () => setState(false);

	return(
		<Image
			src={state ? penOptionsWhite : penOptions}
			onMouseEnter={enter}
			onMouseLeave={leave}
			height={175}
			width={325}
			onClick={callback}
			fluid
		/>
	)
}

export const BtnLogin = ({callback}) => {
	const [state, setState] = useState(false);

	const enter = () => setState(true);
	const leave = () => setState(false);

	return(
		<Image
			src={state ? penLoginWhite : penLogin}
			onMouseEnter={enter}
			onMouseLeave={leave}
			height={175}
			width={325}
			onClick={callback}
			fluid
		/>
	)
}

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