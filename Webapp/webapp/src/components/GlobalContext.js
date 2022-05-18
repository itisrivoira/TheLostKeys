// Contenitore Variabili Globali

import { createContext, useState } from "react";

// CreateContext permette di contenere uno Stato Globale
export const RunCtx = createContext();
export const MusicCtx = createContext();
export const SfxCtx = createContext();
export const SettingCtx = createContext();
export const PgCtx = createContext();
export const NamePlayerCtx = createContext();

// Children è il figlio del componente cioè quello che sta dentro
const GlobalContext = ({children}) => {
	const [run, setRun] = useState(true);				// Flag Gioco in esecuzione
	const [setting, setSetting] = useState(false);	// Flag Pannello Opzioni
	const [music, setMusic] = useState(0.5);			// Livello di Musica
	const [sfx, setSfx] = useState(0.5);				// Livello degli Effetti Sonori
	const [pg, setPg] = useState({}); 					// nome e velocità del personaggio
	const [namePlayer, setNamePlayer] = useState('');

	return(
		<RunCtx.Provider value={{run, setRun}} /*Il Provider fornisce il value ai componenti sottostanti */ >
			<MusicCtx.Provider value={{music, setMusic}}>
				<SfxCtx.Provider value={{sfx, setSfx}}>
					<SettingCtx.Provider value={{setting, setSetting}}>
						<PgCtx.Provider value={{pg, setPg}}>
							<NamePlayerCtx.Provider value={{namePlayer, setNamePlayer}}>
								{children}
							</NamePlayerCtx.Provider>
						</PgCtx.Provider>
					</SettingCtx.Provider>
				</SfxCtx.Provider>
			</MusicCtx.Provider>
		</RunCtx.Provider>
	)
}

export default GlobalContext;