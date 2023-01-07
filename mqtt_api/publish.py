import paho.mqtt.client as mqtt
import time
import csv

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

file = open('PhotomFile0.csv','r')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
details = []
for row in csvreader:
        details.append(row)

for detail in details:
    y = ''
    for x in detail:
        y= y + ',' +x
    client.publish("DATAPOINTS", x)
    print("Just published " + str(detail) + " to Topic DATAPOINTS")
    time.sleep(1)