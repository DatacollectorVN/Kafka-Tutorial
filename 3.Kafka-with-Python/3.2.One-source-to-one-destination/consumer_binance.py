from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads, dumps
import requests
url = "<TABLE_STREAMING_API>"

headers = {
  "Content-Type": "application/json"
  }
def main():
    
    global consumer, client
    client = MongoClient('localhost:27017')
    collection = client.binance.binance
    consumer = KafkaConsumer(
        'binance',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    for message in consumer:
        message = message.value
        print(message)
        result = requests.request(
            method="POST",
            url=url,
            headers=headers,
            data=dumps(message)
        )
        print(result)
        collection.insert_one(message)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:    
        consumer.close()
        client.close()
