import json
import time
from kafka import KafkaConsumer, KafkaProducer
import os

bootstrap_servers = ['server:29092']

topicname = 'myTopic'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
prio_file = open('/home/priority.json')
data = json.load(prio_file)
prio_file.close()
file_paths= []
d = sorted(data, key=lambda k: k['priority'])
for di in d:
    file_paths.append(di['filename'])
file_paths.append("/var/log/failog")
file_paths.append("/var/log/apt/history.log")


file_positions = [0]*len(file_paths)
file_index = 0

while True:
    try:
        with open(file_paths[file_index], 'r') as f:
            f.seek(file_positions[file_index])
            for line in f:
                meta = {"container": os.environ['HOSTNAME'], "source_file": file_paths[file_index], "payload": line.strip(), "producer_timestamp": round(time.time() * 1000)}
                producer.send(topicname, json.dumps(meta).encode('utf-8'))

            file_positions[file_index] = f.tell()

    except FileNotFoundError:
        pass

    file_index = (file_index + 1) % len(file_paths)
    time.sleep(0.1)