// Provider Variabili Globali

import { createContext, useState } from "react";

export const Pausa = createContext();
export const Music = createContext();
export const Sfx = createContext();

const GlobalProvider = ({children}) => {
	const [pause, setPause] = useState(false);
	const [music, setMusic] = useState(0.5);
	const [sfx, setSfx] = useState(0.5);

	return(
		<Pausa.Provider value={{pause, setPause}}>
			<Music.Provider value={{music, setMusic}}>
				<Sfx.Provider value={{sfx, setSfx}}>
					{children}
				</Sfx.Provider>
			</Music.Provider>
		</Pausa.Provider>
	)
}

export default GlobalProvider;