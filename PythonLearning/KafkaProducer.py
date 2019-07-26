from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(0, 1000):
    data = {'number' : e}
    producer.send('numtest', value=data, partition = 0)
    print('Sent message: {}'.format(data))
    # print(data)    
    sleep(5)
