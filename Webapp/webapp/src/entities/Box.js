// Entita di Prova

const Box = ({x, y}) => {

	return(
		<div style={{
			position: "absolute",
			width: 100,
			height: 200,
			backgroundColor: "red",
			left: x,
			top: y,
		}}
		>
		</div>
	)
}

export default Box;