/* 
 * littleWork: work time notifier
 *
 * Part of the Instructables littleBits build night with the Taipei Hackerspace
 * Feel free to copy / modify.
**/

const int dialPin = 9;
const int buzzerPin = 1;
int output = 0;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  analogWrite(dialPin, output);

  if (Serial) {   /* needed by the Leonardo types */
    Serial.begin(115200);
  }
}

void loop() {
  int cmdByte;
  
  if (Serial.available() > 0) {
    cmdByte = Serial.read();
    
    if (cmdByte == 255) {
      /* sound buzzer */
      siren();
    } else {
      /* set display to appropriate value */   
      analogWrite(dialPin, cmdByte);
    }
    Serial.println(cmdByte, DEC);
  }    
}

/* Beeps to sound te buzzer*/
void siren() {
  digitalWrite(buzzerPin, HIGH);
  delay(200);
  digitalWrite(buzzerPin, LOW);
  delay(1000);
  digitalWrite(buzzerPin, HIGH);
  delay(200);
  digitalWrite(buzzerPin, LOW);  
}
