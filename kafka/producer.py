from kafka import KafkaProducer


bootstrap_servers = ['localhost:9092']
producer = KafkaProducer()

while True:
    topic_name = input('Enter topic name: ')
    text = input('Enter text: ')
    producer.send(topic_name, text)
