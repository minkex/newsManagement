import json
from kafka import KafkaProducer
if __name__=='__main__':
    producer = KafkaProducer(bootstrap_servers='seu:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('new-docId-input', {
        "time": "hello454545"
    })
    producer.flush()
    print("yes")
'''
producer=KafkaProducer(bootstrap_servers='seu:9092')
for _ in range(5):
    print("jjj")
    producer.send('new-article-input', b'some_message_bytes')
'''