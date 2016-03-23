const int ledPin1 = 8;

char val;

void setup(){

  pinMode(ledPin1, OUTPUT);



  Serial.begin(9600);

}

void loop(){

 val=Serial.read();

if(val=='1'){
 digitalWrite(ledPin1, HIGH);
}

else if(val=='2'){
digitalWrite(ledPin1, LOW);
}
 



}
