// Provider Variabili Globali

import { createContext, useState } from "react";

export const Run = createContext();
export const Music = createContext();
export const Sfx = createContext();
export const DialogOpen = createContext();
export const Opzioni = createContext();
export const Enigma = createContext();

const GlobalProvider = ({children}) => {
	const [run, setRun] = useState(true);
	const [music, setMusic] = useState(0.5);
	const [sfx, setSfx] = useState(0.5);
	const [dialog, setDialog] = useState(false);
	const [setting, setSetting] = useState(false);
	const [enigma, setEnigma] = useState(false);


	return(
		<Run.Provider value={{run, setRun}}>
			<Music.Provider value={{music, setMusic}}>
				<Sfx.Provider value={{sfx, setSfx}}>
					<DialogOpen.Provider value={{dialog, setDialog}}>
						<Opzioni.Provider value={{setting, setSetting}}>
							<Enigma.Provider value={{enigma, setEnigma}}>
								{children}
							</Enigma.Provider>
						</Opzioni.Provider>
					</DialogOpen.Provider>
				</Sfx.Provider>
			</Music.Provider>
		</Run.Provider>
	)
}

export default GlobalProvider;