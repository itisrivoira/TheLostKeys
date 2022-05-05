/*
	Componente root della Web App
	Qui ci sono tutti gli EndPoint
*/

import { useCallback } from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import { GameProvider } from "./components/components";
import { useEventListener } from "./utils/utils";
import { Menu, Play } from './pages/pages';

const App = () => {

	// Evito che l'Utente premi F11 e Escape per non buggare il FullScreen
	const prevent = useCallback(e => {
		if (e.key == 'F11' || e.key == 'Escape')
			e.preventDefault();		// Annulla le azioni eseguite di default dal Browser
	})

	// assegno la funzione prevent all'evento keydown
	useEventListener('keydown', prevent);

	return (
		<Routes>
			<Route path="*" element={<Navigate to="/menu" />} /* Qualsiasi URL scriva l'utente ritornerà al menu principale */  />
			<Route path="/menu" element={<Menu />} />
			<Route path="/play" element={
				<GameProvider>
					<Play />
				</GameProvider>
			} />
		</Routes>
	);
}

export default App;