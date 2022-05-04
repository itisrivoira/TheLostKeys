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
	x += 45;
	y += 65;

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
			case "KeyW":
				col = collision(x, y, name, 'Collisioni').up;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.up ) {
					player.y -= speed;
					u = motion(u, 'up');
					room.event = false;
				} else {
					player.src = require(`../assets/characters/up/${frames[0]}`);
				}

				if (ev) {
					room.event = true;
					room.evType = ev.evType;
				}

				break;

			case "KeyS":
				col = collision(x, y, name, 'Collisioni').down;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.down ) {
					player.y += speed;
					d = motion(d, 'down');
					room.event = false;
				}	else{
					player.src = require(`../assets/characters/down/${frames[0]}`);
				}

				if (ev) {
					room.event = true;
					room.evType = ev.evType;
				}

				break;

			case "KeyA":
				col = collision(x, y, name, 'Collisioni').left;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.left ) {
					player.x -= speed;
					l = motion(l, 'left');
					room.event = false;
				} else{
					player.src = require(`../assets/characters/left/${frames[0]}`);
				}

				if (ev) {
					room.event = true;
					room.evType = ev.evType;
				}

				break;

			case "KeyD":
				col = collision(x, y, name, 'Collisioni').right;
				ev = collision(x, y, name, 'Eventi');

				if ( !col && !ev.right ) {
					player.x += speed;
					r = motion(r, 'right');
					room.event = false;
				} else {
					player.src = require(`../assets/characters/right/${frames[0]}`);
				}

				if (ev) {
					room.event = true;
					room.evType = ev.evType;
				}

				break;
		}
	}

	return entities;
}

export default Loop;