/*
	Contenitore Variabili Importanti per il gioco
	Separate da quelle globali perchè queste servono solo alla pag Play
	In modo da risparmiare stati inutili alla pag Menu
*/

import { createContext, useEffect, useState } from "react"
import useSessionStorage from "../utils/useSessionStorage";

export const DialogCtx = createContext();
export const EnigmaCtx = createContext();
export const RoomNameCtx = createContext();
export const ScoreCtx = createContext();
export const DoneCtx = createContext();
export const GameOverCtx = createContext();
export const CloseCtx = createContext();

const GameContext = ({children}) => {
	const [dialog, setDialog] = useState(false);		// Flag Pannello Dialoghi (Forse da Tagliare)
	const [enigma, setEnigma] = useState(false);		// Flag UI Engigma
	const [room, setRoom] = useState('Chimica');		// Nome stanza in cui sono
	const [score, setScore] = useState(0);				// Punteggio totale
	const [done, setDone] = useState([0,1,2,3,4,5,6,7,8,9]);				// Array contenente gli enigmi già fatti
	const [gameOver, setGameOver] = useState(false);// Flag del Game Over
	const [close, setClose] = useState(false);

	const [listDone, setList] = useSessionStorage('done', done);
	useEffect( () => setList(done), [done]);

	return(
		<DialogCtx.Provider value={{dialog, setDialog}}>
			<EnigmaCtx.Provider value={{enigma, setEnigma}}>
				<RoomNameCtx.Provider value={{room, setRoom}}>
					<ScoreCtx.Provider value={{score, setScore}}>
						<DoneCtx.Provider value={{done, setDone}}>
							<GameOverCtx.Provider value={{gameOver, setGameOver}}>
								<CloseCtx.Provider value={{close, setClose}}>
									{children}
								</CloseCtx.Provider>
							</GameOverCtx.Provider>
						</DoneCtx.Provider>
					</ScoreCtx.Provider>
				</RoomNameCtx.Provider>
			</EnigmaCtx.Provider>
		</DialogCtx.Provider>
	)
}

export default GameContext;