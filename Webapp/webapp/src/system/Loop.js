// Loop del Gioco
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

	const motion = (i, direct) => {
		if (i === 5) i = 0;
		player.src = require(`../assets/characters/${direct}/${frames[parseInt(i)]}`);
		i += 0.5;

		return i;
	}

	const collisionUp = () => {
		Prova.layers[1].objects.forEach( el => {
			if (y >= el.y && y <= (el.y + el.width) && x == parseInt(el.x)) {
				console.log('Collisione');
			}

		});

	}



	if (payload) {
		const key = payload.code;
		console.log('x: ' + x);
		console.log('y: ' + y);

		switch (key) {
			case "ArrowUp":
				player.y -= speed;
				u = motion(u, 'up');
				break;

			case "ArrowDown":
				player.y += speed;
				d = motion(d, 'down');
				break;

			case "ArrowLeft":
				player.x -= speed;
				l = motion(l, 'left');
				break;

			case "ArrowRight":
				player.x += speed;
				r = motion(r, 'right');
				break;
		}
	}

	return entities;
}

export default Loop;