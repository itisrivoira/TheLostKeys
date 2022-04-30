// collision or event checker

export default (elem, x, y,msg) => {
	let dirs = {
		down: false,
		up: false,
		right: false,
		left: false
	};

	elem.forEach( el => {
		if (
			x >= (el.x - 10) &&
			x <= (el.x + el.width + 10) &&
			y <= (el.y - el.height) &&
			y >= (el.y - el.height - 40)
		) {
			dirs.down = true;
			console.log(`${msg}: down ${el.id} x: ${x}, y: ${y}`);
		}

		if (
			x >= (el.x - 10) &&
			x <= (el.x + el.width + 10) &&
			y >= (el.y - 40) &&
			y <= (el.y - 15)
		){
			dirs.up = true;
			console.log(`${msg}: up ${el.id} x: ${x}, y: ${y}`);
		}

		if (
			x >= (el.x - 20) &&
			x <= el.x &&
			y >= (el.y - el.height - 30) &&
			y <= (el.y - 30)
		) {
			dirs.right = true;
			console.log(`${msg}: right ${el.id} x: ${x}, y: ${y}`);
		}

		if (
			x >= (el.x + el.width) &&
			x <= (el.x + el.width + 15) &&
			y >= (el.y - el.height - 30) &&
			y <= (el.y - 30)
		) {
			dirs.left = true;
			console.log(`${msg}: left ${el.id} x: ${x}, y: ${y}`);
		}
	})

	return dirs;
}