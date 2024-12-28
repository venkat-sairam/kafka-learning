


![Screenshot from 2024-12-27 19-00-04](https://github.com/user-attachments/assets/103504f1-b1f9-4d70-b97a-2e20282f3877)



# Schema Registry in Kafka

A **Schema Registry** is a central repository that stores and manages schemas for data serialization and deserialization. It ensures consistency and compatibility between producers and consumers in Kafka-based systems by defining the structure of the data (e.g., field names, data types, optional fields). The Schema Registry allows for seamless communication between producers and consumers by maintaining schema compatibility and enabling schema evolution.

---

## Why Do We Need Schema Registry?

1. **Data Consistency**:
   - Ensures producers and consumers agree on the structure of the data, avoiding errors due to incompatible fields.

2. **Version Control**:
   - Manages schema versions, enabling schema evolution without breaking existing systems.
   - Assigns a **Schema ID** for each schema, ensuring compatibility checks.

3. **Serialization Efficiency**:
   - Sends only a **Schema ID** with the data, reducing payload size and network overhead.
   - Consumers retrieve the schema from the registry based on the Schema ID.

4. **Schema Evolution**:
   - Allows for controlled schema changes while maintaining compatibility between producers and consumers.

---

## Schema Evolution: Forward and Backward Compatibility

### Forward Compatibility

- **Definition**: New producers use an updated schema, but older consumers can still process the data using the old schema.
- **Rules**:
  - Adding new optional fields is allowed.
  - Removing fields or changing field types is not allowed.
- **Use Case**: Rolling out new producer features while maintaining support for older consumers.

#### Example:
**Schema v1**:
```json
{
  "name": "string",
  "age": "int"
}

Schema v2 (forward-compatible):

{
  "name": "string",
  "age": "int",
  "address": "string"
}
```
Backward Compatibility

Definition: Older producers write data using the old schema, but new consumers can process it using the updated schema.

Rules:
   - Adding new fields with default values is allowed.
   - Removing optional fields is allowed.
   - Changing field types is not allowed.
     
Use Case: Upgrading consumers while older producers are still operational.

Example:
```json
Schema v2:

{
  "name": "string",
  "age": "int",
  "address": "string"
}

Schema v1 (backward-compatible):

{
  "name": "string",
  "age": "int"
}
```
### How Schema Registry Works

**Producers:**
 - Serialize data using a schema and send it to Kafka topics with a Schema ID.
 - Register new schemas with the Schema Registry if necessary.

**Schema Registry:**
  - Stores a mapping of Schema IDs to schemas and ensures compatibility checks for schema evolution.

**Consumers**:
  - Retrieve the schema using the Schema ID from the Schema Registry.
  - Deserialize data using the retrieved schema.

### Advantages of Using Schema Registry

  - Centralized Schema Management:
      Simplifies schema tracking and ensures consistency.

 - Data Validation:
      Ensures all messages conform to the defined schema.

  - Compatibility Guarantees:
      Supports schema evolution with forward and backward compatibility.

 - Reduced Payload Size:
      Sends only Schema IDs with the data, reducing message size.
