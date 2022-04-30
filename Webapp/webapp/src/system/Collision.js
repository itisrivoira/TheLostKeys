// Collision or Event Detector;
import check from "./check";
import paths from "../paths";

export default (x, y, room, name) => {
	const Scheme = paths[room].json;
	var direction = {};

	Scheme.layers.forEach( el => {
		if (el.name == name)
			direction = check(el.objects, x, y, name);
	});

	return direction;
}