#include <DHTesp.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include "ArduinoJson.h"

const char* ssid     = "MyWirelessNetwork";
const char* password = "not my password";
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
  // let's parse this as json
  StaticJsonDocument<1024> doc;
  DeserializationError error = deserializeJson(doc, message, length);
  if (error) {

    // it' not JSON, so let's parse it as bytes
    Serial.print("Message arrived on topic: ");
    Serial.print(topic);
    Serial.print(". Message: ");
    String messageTemp;

    for (int i = 0; i < length; i++) {
      Serial.print((char)message[i]);
      messageTemp += (char)message[i];
    }
    Serial.println();
    return;
  }

  // we're here, so the message was valid json
  // get the parsed values and assign to variables
  const char * sensorType = doc["sensorType"]; //Get sensor type value
  int temperature = doc["temperature"];
  int humidity = doc["humidity"];

  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Temp: ");
  Serial.print(temperature);
  Serial.print(". Humidity: ");
  Serial.print(humidity);
  Serial.println();
  serializeJson(doc, Serial); //output the raw JSON to serial
  Serial.println();

  // Feel free to add more if statements to control more GPIOs with MQTT

  // If a message is received on the topic esp32/output, you check if the message is either "on" or "off".
  // Changes the output state according to the message
  /**
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
  **/

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


  // make sure we're connected to the MQTT broker
  if (!client.connected()) {
    reconnect();
  }
  client.loop();  // enter the MQTT loop

  // get and print DHT22 values
  TempAndHumidity lastValues = dht.getTempAndHumidity();
  Serial.println("Transmit Temperature: " + String(lastValues.temperature,0));
  Serial.println("Transmit Humidity: " + String(lastValues.humidity,0));

  // build a JSON object and transmit

  DynamicJsonDocument doc(1024);
  doc["sensorType"] = "dht22";
  doc["temperature"] = lastValues.temperature;
  doc["humidity"] = lastValues.humidity;
  doc["sensor_name"] = "propagator";

  char buffer[512];
  size_t payload_size = serializeJson(doc, buffer);
  client.publish("sensor/temp_hum/propagator", buffer, payload_size);
  delay(5000); // wait 5 seconds before starting from the top of the loop
}