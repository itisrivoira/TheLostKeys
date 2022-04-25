// Contenitore Variabili Importanti per il gioco

import { createContext, useState } from "react"

export const DialogOpen = createContext();
export const Enigma = createContext();

const GameProvider = ({children}) => {
	const [dialog, setDialog] = useState(false);
	const [enigma, setEnigma] = useState(false);


	return(
		<DialogOpen.Provider value={{dialog, setDialog}}>
			<Enigma.Provider value={{enigma, setEnigma}}>
				{children}
			</Enigma.Provider>
		</DialogOpen.Provider>
	)
}

export default GameProvider;