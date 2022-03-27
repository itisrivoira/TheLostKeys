import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

import GlobalProvider from './components/GlobalProvider';
import App from './App';

import 'bootstrap/dist/css/bootstrap.min.css';
import './style/index.css';

ReactDOM.render(
	<React.StrictMode>
		<GlobalProvider>
			<BrowserRouter>
				<App />
			</BrowserRouter>
		</GlobalProvider>

	</React.StrictMode>,
	document.getElementById('root')
);
