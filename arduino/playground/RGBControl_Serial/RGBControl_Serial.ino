/*This code controls RGB led via (1) individual R/G/B logic 0 or higher. And (2) a dim value.*/

int ledPin = 13;
bool currentState = LOW;
int counter = 0;
int dataIn;

int dim = 0;

int temp = 0;

int redPin = 2;
int greenPin = 1;
int bluePin = 0;

byte r_in = 0;
byte g_in = 0;
byte b_in = 0;


void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);  
  
  Serial.begin(9600);
  while(!Serial);
}

void loop() {
  if(Serial.available() > 3){
    //Waits for 4 bytes to be received.
    // Serial.available++ for every byte received over Serial.
    // For other serial ports you would use Serial1.available, Serial2.available etc...
    r_in = Serial.read() - B110000; //  ASCII - 48
    g_in = Serial.read() - B110000;
    b_in = Serial.read() - B110000;

    dim = Serial.read() - B110000;
  }
  
  
  // custom PWM start. 
  digitalWrite(redPin, r_in);
  digitalWrite(greenPin, g_in);
  digitalWrite(bluePin, b_in);
  delayMicroseconds(dim);
  
  digitalWrite(redPin, 0);
  digitalWrite(greenPin, 0);
  digitalWrite(bluePin, 0);
  delayMicroseconds(100 - dim*10);
}
/*
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    Serial.write(inChar);
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    //stringComplete = true;
  }
}
*/
