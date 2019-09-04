## Purpose

Sometimes during building data piplines on Kafka , there is a need to 

- Quickly build test data for data stream testing
- Provide the AWESOMENESS of AVRO to create data records constrained to a Schema(AVRO)

## Initial Setup 

Install self-contained binary  for OSX and Linux:

```
   apt install confluent-kafka
```
Install AvroProducer and AvroConsumer:
```
   pip install confluent-kafka[avro]
```

## Usage

- Replace the *.avsc file with your schema
- Replace the *.csv file with yours
- Run You kafka cluster with the supplied docker-compose.yml ```docker-compose up```
- Run the producer ```python produce.py```




