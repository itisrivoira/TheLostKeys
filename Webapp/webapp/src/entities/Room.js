/*
	Stanza dove si trova il giocatore
	e gestore degli eventi
*/

import { useEffect, useContext } from "react";
import { Image } from "react-bootstrap";

import { Enigma, Run, RoomName, Done } from "../components/components";
import { useEventListener } from "../utils/utils";
import paths from '../paths';		// Percorsi dei png delle Stanze

const Room = ({name, event, evType, evOptions}) => {
	const { setEnigma } = useContext(Enigma);		// queste già le conosciamo
	const { setRoom } = useContext(RoomName);
	const { setRun } = useContext(Run);
	const { done } = useContext(Done);

	// Aggiorno lo stato Globale Room al cambiamento della prop event
	useEffect( () => setRoom(name), [name]);

	// Cambierò il tasto Z con probabilmente Q
	const attivaEnigma = ev => {
		if (ev.key == 'q') {
			// Evento Enigma
			if ( event && evType == 'Enigma' ) {
				if ( !done.includes(name) ) {		// se l'enigma non è incluso fra quelli GIA FATTI
					setEnigma(true);		// Apro la UI Enigma
					setRun(false);			// Stoppo il gioco
				} else
					alert('Questo Enigmaa l\'ho già fatto');

			} else if ( event && evType == 'Dialog' ) {
				console.log('Questo è un dialogo!');
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