// Funzione per il countdown dell'UHD

var n = 0.5;

const Timer = (entities) => {
	const { uhd } = entities;

	n++;

	if (n == 62.5) {
		uhd.sec -= 1;
		n = 0.5;;

		if (uhd.sec <= 0) {
			uhd.min -= 1;
			uhd.sec = 59;
		}
	}

	return entities;
}

export default Timer;