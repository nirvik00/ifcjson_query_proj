function init() {
	loadDefault();
}
function loadDefault() {
	const frame = {
		'@context': {
			'@vocab': 'http://bsi.org/ifc/4x3/',
			'@base': 'http://myfile.org/ids/',
			ref: '@id',
			data: '@graph',
			type: '@type',
			globalId: '@id',
		},
		'@type': 'Space',
		'@explicit': true,
		objectType: {},
		name: {},
		Area: {},
		Perimeter: {},
		Volume: {},
		Number: {},
		hasAssociations: {},
	};
	document.getElementById('jsonld-query').value = JSON.stringify(
		frame,
		undefined,
		4
	);
}
async function genFrame() {
	console.log('generate solutions');
	let frame = JSON.parse(document.getElementById('jsonld-query').value);
	console.log(frame);
	let A = document.querySelector('#jsonld-return');
	while (A.children.length > 0) {
		A.removeChild(A.firstChild);
	}
	let p = document.createElement('p');
	p.innerHTML = 'Results:';
	A.appendChild(p);
	let q = document.createElement('textarea');
	q.rows = '20';
	q.cols = '70';
	var framed = 'waiting for results';
	q.value = framed;

	framed = await jsonld.frame(inputData, frame);
	console.log(framed);
	console.log(framed instanceof Array, framed instanceof Object);

	q.value = JSON.stringify(framed, undefined, 4);
	A.appendChild(q);
	//q.value = 'error / no return';
	A.appendChild(q);
}
