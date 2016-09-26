class Voxel {
  public float angle;
  public float radius;
  public float level;
  public float radialWidth;
  public color c;
  public boolean render;
  
  // angle is in RADIANS
  Voxel (float angle, float radius, float level, float radialWidth) {
    this.angle = angle;
    this.radius = radius;
    this.level = level;
    this.radialWidth = radialWidth;
    
    this.c = color(255, 0, 0);
    this.render = true;
  }
}