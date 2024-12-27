from kafka import KafkaProducer # type: ignore
from json import dumps

topic_name = 'test-topic'


# Sending data to a particular partition
try:
    
    payload={'name':"venkat"}

    
    print(f"Sending message to Kafka topic '{topic_name}': {payload}")
    producer = KafkaProducer(
    bootstrap_servers=['10.0.0.123:9094', '10.0.0.123:9194', '10.0.0.123:9294'],
    value_serializer=lambda x: dumps(x).encode('utf-8')

)

    future = producer.send(topic= topic_name, value=payload, partition=3)
    
    result = future.get(timeout=10)
    print(f"Message metadata: {result.topic}, partition: {result.partition}, offset: {result.offset}")

    payload={'name':"sairam"}

    
    print(f"Sending message to Kafka topic '{topic_name}': {payload}")

    future = producer.send(topic= topic_name, value=payload, partition=3)

    producer.flush()  
    print("Message sent successfully!")
except Exception as e:
    print(f"Error sending message: {e}")
finally:
    
    producer.close()



try:
    
    payload={'name':"venkat"}

    
    print(f"Sending message to Kafka topic '{topic_name}': {payload}")
    
    producer = KafkaProducer(
    bootstrap_servers=['10.0.0.123:9094', '10.0.0.123:9194', '10.0.0.123:9294'],
    value_serializer=lambda x: dumps(x).encode('utf-8')

)
    future = producer.send(topic= topic_name, value=payload, key=b'name')
    
    result = future.get(timeout=10)
    print(f"Message metadata: {result.topic}, partition: {result.partition}, offset: {result.offset}")

    producer.flush()  
    print("Message sent successfully!")
except Exception as e:
    print(f"Error sending message: {e}")
finally:
    
    producer.close()


'''
When the key is same, producer writes the messages to the same partition.

'''
#############################  Same Key OUTPUT  ###############################

# Sending message to Kafka topic 'test-topic': {'name': 'venkat'}
# Message metadata: test-topic, partition: 2, offset: 1
# Message sent successfully!


# Sending message to Kafka topic 'test-topic': {'name': 'venkat'}
# Message metadata: test-topic, partition: 2, offset: 2
# Message sent successfully!

#################################################################################


# Sending data using a custom partitioner

def modulus_partitioner(key, all_partitions, available):
    print(f"key = {key}")
    print(f"total partitions: {all_partitions}")

    decoded_key = int(key.decode('utf-8'))
    print(f"decoded-key = {decoded_key}")

    partition = decoded_key % len(all_partitions)
    print(f"Chosen partition: {partition}")
    return partition


def on_send_success(record_metadata):
    print(f"Message sent to {record_metadata.topic}, partition {record_metadata.partition}, offset {record_metadata.offset}")

def on_send_error(excp):
    print(f"Error: {excp}")

producer = KafkaProducer(
    bootstrap_servers=['10.0.0.123:9094', '10.0.0.123:9194', '10.0.0.123:9294'],
    partitioner=modulus_partitioner,
    key_serializer=lambda k: k.encode('utf-8'),  
    value_serializer=lambda v: v.encode('utf-8') 
)

producer.send(topic_name, key='1', value='yvvenkat').add_callback(on_send_success).add_errback(on_send_error)

producer.flush()

########################## Custom Partition Output ######################

# Chosen partition: 1
# Message sent to test-topic, partition 1, offset 3

# Chosen partition: 1
# Message sent to test-topic, partition 1, offset 4

##########################################################################
