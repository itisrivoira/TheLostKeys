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
			y >= (el.y - el.height - 35)
		) {
			dirs.down = true;
			console.log(`${msg}: ${dirs.down} ${el.id} x: ${x}, y: ${y}`);
		}

		if (
			x >= (el.x - 10) &&
			x <= (el.x + el.width + 10) &&
			y >= (el.y - 30) &&
			y <= (el.y - 10)
		){
			dirs.up = true;
			console.log(`${msg}: ${dirs.up} ${el.id} x: ${x}, y: ${y}`);
		}

		if (
			x >= (el.x - 15) &&
			x <= el.x &&
			y >= (el.y - el.height - 30) &&
			y <= (el.y - 30)
		) {
			dirs.right = true;
			console.log(`${msg}: ${dirs.right} ${el.id} x: ${x}, y: ${y}`);
		}

		if (
			x >= (el.x + el.width) &&
			x <= (el.x + el.width + 10) &&
			y >= (el.y - el.height - 30) &&
			y <= (el.y - 30)
		) {
			dirs.left = true;
			console.log(`${msg}: ${dirs.left} ${el.id} x: ${x}, y: ${y}`);
		}
	})

	return dirs;
}