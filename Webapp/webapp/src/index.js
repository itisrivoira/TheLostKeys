/*
	File Root
 	Qui c'è il contenitore degli Stati Globali e degli EndPoint
*/

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

import { GlobalContext } from './components/components';
import App from './App';

import 'bootstrap/dist/css/bootstrap.min.css';		// Foglio di stile per Bootstrap
import './style/index.css';

ReactDOM.render(
	<React.StrictMode>
		<BrowserRouter>
			<GlobalContext>
				<App />
			</GlobalContext>
		</BrowserRouter>
	</React.StrictMode>,
	document.getElementById('root')
);
