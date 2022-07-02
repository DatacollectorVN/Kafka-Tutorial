# Kafka-Tutorial
# 1. Getting start without Docker
## 1.1. Start with Zookeeper
- Create folder for Zookeeper (any location)
```bash
mkdir data
mkdir data/zookeeper
```
- Change configuration of Zookeeper to folder that was created
```
nano /opt/homebrew/etc/kafka
```
Edit `dataDir=<PATH_TO_ZOOKEEPER_FOLDER>`

- Start Zookeeper
```bash
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

- If you want it run in the background
```bash
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties &
```

- Verify its running. *Note*: Default the port of Zookeeper is `2181`.
```bash
sudo lsof -i -P | grep LISTEN | grep :2181
```
*Expected output:* `java      50046      nathanngo  123u  IPv6 0x291901b620edaf97      0t0    TCP *:2181 (LISTEN)`. 

- Then in zookeeper folder you will see `version-2` directory.

## 1.2. Start with Kafka
- Create folder for Zookeeper (any location)
```bash
mkdir data/zookeeper
```

- Change configuration of Kafka to folder that was created
```bash
nano /opt/homebrew/etc/kafka/server.properties
```
Edit `log.dirs=<PATH_TO_KAFKA_FOLDER>`

- Verify its running. *Note*: Default the port of Zookeeper is `9092`.
```bash
sudo lsof -i -P | grep LISTEN | grep :9092
```
*Expected output:* `java      50815      nathanngo  128u  IPv6 0x291901b620eda197      0t0    TCP *:9092 (LISTEN)`. 

# 2. Getting start with Docker
After running Docker compose for creating 2 containers `Zookeeper` and `Kafka`.
- Create `topic` in Docker Container
```bash
docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic <TOPIC_NAME>
```

- Write `message` to the `topic`
```bash
docker exec --interactive --tty broker \
kafka-console-producer --bootstrap-server broker:9092 \
                       --topic quickstart
```
Type in some lines of text. Each line is a new message.
```bash
this is my first kafka message
hello world!
this is my third kafka message. I’m on a roll :-D
```
