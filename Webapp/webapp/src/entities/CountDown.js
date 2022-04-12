// conto alla rovescia


const CountDown = ({ x, y, min, sec}) => {

	return(
		<p className="text-black fs-1 text-center">
			{min} : {sec}
		</p>
	)
}

export default CountDown;