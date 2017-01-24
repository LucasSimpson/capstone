/* January 24th, 2017 
by: James Emmens
Basic shift register (working)
- Sets up shift register to receive. 
- Waits for packet to appear over Serial from computer.
- Sends a hardcoded byte to shift register for display.

_______________________________
Physical Setup:
teensy <--> shift register
3 10, _SRCLR
4 13, _OE
9 12, RCLK (aka LATCH)
11  14, SERIAL DATA
13  SRCLK, SERIAL CLOCK
3.3V as Vcc
GND (not AGND) as GND

--

Shit register pins:
LSB = QA
MSB = QH
_______________________________

*/

#include <SPI.h>

int x;
byte c = B10101;
int pled = 2;
int p_clear = 3;
int p_oe = 4;
int pLatch = 9;

void setup() {
  // Pin Defs and Initial Conditions
  pinMode(pled, OUTPUT);
  pinMode(p_clear, OUTPUT);
  pinMode(p_oe, OUTPUT);
  pinMode(pLatch, OUTPUT);
  
  digitalWrite(p_clear, HIGH);
  digitalWrite(p_oe, LOW);
  digitalWrite(pLatch, LOW);

  //SPI setup. begin() claims the bus from other libraries, .set###### sets a variety of spi bus settings.
  SPI.begin();
  SPI.setBitOrder(MSBFIRST);
  SPI.setDataMode(SPI_MODE0);
  
  //Generic Serial Bus setup. Standard settings used, instantiated @ 9600 baud
  Serial.begin(9600);
}

void loop() {
  // Waits to receive any packet over serial bus.
  if (Serial.available() > 0) {
    x = Serial.read(); // sets received packet as "read"
    Send(); // sends a byte to shift register
    Blink(); // blinks led (pin2)
  }
}

void Blink(void){
  digitalWrite(pled, HIGH);
  delay(500);
  digitalWrite(pled, LOW);
  return;
}

void Send(void){
  // Transfer byte to shift register using clock and data buses.
  SPI.transfer(c);

  // Internally transfer byte from storage registers to appear on "output" registers.
  // Without this step any 8bits the shift register receives is stored but won't appear on outputs
  digitalWrite(pLatch,HIGH); 
  digitalWrite(pLatch,LOW);
  return;
}

