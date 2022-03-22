// Bottoni del menu Principale

import { useEffect, useState } from "react";
import { Button, Image } from "react-bootstrap";
import { MdMusicNote, MdMusicOff } from "react-icons/md";

import '../style/App.css';

import { useAudio } from "../utils/useAudio";
import useRandomInterval from "../utils/useRandomTimer";

import rainSound from "../assets/sounds/Rain-sound.mp3";
import thunderSound from "../assets/sounds/thunder-sound.mp3";
import thunderSound2 from "../assets/sounds/thunder-sound2.mp3";
import penPlay from "../assets/img/penPlay.png";
import penOptions from "../assets/img/penOptions.png";
import penLogin from "../assets/img/penLogin.png";
import penPlayWhite from "../assets/img/penPlayWhite.png";
import penOptionsWhite from "../assets/img/penOptionsWhite.png";
import penLoginWhite from "../assets/img/penLoginWhite.png";

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
	const [playing, toggle] = useAudio(rainSound, true);
	const [thunder, setThunder] = useAudio(thunderSound, false);
	const [thunder2, setThunder2] = useAudio(thunderSound2, false);
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

	return(
		<Button variant="secondary" onClick={toggleAudio}>
			{ playing ? <MdMusicNote size={55} /> : <MdMusicOff size={55} />}
		</Button>
	)
}