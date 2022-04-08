// Entita di Prova

import { useEffect } from "react";
import { Image } from "react-bootstrap";

const Player = ({x, y, src}) => {

	//useEffect( () => console.log('x: ' + parseInt(x + 27)));
	//useEffect( () => console.log('y: ' + parseInt(y + 34)));

	return(
		<Image
			style={{
				position: "absolute",
				left: x,
				top: y,
				border: '1px solid black',
			}}
			src={src}
		/>
	)
}

export default Player;