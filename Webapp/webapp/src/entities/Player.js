// Entita di Prova

import { Image } from "react-bootstrap";

const Player = ({x, y, src}) => {

	return(
		<Image
			style={{
				imageRendering: "pixelated",
				position: "absolute",
				left: x,
				top: y,
				border: '1px solid black'
			}}

			src={src}
		/>
	)
}

export default Player;