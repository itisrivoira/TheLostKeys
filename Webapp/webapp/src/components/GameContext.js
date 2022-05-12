/*
	Contenitore Variabili Importanti per il gioco
	Separate da quelle globali perchè queste servono solo alla pag Play
	In modo da risparmiare stati inutili alla pag Menu
*/

import { createContext, useState } from "react"

export const DialogCtx = createContext();
export const EnigmaCtx = createContext();
export const RoomNameCtx = createContext();
export const ScoreCtx = createContext();
export const DoneCtx = createContext();
export const GameOverCtx = createContext();

const GameContext = ({children}) => {
	const [dialog, setDialog] = useState(false);		// Flag Pannello Dialoghi (Forse da Tagliare)
	const [enigma, setEnigma] = useState(false);		// Flag UI Engigma
	const [room, setRoom] = useState('Chimica');		// Nome stanza in cui sono
	const [score, setScore] = useState(0);				// Punteggio totale
	const [done, setDone] = useState([]);				// Array contenente gli enigmi già fatti
	const [gameOver, setGameOver] = useState(false);// Flag del Game Over

	return(
		<DialogCtx.Provider value={{dialog, setDialog}}>
			<EnigmaCtx.Provider value={{enigma, setEnigma}}>
				<RoomNameCtx.Provider value={{room, setRoom}}>
					<ScoreCtx.Provider value={{score, setScore}}>
						<DoneCtx.Provider value={{done, setDone}}>
							<GameOverCtx.Provider value={{gameOver, setGameOver}}>
								{children}
							</GameOverCtx.Provider>
						</DoneCtx.Provider>
					</ScoreCtx.Provider>
				</RoomNameCtx.Provider>
			</EnigmaCtx.Provider>
		</DialogCtx.Provider>
	)
}

export default GameContext;