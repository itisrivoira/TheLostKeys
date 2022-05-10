// Giocatore che si muove nelle stanze

import { Image } from "react-bootstrap";

// Queste prop vengono passate ogni 16ms dal GameEngine
const Player = ({x, y, src}) => {

	return(
		<Image
			style={{
				imageRendering: "pixelated",
				position: "absolute",
				left: x,		// distanza tra l'img e il lato sinistro
				top: y,		// distanza tra l'img e il lato destro
			}}
			width={100}
			height={144}
			src={src}
		/>
	)
}

export default Player;