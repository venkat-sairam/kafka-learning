# Kafka 3-Node Cluster Architecture

This document explains the architecture and configuration of a 3-node Kafka cluster using Docker Compose. It includes a breakdown of each component, how they interact, and an analogy using Starbucks to clarify the concepts. This setup assumes PLAINTEXT communication (without encryption).

---

## **Overview of the Kafka Cluster**

### **Cluster Components**:
1. **Kafka Brokers**: Three nodes act as brokers, each responsible for handling data, coordinating with other brokers, and managing partitions and replicas.
2. **Controllers**: Kafka's KRaft mode enables brokers to also act as controllers, eliminating the need for ZooKeeper.
3. **Clients**: Producers and consumers interact with the brokers to send and retrieve messages.

### **Key Features**:
- **3 Brokers** for fault tolerance and high availability.
- **KRaft Mode**: Handles metadata management without ZooKeeper.
- **Replication Factor**: Ensures data redundancy across brokers.
- **PLAINTEXT Communication**: Used for simplicity in this example.

---

## **Configuration Details**

### **Kafka Broker Configurations in Detail**

#### 1. **ALLOW_ANONYMOUS_LOGIN=yes**
- This setting allows clients to connect to Kafka brokers without authentication.

#### 2. **KAFKA_ENABLE_KRAFT=yes**
- Enables Kafka to operate in KRaft mode, eliminating the need for ZooKeeper.
- KRaft mode makes brokers self-sufficient, managing metadata and cluster state internally.

#### 3. **KAFKA_CFG_PROCESS_ROLES=broker,controller**
- Configures the broker to perform dual roles:
  - **Broker**: Handles data storage and communication with producers and consumers.
  - **Controller**: Manages metadata, assigns partition leadership, and coordinates cluster-wide operations.
- Having brokers act as controllers simplifies the architecture, especially in smaller clusters.

#### 4. **KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER**
- Specifies the listener name for controller communication.
- This is used internally for brokers and controllers to exchange cluster management information.

#### 5. **KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=kraft:PLAINTEXT,CONTROLLER:PLAINTEXT,INTERNAL:PLAINTEXT**
- Maps listeners to their respective security protocols.
  - **kraft**: Used for client-to-broker communication.
  - **CONTROLLER**: Used for controller-to-broker and controller-to-controller communication.
  - **INTERNAL**: Used for inter-broker communication.
- In this configuration, all protocols are set to PLAINTEXT for simplicity.

#### 6. **KAFKA_BROKER_ID**
- A unique identifier for each broker in the cluster.
- Examples:
  - `KAFKA_BROKER_ID=1` for the first broker.
  - `KAFKA_BROKER_ID=2` for the second broker.
  - `KAFKA_BROKER_ID=3` for the third broker.

#### 7. **KAFKA_CFG_CONTROLLER_QUORUM_VOTERS**
- Defines the quorum of controllers that manage the cluster.
- Example: `1@kafka-1:9094,2@kafka-2:9094,3@kafka-3:9094`
- Ensures high availability for metadata management, as a majority of controllers must be available for operations.

#### 8. **KAFKA_KRAFT_CLUSTER_ID**
- A unique identifier for the Kafka cluster.
- This ID ties all brokers together into a single logical cluster.
- Generated using the `kafka-storage.sh random-uuid` command.

#### 9. **KAFKA_CFG_KRAFT_REPLICATION_FACTOR**
- Specifies the number of replicas for each partition in the cluster.
- A replication factor of `3` ensures that each partition has one leader and two replicas, improving fault tolerance.

#### 10. **KAFKA_CFG_ADVERTISED_LISTENERS**
- Defines the network addresses that brokers advertise to clients and other brokers.
- Example: `kraft://:9093,INTERNAL://kafka-1:9092`
  - `kraft://`: Used by clients to connect to the broker.
  - `INTERNAL://`: Used by other brokers for replication and coordination.

#### 11. **KAFKA_CFG_LISTENERS**
- Specifies the actual network addresses and ports on which the broker listens for incoming connections.
- Example: `kraft://:9093,CONTROLLER://kafka-1:9094,INTERNAL://:9092`
  - `kraft://`: For client-to-broker communication.
  - `CONTROLLER://`: For controller communication.
  - `INTERNAL://`: For inter-broker communication.

#### 12. **KAFKA_CFG_INTER_BROKER_LISTENER_NAME=INTERNAL**
- Specifies the listener to be used for inter-broker communication.
- Ensures that replication and coordination between brokers are handled efficiently.

#### 13. **KAFKA_CFG_DEFAULT_REPLICATION_FACTOR**
- Sets the default replication factor for new topics created in the cluster.
- A value of `3` ensures that all topics have at least three copies of their data, distributed across brokers.

---

### **Docker Compose Services**
Each Kafka broker is defined as a separate service in the `docker-compose.yml`. Below are the key configurations:

### **Kafka Broker 1 (`kafka-1`)**
```yaml
image: "bitnami/kafka:3.4.0"
container_name: kafka1
hostname: kafka-1
environment:
  - ALLOW_ANONYMOUS_LOGIN=yes
  - KAFKA_ENABLE_KRAFT=yes
  - KAFKA_CFG_PROCESS_ROLES=broker,controller
  - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
  - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=kraft:PLAINTEXT,CONTROLLER:PLAINTEXT,INTERNAL:PLAINTEXT
  - KAFKA_BROKER_ID=1
  - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka-1:9094,2@kafka-2:9094,3@kafka-3:9094
  - ALLOW_PLAINTEXT_LISTENER=yes
  - KAFKA_KRAFT_CLUSTER_ID=EATEPCK6RZq-1b9ipL2WFA
  - KAFKA_CFG_KRAFT_REPLICATION_FACTOR=3
  - KAFKA_CFG_NODE_ID=1
  - KAFKA_CFG_ADVERTISED_LISTENERS=kraft://:9093,INTERNAL://kafka-1:9092
  - KAFKA_CFG_LISTENERS=kraft://:9093,CONTROLLER://kafka-1:9094,INTERNAL://:9092
  - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=INTERNAL
  - KAFKA_CFG_DEFAULT_REPLICATION_FACTOR=3
ports:
  - "9101:9092"
  - "9102:9093"
  - "9103:9094"
volumes:
  - kafka1-data:/bitnami/kafka
```

---

## **How the Kafka Cluster Works**

### **Communication**
- **Client-to-Broker Communication**:
  - Clients (producers/consumers) connect to brokers using the `kraft://` listener (e.g., `9093`).
- **Inter-Broker Communication**:
  - Brokers communicate with each other for replication and coordination using the `INTERNAL://` listener (e.g., `9092`).
- **Controller Communication**:
  - Controllers coordinate metadata updates and partition leadership via the `CONTROLLER://` listener (e.g., `9094`).

### **Controller Quorum**
- All three brokers act as controllers and participate in the quorum:
  ```yaml
  KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka-1:9094,2@kafka-2:9094,3@kafka-3:9094
  ```
- This ensures high availability for metadata management.

### **Replication**
- **Replication Factor**:
  - Each partition is replicated across 3 brokers.
  - Ensures data availability even if one broker fails.

---

## **Real-World Example: Starbucks Analogy**

### Starbucks Store Setup
Imagine a Starbucks with:
1. **Three Service Counters**: Represent the three Kafka brokers.
2. **Team Managers**: Represent the controllers managing the counters.
3. **Customers**: Represent producers and consumers.

### Communication in Starbucks
1. **Customer to Counter Communication**:
   - Customers place orders (producers) or pick up drinks (consumers) at a specific counter (broker).
2. **Counter to Counter Communication**:
   - Counters share information (replication), such as stock levels or new menu items.
3. **Manager to Counter Communication**:
   - Managers (controllers) assign tasks like "Counter 1 handles espresso orders."

### High Availability
- If one counter (broker) is unavailable, the other counters continue serving customers.
- Orders (messages) are replicated across counters, so no orders are lost.

---

## **How to Run the Kafka Cluster**

### Step 1: Start the Cluster
Run the following command to bring up the Kafka cluster:
```bash
docker-compose up
```

### Step 2: Verify the Cluster
- Check that all three brokers are running using:
  ```bash
  docker ps
  ```
- View logs for a specific broker:
  ```bash
  docker logs kafka1
  ```

### Step 3: Test the Cluster
- Use Kafka CLI tools or a client application to:
  - Create topics.
  - Produce and consume messages.


