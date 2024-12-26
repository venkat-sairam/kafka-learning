
### `KAFKA_PROCESS_ROLES`
Specifies the roles the Kafka node will perform.  
**Example**: `broker,controller` means this node acts as both a broker and a controller.

---

### `KAFKA_NODE_ID`
Unique identifier for the node in the Kafka cluster.  
**Example**: `1` for a single-node setup.

---

### `KAFKA_CONTROLLER_QUORUM_VOTERS`
Defines the nodes in the controller quorum using the format `<KAFKA_NODE_ID>@<KAFKA_HOST_IP>:<CONTROLLER_PORT>`.  
**Example**: `1@localhost:9093`.

---

### `KAFKA_LISTENERS`
Specifies the endpoints Kafka listens on. Different listeners handle internal, external, and controller communications.  
**Example**: `PLAINTEXT_INTERNAL://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093`.

---

### `KAFKA_LISTENER_SECURITY_PROTOCOL_MAP`
Maps each listener to a security protocol.  
**Example**: `PLAINTEXT_INTERNAL:PLAINTEXT,PLAINTEXT_EXTERNAL:PLAINTEXT`.

---

### `KAFKA_INTER_BROKER_LISTENER_NAME`
Specifies the listener used for communication between brokers.  
**Example**: `PLAINTEXT_INTERNAL`.

---

### `KAFKA_CONTROLLER_LISTENER_NAMES`
Defines which listener is used for controller communication.  
**Example**: `CONTROLLER`.

---

### `KAFKA_ADVERTISED_LISTENERS`
Specifies the addresses Kafka advertises to clients. These are typically external-facing endpoints.  
**Example**: `PLAINTEXT_INTERNAL://localhost:9092,PLAINTEXT_EXTERNAL://10.0.0.123:9094`.

---

### `CLUSTER_ID`
Unique identifier for the Kafka cluster, required for KRaft mode.  
**Example**: `pX5QmzWzReCbwLCnexuzCw`.

---

### Ports (`KAFKA_HOST_PORT`, `EXTERNAL_HOST_MACHINE_PORT`, `CONTROLLER_PORT`)
Used to define the respective port numbers for internal, external, and controller communications.  

**Examples**:

- `EXTERNAL_HOST_MACHINE_IP=10.0.0.123`
- `EXTERNAL_HOST_MACHINE_PORT=9094`
- `CLUSTER_ID=pX5QmzWzReCbwLCnexuzCw`
- `CONTROLLER_PORT=9093`
- `KAFKA_HOST_IP=localhost`
- `KAFKA_HOST_PORT=9092`
- `KAKFA_BROKER_ID=1`
