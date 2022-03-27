// Provider Variabili Globali

import { createContext, useState } from "react";

export const Pausa = createContext();

const GlobalProvider = ({children}) => {
	const [pause, setPause] = useState(false)

	return(
		<Pausa.Provider value={{pause, setPause}}>
			{children}
		</Pausa.Provider>
	)
}

export default GlobalProvider;