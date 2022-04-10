// Loop del Gioco
import Prova from '../assets/prova/Prova.json';

var [ u, d, l, r ] = [ 0, 0, 0, 0 ];
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

	const collision = () => {
		Prova.layers[1].objects.forEach( el => {
			if (
				x >= (el.x - 10) &&
				x <= (el.x + el.width + 10) &&
				y <= (el.y + 20) &&
				y >= (el.y - el.height - 20)
			) {
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
				collision();
				break;

			case "ArrowDown":
				player.y += speed;
				d = motion(d, 'down');
				collision();
				break;

			case "ArrowLeft":
				player.x -= speed;
				l = motion(l, 'left');
				collision();
				break;

			case "ArrowRight":
				player.x += speed;
				r = motion(r, 'right');
				collision();
				break;
		}
	}

	return entities;
}

export default Loop;