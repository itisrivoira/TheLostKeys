// Loop del Gioco

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

	if (payload) {
		const key = payload.code;

		switch (key) {
			case "ArrowUp":
				player.y -= player.speed;
				if (u === 5) u = 0;
				player.src = require('../assets/characters/up/' + frames[u]);
				u++;
				break;

			case "ArrowDown":
				player.y += player.speed;
				if (d === 5) d = 0;
				player.src = require('../assets/characters/down/' + frames[d]);
				d++;
				break;

			case "ArrowLeft":
				player.x -= player.speed;
				if (l === 5) l = 0;
				player.src = require('../assets/characters/left/' + frames[l]);
				l++;
				break;

			case "ArrowRight":
				player.x += player.speed;

				if (r === 5) r = 0;
				player.src = require('../assets/characters/right/' + frames[r]);
				r++;

				break;
		}
	}

	return entities;
}

export default Loop;