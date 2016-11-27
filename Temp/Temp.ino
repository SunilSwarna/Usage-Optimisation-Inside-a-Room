void setup(){
  
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  Serial.begin(9600);
  
}
void loop(){
  
  
  float x,temp;
  x=analogRead(A0);
  //Serial.println(x);
  x=(x*500)/1024.0;
  Serial.print("Degrees:");
  Serial.println(abs(x));
  
  if(abs(x)>=35){
    digitalWrite(3,HIGH);
  }
  else{  
  digitalWrite(3,LOW);
  }
  
  delay(500);
  
}
