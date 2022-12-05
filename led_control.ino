float x;
int red = 2;
int yellow = 3;
int green = 4;
int blue = 5;


void setup() {
  Serial.begin(9600);
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
    x = Serial.read();
    Serial.print((x));
  if(x == '1'){
    digitalWrite(red, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
    digitalWrite(blue, HIGH);
    delay(1000);
  }
  else if(x == '2'){
    digitalWrite(yellow, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
    digitalWrite(blue, LOW);
    delay(1000);
  }
  else if(x == '3'){
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(blue, LOW);
    delay(1000);
  }
  else if(x=='4'){
    digitalWrite(blue, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
    delay(1000);
  }
  }
}
