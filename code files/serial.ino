#include<Servo.h>

Servo motor1;
Servo motor2;
Servo motor3;
int p = 0;
int q = 0;
int r = 0;
String myCmd;

int trigPin1 = 8;
int echoPin1 = 9;
int trigPin2 = 10;
int echoPin2 = 11;
int trigPin3 = 12;
int echoPin3 = 13;
long duration1, duration2, duration3, distance1, distance2, distance3;

void setup() {
  Serial.begin(9600); 

  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  motor1.attach(5);
  motor2.attach(6);
  motor3.attach(7);

  //Reset motor to 0 degree
  motor1.write(p);
  motor2.write(q);
  motor2.write(r);

}

void loop()
 
  while(Serial.available()==0){
    // Do nothing, just wait for input
  }

  // Read the string until carriage return
  myCmd=Serial.readStringUntil('\r');

  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = (duration1/2) / 29.1;
  Serial.println(distance1);
  delay(500);

  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  distance2 = (duration2/2) / 29.1;
  Serial.println(distance2);
  delay(500);

  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin3, LOW);
  duration3 = pulseIn(echoPin3, HIGH);
  distance3 = (duration3/2) / 29.1;
  Serial.println(distance3);
  delay(500);


  //Turn Servo motor 1 ON to push small sized potato
  if (distance1 <= 10 and myCmd == "ONE"){
  for(p=0;p<=100;p=p+2)
  {
    motor1.write(p);
    delay(20);
  }
  for(p=100;p>=0;p=p-2)
  {
    motor1.write(p);
    delay(10);
  }
  }

  //Turn Servo motor 2 ON to push small sized potato
  if (distance2 <= 10 and myCmd == "TWO"){
  for(q=0;q<=100;q=q+2)
  {
    motor2.write(q);
    delay(10);
  }
  for(q=100;q>=0;q=q-2)
  {
    motor2.write(q);
    delay(10);
  }
  }

  //Turn Servo motor 3 ON to push small sized potato
  if (distance3 <= 10 and myCmd == "THREE"){
  for(r=0;r<=100;r=r+2)
  {
    motor3.write(r);
    delay(10);
  }
  for(r=100;r>=0;r=r-2)
  {
    motor3.write(r);
    delay(10);
  }
  }
