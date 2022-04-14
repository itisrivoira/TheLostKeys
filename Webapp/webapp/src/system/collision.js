import ChimicaProva from '../assets/prova/ChimicaProva.json';

export default (x, y) => {
	let direction = '';

	ChimicaProva.layers[2].objects.forEach( el => {
		const collX = x >= (el.x - 10);
		const collY = y >= (el.y - el.height);

		if (
			collX &&
			x <= (el.x + el.width + 10) &&
			y <= (el.y - el.height) &&
			y >= (el.y - el.height - 27)
		) direction = 'down';

		if (
			collX &&
			x <= (el.x + el.width + 10) &&
			y >= el.y &&
			y <= (el.y + 17)
		) direction = 'up';

		if (
			collY &&
			y <= el.y &&
			x <= el.x &&
			x >= (el.x - 11)
		) direction = 'right';

		if (
			collY &&
			y <= el.y &&
			x >=( el.x + el.width) &&
			x <= (el.x + el.width + 10)
		) direction = 'left';
	});

	return direction;
}