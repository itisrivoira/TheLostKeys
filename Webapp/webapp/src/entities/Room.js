// Stanza dove si trova il giocatore

import { Image } from "react-bootstrap";

const Room = ({name}) => {

	return(
		<Image
			src={require(`../assets/rooms/png/${name}.png`)}
			style={{
				backgroundPosition: '50%',
				overflow: "hidden",
			}}
		/>
	)

};

export default Room;