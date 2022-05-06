/*
	Contenitore Variabili Importanti per il gioco
	Separate da quelle globali perchè queste servono solo alla pag Play
	In modo da risparmiare stati inutili alla pag Menu
*/

import { createContext, useState } from "react"

export const DialogOpen = createContext();
export const Enigma = createContext();
export const RoomName = createContext();
export const Score = createContext();
export const Done = createContext();

const GameProvider = ({children}) => {
	const [dialog, setDialog] = useState(false);		// Flag Pannello Dialoghi (Forse da Tagliare)
	const [enigma, setEnigma] = useState(false);		// Flag UI Engigma
	const [room, setRoom] = useState('Chimica');		// Nome stanza in cui sono
	const [score, setScore] = useState(0);				// Punteggio totale
	const [done, setDone] = useState([]);				// Array contenente gli enigmi già fatti

	return(
		<DialogOpen.Provider value={{dialog, setDialog}}>
			<Enigma.Provider value={{enigma, setEnigma}}>
				<RoomName.Provider value={{room, setRoom}}>
					<Score.Provider value={{score, setScore}}>
						<Done.Provider value={{done, setDone}}>
							{children}
						</Done.Provider>
					</Score.Provider>
				</RoomName.Provider>
			</Enigma.Provider>
		</DialogOpen.Provider>
	)
}

export default GameProvider;