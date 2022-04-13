// Loop del Gioco

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
	const { player } = entities;
	var { x, y, speed } = player;
	x += 27;
	y += 34;

	const motion = (i, direct) => {
		if (i === 5) i = 0;
		player.src = require(`../assets/characters/${direct}/${frames[parseInt(i)]}`);
		i += 0.25;

		return i;
	}

	if (payload) {
		const key = payload.code;

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