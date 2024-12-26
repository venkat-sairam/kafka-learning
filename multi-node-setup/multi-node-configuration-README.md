

# Kafka Commands for Multi-Node Setup

### Topic Management
- Create Topic:
  `docker exec kafka-1 kafka-topics --bootstrap-server kafka-1:9092 --create --topic test-topic --partitions 3 --replication-factor 3`
- List Topics:
  `docker exec kafka-1 kafka-topics --bootstrap-server kafka-1:9092 --list`
- Describe Topic:
  `docker exec kafka-1 kafka-topics --bootstrap-server kafka-1:9092 --describe --topic test-topic`

### Produce and Consume Messages
- Produce Messages:
  `docker exec -it kafka-1 kafka-console-producer --topic test-topic --bootstrap-server kafka-1:9092`
  *(Type messages and press Enter to send)*
- Consume Messages:
  `docker exec -it kafka-1 kafka-console-consumer --topic test-topic --bootstrap-server kafka-1:9092 --from-beginning`

### Offsets and Logs
- Get Offsets:
  `docker exec kafka-1 kafka-run-class kafka.tools.GetOffsetShell --broker-list kafka-1:9092 --topic test-topic --time -1`
- Log Directories:
  `docker exec kafka-1 kafka-log-dirs --bootstrap-server kafka-1:9092 --describe --topic-list test-topic`

### Cluster Health
- Describe Cluster:
  `docker exec kafka-1 kafka-metadata-quorum --bootstrap-server kafka-1:9092 --describe`

### Cleaning Up
- Stop and Remove Kafka Cluster:
  `docker-compose down`
