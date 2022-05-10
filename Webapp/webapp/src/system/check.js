// Collision or event checker
// Controllo se collido con qualsiasi cosa
// Nel caso dell'evento ritorno anche altri parametri

// Elem è l'array di Object da girare (Collisioni livello Oggetto di Tiled)
// guarda i file json per capire meglio: assets/rooms/json/
// x e y sono le coordinate del giocatore nel suo punto medio (al centro)
// msg è solo di debug
export default (elem, x, y, msg) => {
	let dirs = {
		down: false,	// giù
		up: false,		// su
		right: false,	// destra
		left: false,	// sinistra

		evType: '',		// Tipo evento
		options: {}		// Opzioni Evento
	};

	elem.forEach( el => {
		// Ricordiamoci che el.x ed el.y sono il vertice in basso a sinistra dell'oggetto (non il centro!)
		// Collisioni verso il basso
		if (
			x >= (el.x - 10) &&				// X deve essere compresa tra destra e sinistra
			x <= (el.x + el.width + 10) &&
			y <= (el.y - el.height) &&		// Y deve essere vicina al lato alto (quello superiore) o più in alto
			y >= (el.y - el.height - 50)
		) {
			dirs.down = true;
			console.log(`${msg}: down ${el.id} x: ${x}, y: ${y}`);	// Log di debug

			// Se verifico un evento ritorno i parametri di quell'evento
			if (msg == 'Eventi') {
				dirs.evType = el.evType;
				dirs.options = el.options;
			}
		}

		// Collisioni verso l'alto
		if (
			x >= (el.x - 10) &&		// X deve essere compresa tra destra e sinistra
			x <= (el.x + el.width + 10) &&
			y >= (el.y - 50) &&		// Y deve essere vicina al lato basso (inferiore) o più in alto
			y <= (el.y - 20)			// Questo per dare un effetto 3D del giocatore
		){
			dirs.up = true;
			console.log(`${msg}: up ${el.id} x: ${x}, y: ${y}`);

			if (msg == 'Eventi') {
				dirs.evType = el.evType;
				dirs.options = el.options;
			}
		}

		/*
			FOCUS:
			Collisione verso l'alto: collido con il lato inferiore ma verso l'alto
			Collisione verso il basso: collido con il lato superiore ma verso il basso
			Collisione verso destra: collido con il lato sinistro ma verso destra
			Collisione verso sinistra: collido con il lato destro ma verso sinistra
			Attenti a non confondervi
		*/

		// Collisioni verso destra
		if (
			x >= (el.x - 25) &&		// X deve essere vicina al lato sinistro o più verso sinistra
			x <= el.x &&
			y >= (el.y - el.height - 40) &&		// Y deve essere compresa nell'altezza dell'oggeto
			y <= (el.y - 40)				// ma translata di 30 px verso l'alto per dare l'effetto 3D
		) {
			dirs.right = true;
			console.log(`${msg}: right ${el.id} x: ${x}, y: ${y}`);

			if (msg == 'Eventi') {
				dirs.evType = el.evType;
				dirs.options = el.options;
			}
		}

		// Collisioni verso sinistra
		if (
			x >= (el.x + el.width) &&			// X deve essere vicina al lato destro o più verso destra
			x <= (el.x + el.width + 25) &&
			y >= (el.y - el.height - 40) && 	// Y deve essere compresa nell'altezza dell'oggeto
			y <= (el.y - 40)		// ma translata di 30 px verso l'alto per dare l'effetto 3D
		) {
			dirs.left = true;
			console.log(`${msg}: left ${el.id} x: ${x}, y: ${y}`);

			if (msg == 'Eventi') {
				dirs.evType = el.evType;
				dirs.options = el.options;
			}
		}
	})

	return dirs;
}