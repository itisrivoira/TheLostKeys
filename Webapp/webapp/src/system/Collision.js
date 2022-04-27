// collisioni

export default (x, y, name) => {
	const Scheme = require(`../assets/rooms/json/${name}.json`);
	let direction = '';

	let check = (elem, msg) => {
		elem.forEach( el => {
			if (
				x >= (el.x - 10) &&
				x <= (el.x + el.width + 10) &&
				y <= (el.y - el.height) &&
				y >= (el.y - el.height - 27)
			) {direction = 'down'; console.log(msg + el.id + ' x: ' + x + ' y: ' + y)};

			if (
				x >= (el.x - 10) &&
				x <= (el.x + el.width + 10) &&
				y >= el.y &&
				y <= (el.y + 17)
			){ direction = 'up'; console.log(msg + el.id + ' x: ' + x + ' y: ' + y)};

			if (
				y >= (el.y - el.height) &&
				y <= el.y &&
				x <= el.x &&
				x >= (el.x - 11)
			) {direction = 'right'; console.log(msg + el.id + ' x: ' + x + ' y: ' + y)};

			if (
				y >= (el.y - el.height) &&
				y <= el.y &&
				x >=( el.x + el.width) &&
				x <= (el.x + el.width + 10)
			) {direction = 'left'; console.log(msg + el.id + ' x: ' + x + ' y: ' + y)};
		})
	}


	Scheme.layers.forEach( el => {
		if (el.name == 'Collisioni')
			check(el.objects, 'Collisione ');

		if (el.name == 'Eventi')
			check(el.objects, 'Evento ');

	});

	return direction;
}