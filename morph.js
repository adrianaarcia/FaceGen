/* Adapted from the following sources:
 * 
 * src: https://github.com/learnthreejs/three-js-boilerplate/tree/master/public/examples/3d-obj-loader
 * src: https://github.com/mrdoob/three.js/blob/master/examples/webgl_morphtargets.html
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

var objLoader = new THREE.OBJLoader();
objLoader.setPath('/facegen/assets/anyrace/average/');

var malePositions = [];
objLoader.load('male/avg_anyrace_male.obj', function (object) {
    var n = 0;
    object.traverse(function(child)
    {
        if (n == 0 & child instanceof THREE.Mesh)
        {
            malePositions = child.geometry.attributes.position.array;
            n++;
    }})});

var group = new THREE.Object3D;
var mesh; 
objLoader.load('female/avg_anyrace_female.obj', function (object) {
    var n = 0;
    object.traverse(function(child)
    {
        if (n == 0 & child instanceof THREE.Mesh)
        {
            //add morph
            child.geometry.morphAttributes.position = [];
            const positionAttribute = child.geometry.attributes.position;

            // add the male positions as the morph target
			child.geometry.morphAttributes.position[ 0 ] = new THREE.Float32BufferAttribute(malePositions, 3 );

            //add color
            const count = child.geometry.attributes.position.count;
            colors = new Array(count*3).fill(1);
            child.geometry.addAttribute('color', new THREE.BufferAttribute(new Float32Array(colors), 3));
            
            //add material
            mesh = new THREE.Mesh(child.geometry, material);
            
            group.add(mesh)
            n++;
        }

    });
});

initGUI();
scene.add(group);

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

function initGUI() {

    // Set up dat.GUI to control targets
    const params = {
        Male: 0,
    };
    const gui = new dat.GUI();
    const folder = gui.addFolder( 'Morph Targets' );

    folder.add( params, 'Male', 0, 1 ).step( 0.01 ).onChange( function ( value ) {

        mesh.morphTargetInfluences[ 0 ] = value;

    } );
}
