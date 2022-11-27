// Per gestire i timer

import { useRef, useEffect } from "react";


const useTimeout = (callback, delay) => {
	const savedCallback = useRef();

	useEffect(() => {
	  savedCallback.current = callback;
	}, [callback]);

	useEffect(() => {
		const tick = () => {
			savedCallback.current();
		}

		if (delay !== null) {
			let id = setTimeout(tick, delay);
			return () => clearTimeout(id);
		}
	}, [delay]);
};

export default useTimeout;