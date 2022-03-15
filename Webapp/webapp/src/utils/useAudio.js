// hooks per la gestione degli audio

import { useState, useEffect } from "react";

export const useAudio = (url, loop) => {
	const [audio] = useState(new Audio(url));
	const [playing, setPlaying] = useState(false);

	const toggle = () => setPlaying(!playing);

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

	return [playing, toggle];
 };