
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

---
###  linger.ms property
The linger.ms setting in Kafka producers determines how long the producer should wait before sending a batch of messages ONLY when the producer I/O thread is free.

Immediate Sending:

    - linger.ms=0
    - Messages are sent to the broker as soon as they are available.
    - There is no intentional delay to accumulate more messages into a batch.
---
### Buffer Memory, max block ms and Producer IO:

- Default buffer memory size =32MB
- If the producer is sending data but the I/O thread cannot process it or the message buffer is full, 
the producer's `send` method will block for up to the duration specified by `max.block.ms`.
