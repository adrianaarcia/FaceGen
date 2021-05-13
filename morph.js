/* Adapted from the following sources:
 * 
 * src: https://github.com/learnthreejs/three-js-boilerplate/tree/master/public/examples/3d-obj-loader
 * 
 */

let camera, scene, renderer, controls;

initScene();

const material = new THREE.MeshPhongMaterial( {
    color: 0xeeffff,
    //color: 0xeFBCD4,
    vertexColors: true,
    flatShading: true,
    morphTargets: true
});



arv = new Float32Array(anyrace_verts.flat());
//console.log(arv);
const geometry = new THREE.BufferGeometry();
//const verts = new Float32Array(verts.flat());
//let geometry = new THREE.BufferGeometry().setFromPoints( anyrace_verts );
//geometry.setAttribute( 'position', new THREE.BufferAttribute( arv, 3 ) );
//const mesh = new THREE.Mesh( geometry, material );

// const geometry = new THREE.BoxGeometry( 2, 2, 2, 32, 32, 32 );
// var mesh = new THREE.Mesh( geometry, material );
// scene.add( mesh )

// itemSize = 3 because there are 3 values (components) per vertex
geometry.addAttribute( 'position', new THREE.BufferAttribute( arv, 3 ) );
//const material = new THREE.MeshBasicMaterial( { color: 0xff0000 } );
const mesh = new THREE.Mesh( geometry, material );
console.log(mesh)
var animate = function () {
	requestAnimationFrame( animate );
	controls.update();
	renderer.render(scene, camera);
};

animate();

function initScene() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x8FBCD4 );

    camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
    camera.position.z = 400;

    renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controls.enableZoom = true;

    var keyLight = new THREE.DirectionalLight(new THREE.Color('hsl(30, 100%, 75%)'), 1.0);
    keyLight.position.set(-100, 0, 100);

    var fillLight = new THREE.DirectionalLight(new THREE.Color('hsl(240, 100%, 75%)'), 0.75);
    fillLight.position.set(100, 0, 100);

    var backLight = new THREE.DirectionalLight(0xffffff, 1.0);
    backLight.position.set(100, 0, -100).normalize();

    scene.add(keyLight);
    scene.add(fillLight);
    scene.add(backLight);
}
