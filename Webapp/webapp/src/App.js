// Componente root della Web App

import { useCallback, useEffect } from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import Menu from "./pages/Menu";
import Play from "./pages/Play";

const App = () => {

	const prevent = useCallback(e => {
		if (e.key == 'F11')
			e.preventDefault();
	})

	useEffect( () => {
		document.addEventListener('keydown', prevent, false);
	}, []);

	return (
		<Routes>
			<Route path="*" element={<Navigate to="/menu" />} />
			<Route path="/menu" element={<Menu />} />
			<Route path="/play" element={<Play />} />
		</Routes>
	);
}

export default App;