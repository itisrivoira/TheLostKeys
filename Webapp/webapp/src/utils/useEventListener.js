// Custom Hook per la gestione degli eventi del browser

import { useRef, useEffect } from 'react';

function useEventListener(eventName, handler) {
	const savedHandler = useRef();

	useEffect(() => {
		savedHandler.current = handler;
	}, [handler]);

	useEffect(
		() => {
			const isSupported = window && window.addEventListener;
			if (!isSupported) return;

			const eventListener = (event) => savedHandler.current(event);
			window.addEventListener(eventName, eventListener);

			return () => {
				window.removeEventListener(eventName, eventListener);
			};
		},
 	[eventName] );
}

export default useEventListener;