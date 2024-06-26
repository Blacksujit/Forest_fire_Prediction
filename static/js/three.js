let scene, camera, renderer;
let cube;

function init() {
    // Setup scene, camera, and renderer
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('bgCanvas'), antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Add ambient light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    // Add directional light
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(100, 100, 50);
    scene.add(directionalLight);

    // Add a rotating cube
    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
    cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    animate();
}

function animate() {
    requestAnimationFrame(animate);

    // Rotate cube
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    renderer.render(scene, camera);
}

// Form submission demo (change cube color)
document.getElementById('demoForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const inputValue = document.getElementById('inputValue').value.trim();
    if (inputValue) {
        const color = new THREE.Color(inputValue);
        cube.material.color = color;
    }
});

init();