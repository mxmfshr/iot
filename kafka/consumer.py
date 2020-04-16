from kafka import KafkaConsumer

bootstrap_servers = ['localhost:9092']
TOPIC_NAME = 'test'
GROUP_ID = 'group1'

consumer = KafkaConsumer(TOPIC_NAME, GROUP_ID, bootstrap_servers)
for m in consumer:
    print(f"{m.topic}: {m.value}")
