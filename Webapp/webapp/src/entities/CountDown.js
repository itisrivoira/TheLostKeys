// conto alla rovescia

const CountDown = ({ x, y, min, sec}) => {

	return(
		<p className="text-white fs-1 text-center me-5 txt-pixel">
			{min}:{sec}
		</p>
	)
}

export default CountDown;