#include <DHTesp.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include "ArduinoJson.h"

const char* ssid     = "chillies";
const char* password = "not-my-password";
const char* mqtt_server = "192.168.2.10";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

float temp = 0;
float hum = 0;

String mqtt_temp;
String mqtt_hum;

char transmit_temp[50];
char transmit_hum[50];

DHTesp dht;
/** Task handle for the light value read task */
TaskHandle_t tempTaskHandle = NULL;
/** Pin number for DHT11 data pin */
int dhtPin = 15;

void setup() {
  // put your setup code here, to run once:
  // Initialize temperature sensor
  dht.setup(dhtPin, DHTesp::DHT22);

  // Connect to wifi
  Serial.begin(115200);
  delay(10);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  Serial.println("Connecting to MQTT");
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;

  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  // Feel free to add more if statements to control more GPIOs with MQTT

  // If a message is received on the topic esp32/output, you check if the message is either "on" or "off".
  // Changes the output state according to the message
  if (String(topic) == "esp32/output") {
    Serial.print("Changing output to ");
    if(messageTemp == "on"){
      Serial.println("on");
      //digitalWrite(ledPin, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("off");
      //digitalWrite(ledPin, LOW);
    }
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP32Client", "test", "testing123")) {
      Serial.println("connected");
      // Subscribe
      client.subscribe("test");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() {

  /**
  JSON Code
  **/

  DynamicJsonDocument doc(1024);

  doc["sensorType"] = "temperature";
  //doc["raw"] = serialized("[1,2,3]");
  doc["value"] = 28;
  serializeJson(doc, Serial);

  char buffer[512];
  size_t payload_size = serializeJson(doc, buffer);
  //serializeJson(doc, buffer);

  // deserialize incoming JSON
  char json[] = "{\"sensorType\":\"temperature\",\"value\":30}";
  DeserializationError error = deserializeJson(doc, json);
  if (error)
    return;

  // get the parsed values and assign to variables
  const char * sensorType = doc["sensorType"]; //Get sensor type value
  int value = doc["value"];



  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  // put your main code here, to run repeatedly:
  TempAndHumidity lastValues = dht.getTempAndHumidity();

  temp = lastValues.temperature;
  hum = lastValues.humidity;
  mqtt_temp = "temperature: " + String(temp, 0);
  mqtt_hum = "humidity: " + String(hum, 0);
  strcpy(transmit_temp, mqtt_temp.c_str());
  strcpy(transmit_hum, mqtt_hum.c_str());


  Serial.println("Temperature: " + String(lastValues.temperature,0));
  Serial.println("Humidity: " + String(lastValues.humidity,0));
  client.publish("test", transmit_temp);
  client.publish("test", transmit_hum);
  client.publish("test", buffer, payload_size);

  delay(2000);
}