# Kafka-Tutorial
## Kafka CLI
Source: [here](https://kafka.apache.org/quickstart).

### 1. Topic:
- Create topic. Create topic name with 4 required options:
```bash
--bootstrap-server: Kafka server address.
--topic: name of topic
--partitions: number partitions
--replication-factor: number replication for each partition
```
*Note:* that it is not possible to create a volume broker process in a network cluster. Since broker 1 holds up to 2 partitions the following doesn't make sense at all, let's do it for example, the replication factor can only = 1.

Example:
```bash
 kafka-topics \
    --bootstrap-server localhost:9092 \
    --topic my-first-topic \
    --create \
    --partitions 3 \
    --replication-factor 1
```

- list all exist topics.
```bash
kafka-topics \
    --bootstrap-server localhost:9092 \
    --list
```

- Get information in topic.

You can use `--describe` if you want to see more information
```bash
kafka-topics.sh \
    --bootstrap-server localhost:9092 \
    --topic my-first-topic \
    --describe
```

- Delete topic. Use `--delete`.
```bash
kafka-topics.sh \
    --bootstrap-server localhost:9092 \
    --topic my-first-topic \
    --delete
```

### 2. Producer:
- Create producer for writing message
```bash
kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic my-first-topic
>
```
The output above means you create sucessfully producer and start to write message. `Ctrl + C` to terminate producer.

*Note:* In the case create producer to send message for not exist topic. Then Kafka will create the new topic with default configuration. We can change default config  in file `server.properties`.

### 3. Consumer
- Create consumer for reading message from topic
```bash
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my-first-topic
```

And we do not see any output. Why ?. Because if just consume the message at the time the consumer was created.