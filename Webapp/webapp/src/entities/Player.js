// Entita di Prova

import { useContext } from "react";
import { Image } from "react-bootstrap";

import {Enigma} from '../components/components';
import ProvaChimica from '../assets/prova2/ProvaChimica.json';
import useEventListener from "../utils/useEventListener";

const Player = ({x, y, src}) => {
	const { setEnigma } = useContext(Enigma);


	const evento = e => {
		if (e.key === 'z' ) {
			ProvaChimica.layers[4].objects.forEach( el => {
				if (el.evType == 'enigma') {
					setEnigma(true);
				}
			})
		}
	}

	useEventListener('keydown', evento);

	return(
		<Image
			style={{
				imageRendering: "pixelated",
				position: "absolute",
				left: x,
				top: y,
			}}
			width={75}
			height={105}
			src={src}
		/>
	)
}

export default Player;