from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import csv


value_schema = avro.load('/home/work/src/avroproducer/arlncsvsource.avsc')

AvroProducerConf = {'bootstrap.servers': 'localhost:9092',
                                       'schema.registry.url': 'http://localhost:8081',
                                     }

avroProducer = AvroProducer(AvroProducerConf, default_value_schema=value_schema)

with open('/home/work/src/avroproducer/test.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
       print(row)
       avroProducer.produce(topic='mein_topic', value=row)
       avroProducer.flush()
