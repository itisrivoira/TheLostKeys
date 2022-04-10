// Provider Variabili Globali

import { createContext, useState } from "react";

export const Pausa = createContext();
export const Music = createContext();
export const Sfx = createContext();
export const DialogOpen = createContext();

const GlobalProvider = ({children}) => {
	const [pause, setPause] = useState(false);
	const [music, setMusic] = useState(0.5);
	const [sfx, setSfx] = useState(0.5);
	const [dialog, setDialog] = useState(false);

	return(
		<Pausa.Provider value={{pause, setPause}}>
			<Music.Provider value={{music, setMusic}}>
				<Sfx.Provider value={{sfx, setSfx}}>
					<DialogOpen.Provider value={{dialog, setDialog}}>
						{children}
					</DialogOpen.Provider>
				</Sfx.Provider>
			</Music.Provider>
		</Pausa.Provider>
	)
}

export default GlobalProvider;