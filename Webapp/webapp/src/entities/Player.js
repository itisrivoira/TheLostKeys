// Entita di Prova

import { useEffect } from "react";
import { Image } from "react-bootstrap";

const Player = ({x, y, src}) => {

	useEffect( () => console.log('x: ' + x), [x]);
	useEffect( () => console.log('y: ' + y), [y]);

	return(
		<Image
			style={{
				imageRendering: "pixelated",
				position: "absolute",
				left: x,
				top: y,
			}}
			width={150}
			height={212}
			src={src}
		/>
	)
}

export default Player;