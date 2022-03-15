// Bottoni
import { useEffect, useState } from "react";
import { Button, Image } from "react-bootstrap";
import { BiMicrophoneOff, BiMicrophone } from "react-icons/bi";

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

export const BtnPlay = () => {
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
			onClick={() => alert('Il gioco inizierà da qui')}
			fluid
		/>
	)
}

export const BtnOptions = () => {
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
			onClick={() => alert('Opzioni')}
			fluid
		/>
	)
}

export const BtnLogin = () => {
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
			onClick={() => alert('Login')}
			fluid
		/>
	)
}

export const BtnMusic = () => {
	const [playing, toggle] = useAudio(rainSound, true);
	const [thunder, setThunder] = useAudio(thunderSound, false);
	const [thunder2, setThunder2] = useAudio(thunderSound2, false);
	const [delay1, setDelay1] = useState([12000, 14000]);
	const [delay2, setDelay2] = useState([7000, 9000]);

	useRandomInterval(() => setThunder(), ...delay1);
	useRandomInterval(() => setThunder2(), ...delay2);

	const toggleAudio = () => {
		toggle();
		if (thunder) setThunder();
		if (thunder2) setThunder2();
	}

	useEffect( () => {
		setDelay1([12000, playing ? 14000 : null]);
		setDelay2([7000, playing ? 9000 : null]);
	}, [playing])

	return(
		<Button variant="secondary" onClick={toggleAudio}>
			{ playing ? <BiMicrophone size={55} /> : <BiMicrophoneOff size={55} />}
		</Button>
	)
}