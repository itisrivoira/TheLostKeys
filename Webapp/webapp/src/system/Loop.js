// Loop del Gioco
import collision from "./collision";

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
	const { player, room } = entities;
	var { name } = room;
	var { x, y, speed } = player;
	x += 40;
	y += 58;

	const motion = (i, direct) => {
		if (i === 5) i = 0;
		player.src = require(`../assets/characters/${direct}/${frames[parseInt(i)]}`);
		i += 0.25;

		return i;
	}

	if (payload) {
		const key = payload.code;
		let [col, ev] = [{}, {}];

		switch (key) {
			case "ArrowUp":
				col = collision(x, y, name, 'Collisioni').up;
				ev = collision(x, y, name, 'Eventi').up;

				if ( !col && !ev ) {
					player.y -= speed;
					u = motion(u, 'up');
				} else {
					player.src = require(`../assets/characters/up/${frames[0]}`);
				}

				break;

			case "ArrowDown":
				col = collision(x, y, name, 'Collisioni').down;
				ev = collision(x, y, name, 'Eventi').down;

				if ( !col && !ev ) {
					player.y += speed;
					d = motion(d, 'down');
				}	else{
					player.src = require(`../assets/characters/down/${frames[0]}`);
				}

				break;

			case "ArrowLeft":
				col = collision(x, y, name, 'Collisioni').left;
				ev = collision(x, y, name, 'Eventi').left;

				if ( !col && !ev ) {
					player.x -= speed;
					l = motion(l, 'left');
				} else{
					player.src = require(`../assets/characters/left/${frames[0]}`);
				}

				break;

			case "ArrowRight":
				col = collision(x, y, name, 'Collisioni').right;
				ev = collision(x, y, name, 'Eventi').right;

				if ( !col && !ev ) {
					player.x += speed;
					r = motion(r, 'right');
				} else {
					player.src = require(`../assets/characters/right/${frames[0]}`);
				}

				break;
		}
	}

	return entities;
}

export default Loop;