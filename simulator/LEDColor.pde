class LEDColor {
   public int r;
   public int g;
   public int b;
   public boolean render;
   
   LEDColor (int r, int g, int b) {
      this.r = r;
      this.g = g;
      this.b = b;
      this.render = true;
   }
   
   LEDColor (boolean render) {
     this.render = false; 
   }
  
}