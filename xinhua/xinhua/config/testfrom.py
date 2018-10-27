from kafka import KafkaConsumer
consumer = KafkaConsumer('new-article-input')
for msg in consumer:
    print (msg)