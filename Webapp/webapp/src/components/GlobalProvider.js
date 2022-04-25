// Provider Variabili Globali

import { createContext, useState } from "react";

export const Run = createContext();
export const Music = createContext();
export const Sfx = createContext();
export const Setting = createContext();

const GlobalProvider = ({children}) => {
	const [run, setRun] = useState(true);
	const [setting, setSetting] = useState(false);
	const [music, setMusic] = useState(0.5);
	const [sfx, setSfx] = useState(0.5);

	return(
		<Run.Provider value={{run, setRun}}>
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