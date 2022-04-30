// Stanza dove si trova il giocatore

import { Image } from "react-bootstrap";

import paths from '../paths';

const Room = ({name}) => {

	return(
		<Image
			src={paths[name].png}
		/>
	)

};

export default Room;