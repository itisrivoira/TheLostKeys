// Questo è il Dizionario degli enigmi

const puzzles = {
	Chimica:{
		text: "Per trovare la chiavetta somma il numero degli atomi di ossigeno nell’acqua, di idrogeno dell’acido solforico e l’ordine di grandezza della costante di avogadro",
		img: false,
		A: "25",
		B: "26",
		C: "23",
		D: "15",
		right: "B",
		indizio: "Il numero e' uguale alle lettere dell’alfabeto",
		punti: [0, 10, 20, 40]
	},

	PianoT:{
		text: "",
		img: false,
		A: "",
		B: "",
		C: "",
		D: "",
		right: "",
		indizio: "",
		punti: []
	},

	Fisica:{
		text: "Cosa c’e' all’inizio dell’onda elettromagnetica, al centro dell’atomo, e alla fine di uno spettrometro?",
		img: false,
		A: "La radiazione",
		B: "Il vuoto",
		C: "O'",
		D: "L'atmosfera",
		right: "C",
		indizio: "A volte la risposta e' quella più semplice se si pensa alla lettera",
		punti: [0, 2, 5, 10]
	},

	Archivio:{
		text: "",
		img: false,
		A: "",
		B: "",
		C: "",
		D: "",
		right: "",
		indizio: "",
		punti: []
	},

	AulaMagna:{
		text: "I have 4 legs, a back, but no head, What am I?",
		img: false,
		A: "Cap",
		B: "Blackboard",
		C: "Cat",
		D: "Chair",
		right: "D",
		indizio: "La usiamo tutti i giorni",
		punti: [0, 10, 20, 40]
	},

	LabInfo: {
		text: "Determinare il valore di B a fine esecuzione",
		img: require('../img/info1.png'),
		A: "3",
		B: "B",
		C: "5",
		D: "0",
		right: "D",
		indizio: "Il costrutto Repeat Until funziona come il While",
		punti: [0, 10, 20, 40]
	},

	Classe1A: {
		text: "La somma della superficie di 3 piscine misura 1200 m^2. Se la prima e' il doppio della seconda e questa e' il triplo della terza, quanto misura in m^2 ogni piscina?",
		img: false,
		A: "C = 400  B = 400  A = 400",
		B: "B = 120  C = 390  A = 720",
		C: "C = 120  B = 3C = 360  A = 2B = 720",
		D: "Non si puo determinare",
		right: "C",
		indizio: "A + B + C = 1200",
		punti: [0, 10, 20, 40]
	},

	WCMaschi: {
		text: "",
		img: false,
		A: "",
		B: "",
		C: "",
		D: "",
		right: "",
		indizio: "",
		punti: []
	},

	WCFemmine: {
		text: "Risolvi lo schema per il passaggio di stato: da una sostanza solida come il ghiaccio qual e' il giusto ordine per passare allo stato gassoso, e poi a quello liquido come l’acqua e poi di nuovo allo stato solido?",
		img: false,
		A: "Sublimazione - Liquefazione - Solidificazione",
		B: "Liquefazione - Sublimazione - Solidificazione",
		C: "Solidificazione - Liquefazione - Sublimazione",
		D: "Non si puo determinare",
		right: "A",
		indizio: "Eila', da quanto tempo! Non ti ricordi la prima lezione sui passaggi stato? Ti rinfresco la memoria. I passaggi di stato che possono verificarsi nella materia sono:| il passaggio dallo stato liquido a quello solido: solidificazione| il passaggio dallo stato solido a quello liquido: fusione| passaggio dallo stato liquido a quello aeriforme: vaporizzazione| passaggio dallo stato aeriforme a quello liquido: condensazione| il passaggio dallo stato solido a quello aeriforme sublimazione| Spero di esserti stato utile, in bocca al lupo!",
		punti: [0, 2, 5, 10]
	},

	CLasse1D: {
		text: "Cosa usi per misurare la lunghezza, il tempo la corrente e la temperatura?",
		img: false,
		A: "metri- secondi- Ampere- Kelvin",
		B: "centimetri- ore - ohm - celsius",
		C: "kilometri - minuti - Ampere - Fahrenheit",
		D: "ettometri - secondi - ohm - Kelvin",
		right: "A",
		indizio: "m…., s….., A….., K…..",
		punti: [0, 10, 20, 40]
	},

	AulaProfessori: {
		text: "Ricordi quando ufficialmente la scuola fu chiusa? In quel mese di 101 anni prima si stava concludendo uno duro scontro in un paese distante dal nostro. Trova il libro celebre di quegli anni all'interno dell'edificio, e ti guideranno alla chiavetta",
		img: false,
		A: "1900",
		B: "1817",
		C: "1917",
		D: "1950",
		right: "C",
		indizio: "Vecchio giornale in una classe con in prima pagina la notizia della chiusura della scuola (con la data 2 febbraio 2018)",
		punti: [0, 10, 20, 40]
	},

	Piano1: {
		text: "",
		img: false,
		A: "",
		B: "",
		C: "",
		D: "",
		right: "",
		indizio: "",
		punti: []
	},

	Piano2: {
		text: "Quanto fa 2^12 sapendo che 2^6 fa 64?",
		img: false,
		A: "4096",
		B: "4094",
		C: "4092",
		D: "4090",
		right: "A",
		indizio: "2^12 non è il doppio di 2^6",
		punti: [0, 10, 20, 40]
	},

	LabInfo2: {
		text: "Determinare il valore di A a fine esecuzione",
		img: false,
		A: "5",
		B: "10",
		C: "3",
		D: "15",
		right: "D",
		indizio: "Il costrutto repeat funziona come un il For",
		punti: [0, 2, 5, 10]
	},

	Ripostiglio: {
		text: "Il doppio aumentato di 9 del prodotto di un numero naturale con un altro che lo supera di quattro è uguale a 3 volte il quadrato del primo. Determinare i due numeri.",
		img: false,
		A: "x1 = 19 x2 = 0",
		B: "x1 = 10 x2 = 1",
		C: "x1 = 9 x2 = 13",
		D: "x1 = 144 x2 = 7",
		right: "C",
		indizio: "2x(x + 4) + 9 = 3x2",
		punti: [0, 10, 20, 40]
	},

	Classe4A: {
		text: "Questo enigma è uguale :(",
		img: false,
		A: "",
		B: "",
		C: "",
		D: "",
		right: "",
		indizio: "",
		punti: [0,2,5]
	},

	AulaVideo: {
		text: "Sblocchi un flashback della prima superiore, ti ricordi quando tutto in questo ambiente ti sembrava tutto nuovo, è come se ci fosse un fanciullino dentro di te, che autore di ricorda?",
		img: false,
		A: "Verga",
		B: "Pirandello",
		C: "Pascoli",
		D: "D'Annunzio",
		right: "C",
		indizio: "autore di fine '800",
		punti: [0, 2, 5, 10]
	}
}

export default puzzles;