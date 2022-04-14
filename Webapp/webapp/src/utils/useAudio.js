// hooks per la gestione degli audio

import { useState, useEffect, useContext } from "react";
import { Music, Sfx } from "../components/components";

const useAudio = (url, loop) => {
	const [audio] = useState(new Audio(url));
	const [playing, setPlaying] = useState(false);

	const { music } = useContext(Music);
	const { sfx } = useContext(Sfx);

	const toggle = () => setPlaying(!playing);
	const pause = () => audio.pause();

	useEffect(() => {
		playing ? audio.play() : audio.pause();
	}, [playing]);

	useEffect(() => {
		audio.loop = loop;
		audio.addEventListener('ended', () => setPlaying(false));
		return () => {
			audio.removeEventListener('ended', () => setPlaying(false));
	 	};
	}, []);

	useEffect( () => {
		audio.volume = loop ? music : sfx;
	}, [music, sfx])

	return [playing, toggle, pause];
};

export default useAudio;