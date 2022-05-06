// Contenitore Variabili Globali

import { createContext, useState } from "react";

// CreateContext permette di contenere uno Stato Globale
export const Run = createContext();
export const Music = createContext();
export const Sfx = createContext();
export const Setting = createContext();

// Children è il figlio del componente cioè quello che sta dentro
const GlobalProvider = ({children}) => {
	const [run, setRun] = useState(true);				// Flag Gioco in esecuzione
	const [setting, setSetting] = useState(false);	// Flag Pannello Opzioni
	const [music, setMusic] = useState(0.5);			// Livello di Musica
	const [sfx, setSfx] = useState(0.5);				// Livello degli Effetti Sonori

	return(
		<Run.Provider value={{run, setRun}} /*Il Provider fornisce il value ai componenti sottostanti */ >
			<Music.Provider value={{music, setMusic}}>
				<Sfx.Provider value={{sfx, setSfx}}>
					<Setting.Provider value={{setting, setSetting}}>
						{children}
					</Setting.Provider>
				</Sfx.Provider>
			</Music.Provider>
		</Run.Provider>
	)
}

export default GlobalProvider;