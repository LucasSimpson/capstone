
final int RPS = 24;


Controller controller;
Camera camera;

void setup () {
  frameRate(RPS);
  size(1000, 800, P3D);
  noStroke();
  
  controller = new Controller();
  controller.injest("data.txt");
  camera = new Camera();
}


void draw () {
 
  pushMatrix();
  camera.doSetup();
  
  controller.doFrame();
  
  camera.renderVoxels(controller.getVoxels());
  
  camera.doPostProduction();
  popMatrix();
}