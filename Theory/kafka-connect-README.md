
# Kafka Connect: README

## Overview
Kafka Connect is a powerful framework in the Apache Kafka ecosystem for integrating external systems with Kafka. It simplifies the process of streaming data **into Kafka topics (Source Connectors)** and **out of Kafka topics (Sink Connectors)** without requiring custom code.

This README provides an overview of Kafka Connect, its components, and steps to set it up for real-time streaming applications.

---

## Key Features
- **Source Connectors**: Stream data from external systems (e.g., databases, file systems) into Kafka.
- **Sink Connectors**: Stream data from Kafka topics to target systems (e.g., databases, cloud storage).
- **Scalable & Fault-Tolerant**: Supports distributed mode for high availability.
- **Pre-Built Connectors**: Includes plugins for popular systems like MySQL, PostgreSQL, Elasticsearch, and S3.
- **Configuration-Driven**: No custom coding required; connectors are set up with configuration files.

---

## How It Works
1. **Source Connector**: Reads data from an external system and publishes it to Kafka topics.
2. **Kafka Topics**: Acts as the intermediary buffer for real-time data.
3. **Sink Connector**: Reads data from Kafka topics and writes it to a target system.
4. **Worker Nodes**: Manages the lifecycle of connectors and distributes tasks for scalability.

---

## Modes of Operation
- **Standalone Mode**:
  - Single-node setup.
  - Ideal for development or small workloads.

- **Distributed Mode**:
  - Multi-node setup.
  - Used in production environments for high availability and scalability.

---

## Setting Up Kafka Connect

### Prerequisites
1. Apache Kafka installed and running.
2. External systems (e.g., databases or storage) configured.
3. Connector plugins installed (if required).

### Steps to Install and Configure

#### 1. Install Kafka Connect
Kafka Connect is bundled with Apache Kafka. To start it:
```bash
bin/connect-distributed.sh config/connect-distributed.properties
```

#### 2. Create a Connector Configuration
Example configuration for a **File Source Connector**:
```properties
name=file-source
connector.class=FileStreamSource
tasks.max=1
file=/tmp/input.txt
topic=file-input-topic
```
Save this configuration as `file-source.properties`.

#### 3. Deploy the Connector
Deploy the connector using the REST API:
```bash
curl -X POST -H "Content-Type: application/json" --data @file-source.properties http://localhost:8083/connectors
```

#### 4. Monitor the Connector
Use the REST API to check the status:
```bash
curl -X GET http://localhost:8083/connectors/file-source/status
```

---

## Popular Use Cases
1. **Database to Kafka**:
   - Use the **Debezium Source Connector** to stream database changes (CDC) into Kafka.

2. **Log Processing**:
   - Use the **File Source Connector** to stream log files into Kafka topics for processing.

3. **Cloud Storage**:
   - Use the **Amazon S3 Sink Connector** to store Kafka data in S3 for long-term analytics.

4. **Search Indexing**:
   - Use the **Elasticsearch Sink Connector** to populate search indices with Kafka topic data.

---

## Example Workflow
1. **Input**:
   - Source Connector streams data from a MySQL database into Kafka topics.
2. **Processing**:
   - Kafka topic acts as a buffer for real-time data.
3. **Output**:
   - Sink Connector pushes the data from Kafka topics to Amazon S3.

---

## Example: File Source to S3 Sink

### File Source Connector Configuration
```properties
name=file-source
connector.class=FileStreamSource
tasks.max=1
file=/tmp/input.txt
topic=file-input-topic
```

### S3 Sink Connector Configuration
```properties
name=s3-sink
connector.class=io.confluent.connect.s3.S3SinkConnector
tasks.max=1
topics=file-input-topic
s3.bucket.name=my-kafka-bucket
s3.region=us-east-1
```

---

## Monitoring and Maintenance
1. **Monitoring Connectors**:
   - Use Kafka Connect REST API or tools like Confluent Control Center.

2. **Scaling Connectors**:
   - Increase `tasks.max` to parallelize the work across workers.

3. **Error Handling**:
   - Use Kafka Dead Letter Queues (DLQs) to handle failed records.

---

## Advantages of Kafka Connect
- Eliminates the need for custom producer/consumer code.
- Simplifies integration with external systems.
- Scales easily for high-throughput use cases.

---

## Useful Links
- [Kafka Connect Documentation](https://kafka.apache.org/documentation/#connect)
- [Confluent Hub for Pre-Built Connectors](https://www.confluent.io/hub/)
- [Debezium Documentation](https://debezium.io/documentation/)

