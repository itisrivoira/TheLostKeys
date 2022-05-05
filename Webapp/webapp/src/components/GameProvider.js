// Contenitore Variabili Importanti per il gioco
// Separate da quelle globali perchè queste servono solo alla pag Play
// In modo da risparmiare stati inutili alla pag Menu

import { createContext, useState } from "react"

export const DialogOpen = createContext();
export const Enigma = createContext();
export const RoomName = createContext();
export const Score = createContext();

const GameProvider = ({children}) => {
	const [dialog, setDialog] = useState(false);		// Flag Pannello Dialoghi
	const [enigma, setEnigma] = useState(false);		// Flag UI Engigma
	const [room, setRoom] = useState('Chimica');		// Nome stanza in cui sono
	const [score, setScore] = useState(0);				// Punteggio totale

	return(
		<DialogOpen.Provider value={{dialog, setDialog}}>
			<Enigma.Provider value={{enigma, setEnigma}}>
				<RoomName.Provider value={{room, setRoom}}>
					<Score.Provider value={{score, setScore}}>
						{children}
					</Score.Provider>
				</RoomName.Provider>
			</Enigma.Provider>
		</DialogOpen.Provider>
	)
}

export default GameProvider;