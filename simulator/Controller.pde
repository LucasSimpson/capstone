class Controller {
  
  // params
  private final int DEGREE_ACC = 2;            // radial partitions is 360 / DEGREE_ACC; ie if DEGREE_ACC is 2 then theres 18 radial partitions
  private final int RADIAL_RES = 10;             // radial resolution, or how many LEDs per blade, whichever you prefer
  private final int NUM_BLADES = 10;             // i feel this is pretty self-explanitory, but i dont wanna break the comment streak
  private final float RADIUS_COEF_START = 0.3;  // percentage at which LED's start appearing (size of the whole in the middle)
  
  private final float SCALE_RADIAL = 250; // radial scale factor, for visualization
  private final float SCALE_Z = 20;      // vertical scale factor, for visualization
  
  private int numVoxels;
  private int LEDCounter = 0;
  private ArrayList<LEDColor> colorInfo = new ArrayList<LEDColor>();
  
  // list of all voxels that exist
  private ArrayList<Voxel> voxels = new ArrayList<Voxel>();
  
  // initialize shit
  Controller () {
    
    this.numVoxels = int (360.0 / float(this.DEGREE_ACC)) * this.RADIAL_RES * this.NUM_BLADES;
    println ("Starting with ", this.numVoxels, " voxels");
    
    // initialize all voxels
    for (int i = 0; i < this.NUM_BLADES; i++) {
      for (int j = 0; j < this.RADIAL_RES; j++) {
        for (int k = 0; k < int (360.0 / float(this.DEGREE_ACC)); k++) {
          
          float angle = 2 * PI * (k * this.DEGREE_ACC + 0.5 * this.DEGREE_ACC) / 360.0;
          
          float radUnit = (1 - this.RADIUS_COEF_START) / this.RADIAL_RES;
          float radius = (float (j) * radUnit + 0.5 * radUnit + this.RADIUS_COEF_START) * this.SCALE_RADIAL;
          float level = i * this.SCALE_Z;
          float radialWidth = 2 * PI * float(this.DEGREE_ACC) / 360.0;
      
          // all the math is so that the coordiantes are at the middle of the voxels, not on the corners. hence the offsets
          this.voxels.add(new Voxel (angle, radius, level, radialWidth));
        }
      }
    }
  }

  // injests a data source that describes how the LED's should light up
  public void injest(ArrayList<String> data) {
    
    // make sure data lines up
    if (data.size() % this.numVoxels != 0) {
      
      // this should be runtime exception but apperently those arent supported/documented????
       println ("Length of data passed (", data.size(), ") is not modulable by number of voxels (", this.numVoxels, ")"); 
    }
    
    // build list of colors
    for (String line_: data) {
      
      // remove new line charts if they exist
      String line = line_.substring(line_.length()-1) == "\n" ? line_.substring(0, line_.length() - 1) : line_;
            
      if (line.length() == 1) {
        this.colorInfo.add(new LEDColor(false));
      } else {
        String[] clrs = split(line, ',');
        this.colorInfo.add(new LEDColor(int(clrs[0]), int(clrs[1]), int(clrs[2])));
      }
    }
    
  }
  
  // injest data from file
  public void injest(String filename) {
    String[] lines = loadStrings(filename);
    
    // cast to arrayList, this is the best way i can figure out how -.-
    ArrayList<String> lines_ = new ArrayList<String>();
    for (String line: lines) {
      lines_.add(line);
    }
    
    // injest array
    this.injest(lines_);
  }
  
  // compute data for 1 frame (or 1 rotation)
  public void doFrame() {
    
    // set all LEDs, one per voxel1
    for (int i = 0; i < this.numVoxels; i++) {
      
      // get the next voxel and color
      Voxel v = this.voxels.get(i);
      LEDColor c = this.colorInfo.get(this.LEDCounter);
      
      // set color
      if (c.render) {
        v.render = true;
        v.c = color(c.r, c.g, c.b);
      } else {
        v.render = false;
      } 
   
      // inc counter
      this.LEDCounter ++;
    }
    
    // loop animation
    if (this.LEDCounter == this.colorInfo.size()) {
      this.LEDCounter = 0; 
    }
  }
  
  public ArrayList<Voxel> getVoxels() {
    return this.voxels;
  }
}