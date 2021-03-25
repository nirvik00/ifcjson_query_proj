function genGeo(verts, faces, ele) {
	let Geom = new THREE.Geometry();
	verts.forEach((v) => {
		let p = new THREE.Vector3(v[0], v[1], v[2]);
		Geom.vertices.push(p);
	});
	faces.forEach((f) => {
		let F = new THREE.Face3(f[0], f[1], f[2]);
		Geom.faces.push(F);
	});
	mat = new THREE.MeshPhongMaterial({
		color: getColor(ele),
		opacity: 0.5,
		transparent: true,
	});
	me = new THREE.Mesh(Geom, mat);
	return { me, mat };
}

function init3d() {
	scene3d = new THREE.Scene();
	scene3d.background = new THREE.Color(0xffffff);
	camera3d = new THREE.PerspectiveCamera(
		45,
		window.innerWidth / window.innerHeight,
		0.1,
		100000
	);
	camera3d.up = new THREE.Vector3(0, 0, 1);
	camera3d.position.set(25, 25, 25);
	renderer3d = new THREE.WebGLRenderer();
	renderer3d.setSize(window.innerWidth, window.innerHeight);
	raycaster = new THREE.Raycaster();
	div3d = document.getElementById('viewer3d');
	div3d.appendChild(renderer3d.domElement);
	controls3d = new THREE.OrbitControls(camera3d, renderer3d.domElement);
	controls3d.addEventListener('change', updateScene);
	let axes = new THREE.AxesHelper(10);
	scene3d.add(axes);
	let light = new THREE.AmbientLight(0x404040);
	scene3d.add(light);
	document.addEventListener('mousedown', onMouseDown, false);
}

function clearMeshes() {
	ObjArr.forEach((obj) => {
		try {
			obj.mesh.geometry.dispose();
			obj.mesh.material.dispose();
			scene3d.remove(obj.mesh);
		} catch (err) {}
	});
	ObjArr = [];
	meshArr3d.forEach((m) => {
		try {
			m.geometry.dispose();
			m.material.dispose();
			scene3d.remove(m);
			delete m;
		} catch (err) {}
	});
	meshArr3d = [];
}

function getColor(ele) {
	let color = new THREE.Color(0xff0000);
	if (ele === 'spaces') {
		color = new THREE.Color(0xeeeeee);
	} else if (ele === 'walls') {
		color = new THREE.Color(0x0000ff);
	} else if (ele === 'doors') {
		color = new THREE.Color(0x00ff00);
	} else if (ele === 'slabs') {
		color = new THREE.Color(0x0aff0a);
	} else if (ele === 'beams') {
		color = new THREE.Color(0x00000a);
	} else if (ele === 'windows') {
		color = new THREE.Color(0xa0f00a);
	} else if (ele === 'roofs') {
		color = new THREE.Color(0xfff00a);
	}
	return color;
}

function updateScene() {
	camera3d.aspect = window.innerWidth / window.innerHeight;
	renderer3d.setSize(window.innerWidth, window.innerHeight);
	camera3d.updateProjectionMatrix();
}

function draw3d() {
	requestAnimationFrame(draw3d);
	renderer3d.render(scene3d, camera3d);
}

function onMouseDown(e) {
	console.log('mousedown');
	var m2 = new THREE.MeshPhongMaterial({
		color: 0xff0000,
		opacity: 0.25,
		transparent: true,
	});
	ObjArr.forEach((obj) => {
		obj.mesh.scale.set(1, 1, 1);
	});
	intxArr = [];
	mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
	mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
	raycaster.setFromCamera(mouse, camera3d);
	var intersects = raycaster.intersectObjects(scene3d.children);
	if (intersects.length > 0) {
		var obj = intersects[0];
		var p = obj.object.uuid;
		for (var i = 0; i < ObjArr.length; i++) {
			let meshObj = ObjArr[i].mesh;
			var q = meshObj.uuid;
			if (p === q) {
				intxArr.push(ObjArr[i].mesh);
				ObjArr[i].mesh.material = m2;
				// console.log('obj selected: ', ObjArr[i]);
				getInfo(ObjArr[i]);
			}
		}
	}
}
