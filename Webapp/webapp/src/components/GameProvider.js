// Contenitore Variabili Importanti per il gioco

import { createContext, useState } from "react"

export const DialogOpen = createContext();
export const Enigma = createContext();
export const RoomName = createContext();
export const Score = createContext();

const GameProvider = ({children}) => {
	const [dialog, setDialog] = useState(false);
	const [enigma, setEnigma] = useState(false);
	const [room, setRoom] = useState('Chimica');
	const [score, setScore] = useState(0);

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