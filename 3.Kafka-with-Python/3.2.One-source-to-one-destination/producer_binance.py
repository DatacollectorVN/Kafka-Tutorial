#!/usr/bin/env python
import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from kafka import KafkaProducer
import requests
from datetime import datetime
import json
                         


def message_handler_btc(message):
    if len(message) == 8:
        now = datetime.strftime(
                                datetime.now(),
                                "%Y-%m-%dT%H:%M:%S"
                                )
        data = {
                'coin': 'btc',
                'price': message['P'], 
                'time': now
                }
        print(data)
        producer.send('binance', value=data)

def message_handler_eth(message):
    if len(message) == 8:
        now = datetime.strftime(
                                datetime.now(),
                                "%Y-%m-%dT%H:%M:%S"
                                )
        data = {
                'coin': 'eth',
                'price': message['P'], 
                'time': now
                }
        print(data)
        producer.send('binance', value=data)



def main():
    global producer
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
                         client_id='producer_1',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    config_logging(logging, logging.DEBUG)
    my_client = UMFuturesWebsocketClient()
    my_client.start()

    my_client.mark_price(
        symbol="btcusdt",
        id=13,
        speed=1,
        callback=message_handler_btc,
    )

    my_client.mark_price(
        symbol="ethusdt",
        id=14,
        speed=1,
        callback=message_handler_eth,
    )

    time.sleep(30)
    logging.debug("closing ws connection")
    my_client.stop()
    producer.close()

if __name__ == "__main__":
    main()