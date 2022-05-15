/*
	Stanza dove si trova il giocatore
	e gestore degli eventi
*/

import { useEffect, useContext } from "react";
import { Image } from "react-bootstrap";

import { EnigmaCtx, RunCtx, RoomNameCtx, DoneCtx } from "../components/components";
import { useEventListener } from "../utils/utils";
import paths from '../paths';		// Percorsi dei png delle Stanze

const Room = ({name, evType}) => {
	const { setEnigma } = useContext(EnigmaCtx);		// queste già le conosciamo
	const { setRoom } = useContext(RoomNameCtx);
	const { setRun } = useContext(RunCtx);
	const { done } = useContext(DoneCtx);

	// Aggiorno lo stato Globale Room al cambiamento della prop event
	useEffect( () => setRoom(name), [name]);

	const attivaEnigma = ev => {
		if (ev.key == 'q') {
			// Evento Enigma
			if ( evType == 'Enigma' ) {
				if ( !done.includes(name) ) {		// se l'enigma non è incluso fra quelli GIA FATTI
					setEnigma(true);		// Apro la UI Enigma
					setRun(false);			// Stoppo il gioco
				} else
					alert('Questo Enigmaa l\'ho già fatto');
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