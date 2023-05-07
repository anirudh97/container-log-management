from kafka import KafkaConsumer
from pymongo import MongoClient
from subprocess import check_output
import json
import os
import time
import sys
# Define the Kafka topic to consume from

# DOMAIN = ips = check_output(['hostname', '--all-ip-addresses']).decode('utf-8').strip()
DOMAIN = os.environ["HOSTNAME"]
PORT = 27017

client = MongoClient(
        host = "mongodb://" + str(DOMAIN) + ":" + str(PORT),
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = "root",
        password = "1234",
    )

mydb = client['data']
mycol = mydb["topics"]
topic = sys.argv[1]

# Define the Kafka broker server and port
bootstrap_servers = ['server:29092']

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest', value_deserializer=lambda x: x.decode('utf-8'))

# Consume messages from the Kafka topic
for message in consumer:
    consumed_message = json.loads(message.value)
    # print(consumed_message)
    # f.write(message.value)
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    consumed_message["consumer_timestamp"] = round(time.time() * 1000)
    consumed_message["ram_usage_consumer"] = round((used_memory/total_memory) * 100, 2)
    x = mycol.insert_one(consumed_message)


