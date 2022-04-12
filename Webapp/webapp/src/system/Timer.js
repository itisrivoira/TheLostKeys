// Funzione per il countdown

var n = 0.5;

const Timer = (entities) => {
	const { countdown } = entities;

	n++;

	if (n == 62.5) {
		countdown.sec -= 1;
		n = 0.5;

		if (countdown.sec <= 0) {
			countdown.min -= 1;
			countdown.sec = 59;
		}
	}

	return entities;
}

export default Timer;