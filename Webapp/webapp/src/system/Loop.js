// Loop del Gioco

const Loop = (entities, { input }) => {

	const { payload } = input.find( x => x.name === "onKeyDown") || {};

	if (payload) {
		const box1 = entities["box1"];
		const key = payload.code;

		switch (key) {
			case "ArrowUp":
				box1.y -= box1.speed;
				break;

			case "ArrowDown":
				box1.y += box1.speed;
				break;

			case "ArrowLeft":
				box1.x -= box1.speed;
				break;

			case "ArrowRight":
				box1.x += box1.speed;
				break;

			default:
				break;
		}
	}

	return entities;
}

export default Loop;