// Hooks per la gestione degli audio
// Restuisce un Boolean che indica se è in riproduzione o meno
// Una funzione per attivare/disattivare
// Una funzione per metter in pausa

import { useState, useEffect, useContext } from "react";
import { MusicCtx, SfxCtx } from "../components/components";

const useAudio = (url, loop) => {
	const [audio] = useState(new Audio(url));
	const [playing, setPlaying] = useState(false);

	// Ottengo i livelli della musica e SFX
	const { music } = useContext(MusicCtx);
	const { sfx } = useContext(SfxCtx);

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

	// Se Loop è vero considero il volume della musica, altrimento quello dei SFX
	useEffect( () => {
		audio.volume = loop ? music : sfx;
	}, [music, sfx])

	return [playing, toggle, pause];
};

export default useAudio;