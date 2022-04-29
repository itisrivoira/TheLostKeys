// Collision or Event Detector;
import check from "./check";

export default (x, y, room, name) => {
	const Scheme = require(`../assets/rooms/json/${room}.json`);
	var direction = {};

	Scheme.layers.forEach( el => {
		if (el.name == name)
			direction = check(el.objects, x, y, 'Collisione ');
	});

	return direction;
}