// Entita di Prova

import { Image } from "react-bootstrap";

const Player = ({x, y, src}) => {


	return(
		<Image
			style={{
				position: "absolute",
				left: x,
				top: y,
			}}
			width={200}
			height={288}
			src={src}
		/>
	)
}

export default Player;