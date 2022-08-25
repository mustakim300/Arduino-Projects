#include <Servo.h>
#define unpress_angle 0
#define press_angle 35
int ldr=A1;
int data; 
Servo myservo; // create servo object to control a servo
void setup() 
{ 
  pinMode(ldr,INPUT);
  Serial.begin(9600);    
  myservo.attach(9); 
  myservo.write(unpress_angle);
} 
void loop(){
  data=analogRead(ldr);
  Serial.println(data);
  myservo.write(unpress_angle); // unpress the button
  delay(50);
 if(data<30)
   {  
     myservo.write(press_angle); // press the button
     delay(100); // waits 100ms for the servo to reach the position
  }
}
