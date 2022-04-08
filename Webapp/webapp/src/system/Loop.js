// Loop del Gioco
import { useEffect } from 'react';
import Prova from '../assets/prova/Prova.json';

var [ u, d, l, r ] = [ 0, 0, 0, 0 ]
const frames = [
	'Walk0.png',
	'Walk1.png',
	'Walk2.png',
	'Walk3.png',
	'Walk4.png',
	'Walk5.png',
];

const Loop = (entities, { input }) => {
	const { payload } = input.find(x => x.name === "onKeyDown") || {};
	const player = entities["player"];
	var { x, y, speed } = player;
	x += 27;
	y += 34;

	const motion = (i, direct) => {
		if (i === 5) i = 0;
		player.src = require(`../assets/characters/${direct}/${frames[parseInt(i)]}`);
		i += 0.5;

		return i;
	}

	const collisionUp = () => {
		Prova.layers[1].objects.forEach( el => {
			if ( x >= el.x && x <= (el.x + el.width) && y <= el.y && y >= (el.y - el.height)) {
				console.log('Collisione');
			}
		});
	}

	if (payload) {
		const key = payload.code;

		switch (key) {
			case "ArrowUp":
				player.y -= speed;
				u = motion(u, 'up');
				collisionUp();
				break;

			case "ArrowDown":
				player.y += speed;
				d = motion(d, 'down');
				collisionUp();
				break;

			case "ArrowLeft":
				player.x -= speed;
				l = motion(l, 'left');
				collisionUp();
				break;

			case "ArrowRight":
				player.x += speed;
				r = motion(r, 'right');
				collisionUp();
				break;
		}
	}

	return entities;
}

export default Loop;