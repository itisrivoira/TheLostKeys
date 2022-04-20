import useLoop from './useLoop';
import useTimer from './useTimer.js';

const useSystem = () => {
	return [
		useLoop,
		useTimer
	]
}

export default useSystem;