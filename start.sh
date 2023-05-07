#!/bin/bash


/usr/share/zookeeper/bin/zkServer.sh start-foreground &
sleep 5

exec python3 /home/consumer.py &

/home/kafka/bin/kafka-server-start.sh /home/kafka/config/server.properties