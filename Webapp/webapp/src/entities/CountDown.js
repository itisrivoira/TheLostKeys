// conto alla rovescia

const CountDown = ({ x, y, min, sec}) => {

	return(
		<p className="text-white fs-1 text-end me-5">
			{min} : {sec}
		</p>
	)
}

export default CountDown;