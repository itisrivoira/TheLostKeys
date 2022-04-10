// testo del dialogo con vignetta

import { useEffect, useState } from "react";

const DialogText = ({i, now, text}) => {

	return(
		i === now && (
			<p>
				{text}
			</p>
		)
	)
}

export default DialogText;