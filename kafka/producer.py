from kafka import KafkaProducer

topicName = input('Enter topic name: ')
text = input('Enter text: ')

bootstrap_servers = ['localhost:9092']
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

ack = producer.send(topicName, text)
metadata = ack.get()

print(metadata.topic)
print(metadata.partition)
