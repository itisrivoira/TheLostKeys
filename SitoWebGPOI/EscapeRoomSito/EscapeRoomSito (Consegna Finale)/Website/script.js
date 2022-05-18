var i = 0;
var progress = document.getElementsByClassName('progress-bar');

var stats = [
	[
		5,
		10,
		10,
		6,
        2,
        7,
        8,
        10,
        7,
		2
	],
	[
		6,
		2,
		8,
		4,
        2,
        6,
        6,
        5,
        9,
		7
	],
	[
		3,
		8,
		7,
		9,
        10,
        8,
        6,
        7,
        6,
		2
	],
	[
		2,
		8,
		10,
		8,
        9,
        10,
        10,
        8,
        10,
		10
	],
	[
		5,
		8,
		6,
		7,
        3,
        6,
        6,
        5,
        4,
		10
	]
]

function avanti() {
	i++;

	if (i > 4) {
		i = 0;
	}

	for (let l = 0; l < progress.length; l++) {
		progress[l].style.width = stats[i][l] + '0%';
		progress[l].ariaValueNow = stats[i][l];
	}
}

function indietro() {
	i--;

	if ( i == 0) {
		i = 4;
	}

	for (let l = 0; l < progress.length; l++) {
		progress[l].style.width = stats[i][l] + '0%';
		progress[l].ariaValueNow = stats[i][l];
	}
}