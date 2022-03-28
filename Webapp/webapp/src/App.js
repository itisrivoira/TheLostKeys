// Componente root della Web App

import { Routes, Route, Navigate } from "react-router-dom";

import Menu from "./pages/Menu";
import Play from "./pages/Play";

const App = () => {

	return (
		<Routes>
			<Route path="*" element={<Navigate to="/menu" />} />
			<Route path="/menu" element={<Menu />} />
			<Route path="/play" element={<Play />} />
		</Routes>
	);
}

export default App;