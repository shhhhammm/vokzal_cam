/*Souce code of parsing() by AlexGyver
 * Recieves data in string: $MODE VALUE;
 * MODE: 1 or 2:
 * 1 - connects <VALUE> pin as output, VALUE - 1-13, number of pin
 */
int pin = 0;

#define PARSE_AMOUNT 3
int intData[PARSE_AMOUNT] = {0, 0};
boolean recievedFlag;
boolean getStarted;
byte index;
String string_convert = "";
void parsing() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (getStarted) {
      if (incomingByte != ' ' && incomingByte != ';') {
        string_convert += incomingByte;
      } else {
        intData[index] = string_convert.toInt();
        string_convert = "";
        index++;
      }
    }
    if (incomingByte == '$') {
      getStarted = true;
      index = 0;
      string_convert = "";
    }
    if (incomingByte == ';') {
      getStarted = false;
      recievedFlag = true;
    }
  }
}


void setup() {
  Serial.begin(9600);
}

void loop() {
  parsing();
  if (recievedFlag) {
    recievedFlag = false;
  }

  for (byte i = 0; i < PARSE_AMOUNT; i++) {
      Serial.print(intData[i]); Serial.print(" ");
    } Serial.println();
  switch (intData[0])
  {
    case 1:
      pinMode(intData[1], OUTPUT);
      break;
    case 2:
      digitalWrite(intData[1], intData[2]);
  }

}
