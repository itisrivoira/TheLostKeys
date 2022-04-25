// Componente root della Web App

import { useCallback } from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import { GameProvider } from "./components/components";
import { useEventListener } from "./utils/utils";
import { Menu, Play } from './pages/pages';

const App = () => {

	const prevent = useCallback(e => {
		if (e.key == 'F11')
			e.preventDefault();
	})

	useEventListener('keydown', prevent);

	return (
		<Routes>
			<Route path="*" element={<Navigate to="/menu" />} />
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