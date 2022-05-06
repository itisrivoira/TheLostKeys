// File di Export
// Qui ci sono tutti gli import dei png delle stanze richimati un Literal Object
// Questo perchè in React non si possono importare le immagini dinamicamente ma solo in modo statico
// Come chiave uso il nome della stanza e sotto altre due sottochiavi: una per png l'altra per il json

export default {
	Chimica: {
		png: require("./assets/rooms/png/Chimica.png"),
		json: require("./assets/rooms/json/Chimica.json")
	},

	Fisica: {
		png: require("./assets/rooms/png/Fisica.png"),
		json: require("./assets/rooms/json/Fisica.json")
	},

	Archivio: {
		png: require("./assets/rooms/png/Archivio.png"),
		json: require("./assets/rooms/json/Archivio.json")
	},

	Corridoio: {
		png: require("./assets/rooms/png/Corridoio.png"),
		json: require("./assets/rooms/json/Corridoio.json")
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
	}

}