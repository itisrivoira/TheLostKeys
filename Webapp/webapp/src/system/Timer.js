// Funzione per il countdown dell'UHD

var n = 0.5;

const Timer = (entities) => {
	const { uhd } = entities;

	n++;	// ogni 16ms aumento questo contatore

	if (n == 62.5) {		// quindi dopo 62.5 reloads sarà passato un secondo
		uhd.sec -= 1;
		n = 0.5;

		if (uhd.sec <= 0) {	// quando i secondi arrivano a zero tolgo un minuto
			// Se entrambi arrivano a 0 sarà GAME OVER
			if (uhd.min == 0 && uhd.sec == 0)
				uhd.gameOver = true;
			else {
				uhd.min -= 1;
				uhd.sec = 59;
			}
		}
	}

	return entities;
}

export default Timer;