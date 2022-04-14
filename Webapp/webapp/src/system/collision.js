import ChimicaProva from '../assets/prova/ChimicaProva.json';

export default (x, y) => {
	let direction = '';

	ChimicaProva.layers[2].objects.forEach( el => {
		if (
			x >= (el.x - 10) &&
			x <= (el.x + el.width + 10) &&
			y <= (el.y - el.height) &&
			y >= (el.y - el.height - 27)
		) direction = 'down';

		if (
			x >= (el.x - 10) &&
			x <= (el.x + el.width + 10) &&
			y >= el.y &&
			y <= (el.y + 17)
		) direction = 'up';

		if (
			y >= (el.y - el.height) &&
			y <= el.y &&
			x <= el.x &&
			x >= (el.x - 11)
		) direction = 'right';

		if (
			y >= (el.y - el.height) &&
			y <= el.y &&
			x >=( el.x + el.width) &&
			x <= (el.x + el.width + 10)
		) direction = 'left';
	});

	return direction;
}