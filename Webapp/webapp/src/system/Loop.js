// Loop del Gioco
import collision from "./Collision";

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
	const room = entities["room"];
	var { name } = room;
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
				if (collision(x,y, name) != 'up') {
					player.y -= speed;
					u = motion(u, 'up');
				} else {
					console.log('up')
					player.src = require(`../assets/characters/up/${frames[0]}`);}

				break;

			case "ArrowDown":
				if (collision(x,y, name) != 'down') {
					player.y += speed;
					d = motion(d, 'down');
				}	else
			{	console.log('down')
					player.src = require(`../assets/characters/down/${frames[0]}`);}

				break;

			case "ArrowLeft":
				if (collision(x,y, name) != 'left') {
					player.x -= speed;
					l = motion(l, 'left');
				} else{
				console.log('left')
					player.src = require(`../assets/characters/left/${frames[0]}`);}

				break;

			case "ArrowRight":
				if (collision(x,y, name) != 'right') {
					player.x += speed;
					r = motion(r, 'right');
				} else
				{console.log('right')
					player.src = require(`../assets/characters/right/${frames[0]}`);}

				break;
		}
	}

	return entities;
}

export default Loop;