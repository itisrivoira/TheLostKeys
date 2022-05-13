/*
	File di Export
	Qui ci sono tutti gli import dei png delle stanze richimati un Literal Object
	Questo perchè in React non si possono importare le immagini dinamicamente ma solo in modo statico
	Come chiave uso il nome della stanza e sotto altre due sottochiavi: una per png l'altra per il json
*/

export default {
	// Ogni stanza ha una sua etichetta
	Chimica: {
		png: require("./assets/rooms/png/Chimica.png"),			// Sfondo Stanze
		json: require("./assets/rooms/json/Chimica.json")		// Schema Collisioni Eventi
	},

	Fisica: {
		png: require("./assets/rooms/png/Fisica.png"),
		json: require("./assets/rooms/json/Fisica.json")
	},

	Archivio: {
		png: require("./assets/rooms/png/Archivio.png"),
		json: require("./assets/rooms/json/Archivio.json")
	},

	PianoT: {
		png: require("./assets/rooms/png/PianoT.png"),
		json: require("./assets/rooms/json/PianoT.json")
	},

	Classe1A: {
		png: require("./assets/rooms/png/Classe1A.png"),
		json: require("./assets/rooms/json/Classe1A.json")
	},

	AulaMagna: {
		png: require("./assets/rooms/png/AulaMagna.png"),
		json: require("./assets/rooms/json/AulaMagna.json")
	},

	LabInfo: {
		png: require("./assets/rooms/png/LabInfo.png"),
		json: require("./assets/rooms/json/LabInfo.json")
	},

	WCMaschi: {
		png: require("./assets/rooms/png/WCMaschi.png"),
		json: require("./assets/rooms/json/WCMaschi.json")
	},

	Piano1: {
		png: require("./assets/rooms/png/Piano1.png"),
		json: require("./assets/rooms/json/Piano1.json")

	},

	AulaProfessori: {
		png: require("./assets/rooms/png/AulaProfessori.png"),
		json: require("./assets/rooms/json/AulaProfessori.json")

	},

	WCFemmine: {
		png: require("./assets/rooms/png/WCFemmine.png"),
		json: require("./assets/rooms/json/WCFemmine.json")

	},

	LabInfo2: {
		png: require("./assets/rooms/png/LabInfo2.png"),
		json: require("./assets/rooms/json/LabInfo2.json")

	},

	Ripostiglio: {
		png: require("./assets/rooms/png/Ripostiglio.png"),
		json: require("./assets/rooms/json/Ripostiglio.json")

	},

	Piano2: {
		png: require("./assets/rooms/png/Piano2.png"),
		json: require("./assets/rooms/json/Piano2.json")

	},

	Classe4A: {
		png: require("./assets/rooms/png/Classe4A.png"),
		json: require("./assets/rooms/json/Classe4A.json")

	},

	AulaVideo: {
		png: require("./assets/rooms/png/AulaVideo.png"),
		json: require("./assets/rooms/json/AulaVideo.json")
	},

	StanzaSegreta: {
		png: require("./assets/rooms/png/StanzaSegreta.png"),
		json: require("./assets/rooms/json/StanzaSegreta.json")
	}
}