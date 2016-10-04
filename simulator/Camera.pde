class Camera {
  private final int DAMP_COEF = 120;
  
  private float rotX, rotY, mx, my, prevMx, prevMy = 0;
   
  // set up camera for frame visualization
  public void doSetup() {
    // set empty background
    background (255);
    
    
    // get mouse coordinates
    this.mx = mouseX;
    this.my = mouseY;
    
    // add to rotation offsets based on mouse movement
    this.rotX += (this.mx - this.prevMx) / DAMP_COEF;
    this.rotY += (this.prevMy - this.my) / DAMP_COEF;
    
    // save prev values
    this.prevMx = mx;
    this.prevMy = my;
  }
  
  private void renderVoxel(Voxel voxel) {
    float x = voxel.radius * sin(voxel.angle);
    float y = voxel.radius * cos(voxel.angle);
    float z = voxel.level;
    float sx = voxel.radius * voxel.radialWidth;
    
    pushMatrix();
    
    // center shit visually
    translate (width / 2.0, height / 2.0, -50);
    
    // rotate frame
    rotateY (this.rotX);
    rotateX (this.rotY);
    
    // translate for center rotating
    translate (0, 0, -100);
    
    // translate set amount
    translate (x, y, z);
    
    // rotate to face inwards
    rotateZ(-voxel.angle);
    
    // scale
    scale(sx, 5, 5);

    // draw voxel
    fill (voxel.c);
    box (1);
    
    popMatrix();
  }
  
  public void renderVoxels (ArrayList<Voxel> voxels) {
    for (Voxel voxel: voxels) {
      if (voxel.render) {
        this.renderVoxel(voxel);
      } /* temp debugging hack, draw non-rendered as gray */ else {
        voxel.c = color(215);
        this.renderVoxel(voxel);
      }
    }
  }
  
  // because we're THAT fancy
  public void doPostProduction() {
    pushMatrix();
    
    // center shit visually
    translate (width / 2.0, height / 2.0, -50);
    
    // rotate frame
    rotateY (this.rotX);
    rotateX (this.rotY);
  
    // translate for center rotating
    translate (0, 0, -100);
  
    // draw context lines
    stroke(color(255, 0, 0));
    line (-300, -300, 300, -300);
    stroke(color(0, 255, 0));
    line(-300, -300, -300, 300);
    rotateX(PI/2);
    translate(-300, 0, 300);
    stroke(color(0, 0, 255));
    line(0, 0, 0, 300);
    
    noStroke();
    popMatrix();
  }
}