function init(rootObj, prev = 'root') {
	/* console.log('\n', rootObj, prev); */
	let A = document.getElementById('data-container');
	while (A.children.length > 0) {
		A.removeChild(A.firstChild);
	}
	if (!(rootObj instanceof Object)) {
		let p = document.createElement('p');
		p.innerHTML = prev + '\t=\t' + rootObj.toString();
		A.appendChild(p);
		return;
	}
	let obj = { ...rootObj };
	let keys = Object.keys(obj);
	keys.forEach((e) => {
		let p = document.createElement('p');
		let walk = prev + '\t->\t' + e.toString();
		p.innerHTML = walk;
		p.className = 'buiding-element';
		p.addEventListener('click', () => {
			console.log(
				'object: ',
				rootObj[e] instanceof Object,
				'Array: ',
				rootObj[e] instanceof Array
			);
			if (rootObj[e] instanceof Object && rootObj[e] instanceof Array) {
				init(rootObj[e], walk);
			} else if (
				rootObj[e] instanceof Object &&
				!(rootObj[e] instanceof Array)
			) {
				init(rootObj[e], walk);
			} else {
				walk = prev + '\t->\t' + e;
				init(rootObj[e], walk);
			}
		});
		A.appendChild(p);
	});
}

function jsonPathSearch() {
	let x = document.getElementById('jsonpath-query').value.toString();
	let A = document.getElementById('jsonpath-return');
	while (A.children.length > 0) {
		A.removeChild(A.firstChild);
	}
	console.log(x.toString());
	let ret = jsonPath(inputData, x);
	let p = document.createElement('p');
	p.innerHTML = 'Results: ' + ret.length;
	A.appendChild(p);

	let q = document.createElement('textarea');
	q.rows = '40';
	q.cols = '100';
	q.innerHTML = JSON.stringify(ret, undefined, 4);
	A.appendChild(q);
}

function gotoRoot() {
	init(inputData);
}
