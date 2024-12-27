
---

### Acknowledgment Settings for Kafka Producers

Producers can choose how Kafka confirms the delivery of messages using three acknowledgment levels:

    acks=0 (No acknowledgment): 
    
    The producer sends the message and does not wait for confirmation.
    It doesn’t verify if the message was received.

    acks=1 (Leader acknowledgment): 
    
    The producer waits for a confirmation from the leader broker of the topic partition.
    Once the leader confirms receipt, the message is considered delivered.

    acks=all (Replica acknowledgment): 
    
    The producer waits until all in-sync replicas confirm receipt. 
    This ensures maximum data safety but may increase delay.


![image](https://github.com/user-attachments/assets/2eb7f1ba-8cc7-46c0-bcb4-daa3828ee7c6)

source: [GitHub](https://github.com/SatadruMukherjee/Data-Preprocessing-Models/blob/main/Kafka%20Producer%20Internals.png)
