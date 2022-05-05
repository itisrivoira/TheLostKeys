/*
	Collision or Event Detector;
	Questo file richiama check.js per controllare le collisioni
	una volta nelle Collisioni vere e proprie
	una altra per gli eventi
*/

import check from "./check";
import paths from "../paths";

export default (x, y, room, name) => {
	const Scheme = paths[room].json;		// JSON da girare compreso nel file paths e indicato dal nome della stanza
	var direction = {};		// direzioni in cui il giocatore collide

	Scheme.layers.forEach( el => {
		if (el.name == name)
			direction = check(el.objects, x, y, name);
	});

	return direction;
}