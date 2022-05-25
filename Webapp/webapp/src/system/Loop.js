/*
	Loop del Gioco
	Funzione che fa muovere il giocatore
*/

import collision from "./collision";
import Player from "../entities/Player";
import Room from "../entities/Room";

// Indicatori di frame nelle 4 direzioni
var [ u, d, l, r ] = [ 0, 0, 0, 0 ];
const frames = [	// nomi degli sprite di movimento
	'Walk0.png',
	'Walk1.png',
	'Walk2.png',
	'Walk3.png',
	'Walk4.png',
	'Walk5.png',
];

const Loop = (entities, { input }) => {
	// payload è l'oggetto ritornato quando un evento si verifica
	const { payload } = input.find(x => x.name === "onKeyDown") || {};
	// Estraggo le entità player e room definite nel file entities.js
	const { player, room, uhd } = entities;

	// Estraggo varie proprietà dalle entita per comodità
	var { x, y, speed, pg } = player;
	var { name } = room;

	// Smezzo le coordinate del giocatore per ottenere il punto medio
	x += 45;
	y += 65;

	// funzione che anima lo sprite di movimento
	// Questa funzione cambierà quando aggiugerò più personaggi
	const move = (i, direct) => {
		if (i === 5) i = 0;		// se il contatore arriva al massimo lo resetto
		// ogni 4 click cambio immagine dove direct=direzione e frame=numero della animazione
		player.src = require(`../assets/characters/${pg}/${direct}/${frames[parseInt(i)]}`);
		// aumento di un 1/4 per ritardare l'animazione e renderla più fluida
		i += 0.25;

		// ritorno il valore perchè il contatore viene passato alla funzione per valore
		// quindi si modifica solo una copia
		return i;
	}

	// funzione per caricare lo sprite del pg fermo
	const stop = direct => {
		player.src = require(`../assets/characters/${pg}/${direct}/Walk0.png`);
	};

	// Quando l'evento si verifica faccio muovere il giocatore
	if (payload) {
		const key = payload.code;		// Lettera tasto premuto
		let [col, ev] = [{}, {}];		// col ed ev sono Object che indicano le direzioni in cui collide il giocatore

		switch (key) {
			case "KeyW":
				col = collision(x, y, name, 'Collisioni').up;		// prendo solo la proprietà up
				ev = collision(x, y, name, 'Eventi');			// qui invece mi servono tutte le proprietà

				if ( !col && !ev.up ) {		// Se entrambi sono falsi posso andare avanti
					player.y -= speed;		// Diminuisco perchè le Y crescono verso il basso
					u = move(u, 'up');		// Animazione
				} else 		// Se invece non posso muovermi carico lo sprite da fermo
					stop('up');

				if (ev.evType != '') 	// Se c'è l'evento
					room.evType = ev.evType;	// Mi salvo il tipo di evento
				else
					room.evType = '';

				break;

			case "KeyS":
				col = collision(x, y, name, 'Collisioni').down;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.down ) {
					player.y += speed;
					d = move(d, 'down');
				} else
					stop('down');

				if (ev.evType != '')
					room.evType = ev.evType;
				else
					room.evType = '';

				break;

			case "KeyA":
				col = collision(x, y, name, 'Collisioni').left;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.left ) {
					player.x -= speed;
					l = move(l, 'left');
				} else
					stop('left');

				if (ev.evType != '')
					room.evType = ev.evType;
				else
					room.evType = '';

				break;

			case "KeyD":
				col = collision(x, y, name, 'Collisioni').right;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.right ) {
					player.x += speed;
					r = move(r, 'right');
				} else
					stop('right');

				if (ev.evType != '')
					room.evType = ev.evType;
				else
					room.evType = '';

				break;

			case "KeyQ":
				ev = collision(x, y, name, 'Eventi');

				// Cambio stanza
				if (ev.evType == 'Door') {
					// imposto un ritardo per non uccidere i miei occhi
					setTimeout(() => {
						room.renderer = null;		// nascondo lo sfondo e il giocatore
						player.renderer = null;
					}, 300);

					// cambio stanza e sposto il giocatore dopo quasi un secondo
					setTimeout( () => {
						room.name = ev.options.dest;	// cambio name cioè la stanza
						player.x = ev.options.nextX;	// cambio le coordinate del giocatore
						player.y = ev.options.nextY;

						room.renderer = <Room/>;		// mostro lo sfondo e il giocatore
						player.renderer = <Player />;

						const direction = ev.options.direction;		// direzione in cui il giocatore sarà rivolto
						stop(direction);
					}, 600);
				}

				if (ev.evType == 'FinalDoor') {
					let done = JSON.parse(sessionStorage.getItem('done'));
					if (done.length >= 13)
						room.name = "Archivio1";
				}

				if (ev.evType == 'Win')
					uhd.gameWin = true;

				break;
		}
	}

	// ritorno le entità per renderle disponibili ai prossimi richiami
	return entities;
}

export default Loop;