// Stanza dove si trova il giocatore

import { useEffect, useState, useContext } from "react";
import { Image } from "react-bootstrap";

import { Enigma, Run, RoomName } from "../components/components";
import { useEventListener } from "../utils/utils";
import paths from '../paths';

const Room = ({name, event, evType, evOptions}) => {
	const { setEnigma } = useContext(Enigma);
	const { setRoom } = useContext(RoomName);
	const { setRun } = useContext(Run);
	const [state, setState] = useState(event);

	useEffect( () => setState(event), [event]);
	useEffect( () => setRoom(name), [name]);

	const attivaEnigma = ev => {
		if (ev.key == 'z') {
			if ( event && evType == 'Enigma' ) {
				setEnigma(true);
				setRun(false);
			} else if ( event && evType == 'Dialog' ) {
				alert('Questo è un dialogo!');
			} else if ( event && evType =='Door' ) {
				alert('Qui cambierò stanza!');
			}
		}
	}

	useEventListener('keydown', attivaEnigma);

	return(
		<Image
			src={paths[name].png}
		/>
	)
}

export default Room;