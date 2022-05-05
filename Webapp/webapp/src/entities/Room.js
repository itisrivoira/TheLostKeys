// Stanza dove si trova il giocatore

import { useEffect, useContext } from "react";
import { Image } from "react-bootstrap";

import { Enigma, Run, RoomName } from "../components/components";
import { useEventListener } from "../utils/utils";
import paths from '../paths';		// Percorsi dei png delle Stanze

const Room = ({name, event, evType, evOptions}) => {
	const { setEnigma } = useContext(Enigma);		// queste già le conosciamo
	const { setRoom } = useContext(RoomName);
	const { setRun } = useContext(Run);

	// Aggiorno lo stato Globale Room al cambiamento della prop event
	useEffect( () => setRoom(name), [name]);

	// Cambierò il tasto Z con probabilmente Q
	const attivaEnigma = ev => {
		if (ev.key == 'z') {
			// Evento Enigma
			if ( event && evType == 'Enigma' ) {
				setEnigma(true);
				setRun(false);		// Stoppo il gioco
			} else if ( event && evType == 'Dialog' ) {
				alert('Questo è un dialogo!');
			} else if ( event && evType =='Door' ) {
				// Questo evento lo sposterò da qui perchè inutile
				alert('Qui cambierò stanza!');
			}
		}
	};

	useEventListener('keydown', attivaEnigma);

	return(
		<Image
			draggable={false}		// per evitare che l'utente possa trascinare lo sfondo
			src={paths[name].png}		// Lo sfondo sarà il png della stanza 'name' contenuta nell'Object paths
		/>
	)
}

export default Room;