function showElements(data) {
	init3d();
	createObjArr(jsonDataIn, 'spaces');
	createObjArr(jsonDataIn, 'walls');
	createObjArr(jsonDataIn, 'slabs');
	createObjArr(jsonDataIn, 'doors');
	createObjArr(jsonDataIn, 'windows');
	createObjArr(jsonDataIn, 'beams');

	ObjArr.forEach((obj) => {
		meshArr3d.push(obj.mesh);
	});

	meshArr3d.push(me);
	meshArr3d.forEach((me) => {
		scene3d.add(me);
	});

	draw3d();
}

function updateView() {
	console.log('update');
	spaces = document.getElementById('cb_spaces').checked;
	walls = document.getElementById('cb_walls').checked;
	slabs = document.getElementById('cb_slabs').checked;
	doors = document.getElementById('cb_doors').checked;
	windows = document.getElementById('cb_windows').checked;
	beams = document.getElementById('cb_beams').checked;
	console.log(spaces, walls, slabs, doors, windows, beams);
	//
	//
	clearMeshes();
	objArr = [];
	if (spaces) createObjArr(jsonDataIn, 'spaces');
	if (walls) createObjArr(jsonDataIn, 'walls');
	if (slabs) createObjArr(jsonDataIn, 'slabs');
	if (doors) createObjArr(jsonDataIn, 'doors');
	if (windows) createObjArr(jsonDataIn, 'windows');
	if (beams) createObjArr(jsonDataIn, 'beams');

	ObjArr.forEach((obj) => {
		meshArr3d.push(obj.mesh);
	});

	meshArr3d.push(me);
	meshArr3d.forEach((me) => {
		scene3d.add(me);
	});

	draw3d();
}

function createObjArr(data, ele) {
	try {
		// console.log(ele);
		let i = 0;
		while (i < data[ele].length) {
			let spaceData = data[ele][i].OBJ;
			verts = [];
			faces = [];
			arr = spaceData.split('\n');
			arr.forEach((e) => {
				a = e.split(' ');
				if (a[0] === 'v') {
					let x = parseFloat(a[1]);
					let y = parseFloat(a[2]);
					let z = parseFloat(a[3]);
					verts.push([x, y, z]);
				} else if (a[0] === 'f') {
					let x = parseInt(a[1]);
					let y = parseInt(a[2]);
					let z = parseInt(a[3]);
					faces.push([x, y, z]);
				}
			});
			me = genGeo(verts, faces, ele).me;
			mat = genGeo(verts, faces, ele).mat;
			data[ele][i].type = ele;
			data[ele][i].mesh = me;
			data[ele][i].material = mat;
			data[ele][i].ori_material = mat;
			data[ele][i].IDX = ObjArr.length + 1;
			ObjArr.push(data[ele][i]);
			i++;
		}
		return true;
	} catch (err) {
		return false;
	}
}

function getInfo(x_obj) {
	let div = document.getElementById('info_selected_div');
	while (div.children.length > 0) {
		div.removeChild(div.firstChild);
	}
	for (x in x_obj) {
		console.log(x, x_obj[x]);
		let p = document.createElement('p');
		p.innerHTML += x + ' --> ' + x_obj[x];
		div.appendChild(p);
	}
}
