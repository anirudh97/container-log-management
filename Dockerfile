FROM ubuntu:20.04
RUN apt-get update && apt-get -y install curl && apt-get install -y python3 && apt-get -y install systemctl
RUN apt -y install iputils-ping && apt -y install net-tools && apt-get install -y vim && apt-get install -y kafkacat
RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y install default-jre && apt-get -y install zookeeperd
RUN apt-get install -y python3-pip && pip3 install kafka-python && apt-get install -y vim
RUN cd /home && curl "https://downloads.apache.org/kafka/2.8.2/kafka_2.13-2.8.2.tgz" -o ./kafka.tgz
RUN mkdir /home/kafka && cd /home/kafka && tar -xvf /home/kafka.tgz --strip 1

COPY ./server.properties /home/kafka/config/server.properties
COPY ./kafka.service /etc/systemd/system/kafka.service

COPY ./start.sh /home/start.sh
RUN chmod +x /home/start.sh

EXPOSE 9092
EXPOSE 2181


# ENV KAFKA_LISTENERS LISTENER_INTERNAL://server:29090,LISTENER_EXTERNAL://localhost:9090
# ENV KAFKA_LISTENER_SECURITY_PROTOCOL_MAP PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
# ENV KAFKA_INTER_BROKER_LISTENER_NAME PLAINTEXT
# ENV KAFKA_ADVERTISED_LISTENERS LISTENER_INTERNAL://server:29090,LISTENER_EXTERNAL://localhost:9090

COPY ./consumer.py /home/consumer.py

CMD ["/home/start.sh"]
