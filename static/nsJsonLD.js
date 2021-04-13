function init() {
	console.log(inputData);
	loadDefault();
}
function loadDefault() {
	const frame = {
		'@context': {
			'@vocab': 'http://ns.org/ifc/4x3/',
			'@base': 'http://myfile.org/ids/',
			ref: '@id',
			data: '@graph',
			type: '@type',
			globalId: '@id',
		},
		'@type': 'Space',
		'@explicit': true,
		'@contains': 'name',
		objectType: {},
		name: {},
		Area: {},
		Perimeter: {},
		Volume: {},
		Number: {},
		representations: {},
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
	let data = inputData;
	let frame = JSON.parse(document.getElementById('jsonld-query').value);
	console.log(typeof data);
	console.log(typeof frame);
	let A = document.querySelector('#jsonld-return');
	while (A.children.length > 0) {
		A.removeChild(A.firstChild);
	}
	let p = document.createElement('p');
	p.innerHTML = 'Results:';
	A.appendChild(p);
	let q = document.createElement('textarea');
	q.rows = '30';
	q.cols = '100';
	try {
		let framedData = await jsonld.frame(data, frame);
		console.log(framedData);
		q.value = JSON.stringify(framedData, undefined, 4);
	} catch (e) {
		q.value = 'error or did not resolve query';
	}
	A.appendChild(q);
}
