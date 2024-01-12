# Apache kafka
 
## Onboarding

### What problem does this aim to solve?

Apache Kafka addresses the challenge of building scalable, fault-tolerant, and real-time data streaming applications. Traditional messaging systems often struggle to handle high volumes of data and provide low-latency processing. Additionally, they may lack the ability to handle failures gracefully and ensure data consistency. Kafka solves these problems by providing a distributed, fault-tolerant, and highly scalable platform for building real-time data pipelines and streaming applications.

### What sub-category of technologies is this?

Apache Kafka falls under the sub-category of "stream processing" within the broader field of data engineering and data processing. It is a distributed streaming platform that allows developers to publish and subscribe to streams of records, store them in a fault-tolerant way, and process them in real-time. Kafka is commonly used for building event-driven architectures, real-time analytics, log aggregation, and data integration pipelines.
 
## Developer life with/without this tool

### Without Apache Kafka

#### Message Passing

Developers need to implement their own custom message passing system to enable communication between different components of a distributed system.
This can be time-consuming and error-prone, as developers need to handle message routing, delivery guarantees, and fault tolerance.

#### Scalability and Performance

Scaling a system to handle high volumes of data and concurrent requests can be challenging without a dedicated message streaming platform.
Developers need to design and implement their own solutions for handling data partitioning, load balancing, and fault tolerance.

#### Data Integration

Integrating data from multiple sources and systems requires custom code to handle data transformation, synchronization, and consistency.
Developers need to build and maintain complex data pipelines to ensure data is delivered reliably and in a timely manner.

### With Apache Kafka

#### Distributed Messaging System

Apache Kafka provides a distributed messaging system that simplifies the communication between different components of a distributed system.
Developers can use Kafka's publish-subscribe model to send and receive messages, ensuring reliable delivery and fault tolerance.

Example code for producing a message:

```java
ProducerRecord<String, String> record = new ProducerRecord<>("my-topic", "key", "value");
producer.send(record);
```

Example code for consuming messages:

```java
ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
for (ConsumerRecord<String, String> record : records) {
    System.out.println("Received message: " + record.value());
}
```

#### Scalability and Performance

Kafka is designed to handle high volumes of data and concurrent requests.
It provides built-in support for data partitioning, load balancing, and fault tolerance, allowing developers to easily scale their systems.

#### Stream Processing

Kafka's integration with Apache Kafka Streams allows developers to process and analyze data in real-time.
Developers can build stream processing applications that consume data from Kafka topics, perform transformations, aggregations, and join operations, and produce results to other Kafka topics.

Example code for stream processing:

```java
KStream<String, String> stream = builder.stream("input-topic");
stream.filter((key, value) -> value.contains("important"))
      .mapValues(value -> value.toUpperCase())
      .to("output-topic");
```

#### Data Integration

Apache Kafka acts as a central data hub, enabling easy integration of data from multiple sources and systems.
Developers can use Kafka Connect to build and manage data pipelines, simplifying the process of ingesting and delivering data to various systems.

Example configuration for a Kafka Connect source connector:

```properties
name=my-source-connector
connector.class=org.apache.kafka.connect.jdbc.JdbcSourceConnector
tasks.max=1
connection.url=jdbc:mysql://localhost:3306/my-database
topic.prefix=my-topic-
```

#### Real-time Analytics

Kafka's integration with Apache Kafka Streams and other analytics frameworks allows developers to perform real-time analytics on streaming data.
Developers can build applications that process and analyze data as it flows through Kafka, enabling real-time insights and decision-making.

Example code for real-time analytics:

```java
KStream<String, String> stream = builder.stream("input-topic");
stream.groupByKey()
      .windowedBy(TimeWindows.of(Duration.ofMinutes(5)))
      .count()
      .toStream()
      .foreach((windowedKey, count) -> System.out.println("Count for window " + windowedKey + ": " + count));
```

Overall, Apache Kafka simplifies the development of distributed systems by providing a reliable messaging platform, scalability and performance optimizations, stream processing capabilities, data integration tools, and real-time analytics support.
 
## Core Concepts

### Topics
In Apache Kafka, a topic is a category or feed name to which messages are published. It represents a stream of records, where each record consists of a key, a value, and a timestamp. Topics are partitioned and replicated across a cluster of Kafka brokers to provide fault tolerance and scalability.

### Producers
Producers in Apache Kafka are responsible for publishing messages to Kafka topics. They write records to a specific topic and can choose to include a key with each record. Producers can also specify a partition or let Kafka automatically assign one. They provide high throughput and fault tolerance by buffering and batching messages before sending them to Kafka.

### Consumers
Consumers in Apache Kafka read messages from Kafka topics. They subscribe to one or more topics and consume records in the order they were written. Consumers can be part of a consumer group, where each consumer in the group reads from a different subset of partitions. This allows for parallel processing of messages and load balancing across consumers.

### Partitions
Partitions are the fundamental unit of parallelism in Apache Kafka. Each topic is divided into one or more partitions, and each partition is ordered and immutable. Partitions allow for horizontal scalability and parallel processing of messages. They also determine the level of parallelism and the maximum throughput that can be achieved when consuming or producing messages.

### Brokers
Brokers are the servers that form a Kafka cluster. They are responsible for storing and replicating the topic partitions. Each broker can handle multiple partitions and acts as a leader for some partitions and a follower for others. Brokers communicate with producers and consumers, handle data replication, and ensure fault tolerance and high availability in the Kafka cluster.
 
## Core APIs

### `kafka-topics.sh`

- Purpose: Creates, lists, or deletes Kafka topics.
- Usage Examples:

```bash
# Create a new topic
kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List all topics
kafka-topics.sh --list --bootstrap-server localhost:9092

# Delete a topic
kafka-topics.sh --delete --topic my-topic --bootstrap-server localhost:9092
```

### `kafka-console-producer.sh`

- Purpose: Publishes messages to a Kafka topic from the command line.
- Usage Example:

```bash
# Publish a message to a topic
kafka-console-producer.sh --topic my-topic --bootstrap-server localhost:9092
> Hello, Kafka!
```

### `kafka-console-consumer.sh`

- Purpose: Consumes messages from a Kafka topic and displays them on the command line.
- Usage Example:

```bash
# Consume messages from a topic
kafka-console-consumer.sh --topic my-topic --bootstrap-server localhost:9092 --from-beginning
```

### `kafka-configs.sh`

- Purpose: Manages and inspects Kafka configurations.
- Usage Examples:

```bash
# List all configurations for a topic
kafka-configs.sh --describe --topic my-topic --bootstrap-server localhost:9092

# Add a configuration to a topic
kafka-configs.sh --alter --topic my-topic --bootstrap-server localhost:9092 --add-config max.message.bytes=1048576

# Delete a configuration from a topic
kafka-configs.sh --alter --topic my-topic --bootstrap-server localhost:9092 --delete-config max.message.bytes
```

### `kafka-consumer-groups.sh`

- Purpose: Lists, describes, or resets consumer group offsets.
- Usage Examples:

```bash
# List all consumer groups
kafka-consumer-groups.sh --list --bootstrap-server localhost:9092

# Describe a consumer group
kafka-consumer-groups.sh --describe --group my-group --bootstrap-server localhost:9092

# Reset consumer group offsets to a specific position
kafka-consumer-groups.sh --reset-offsets --group my-group --topic my-topic --to-offset 0 --bootstrap-server localhost:9092 --execute
```
 
## Small Running Example

This section provides a practical example of using Apache Kafka, starting from installation to running a simple application.

### Installation

1. Install Apache Kafka:

- Download Apache Kafka from the Apache Kafka website.
- Extract the downloaded file to a directory of your choice.

2. Start the ZooKeeper Server:

- Open a terminal or command prompt.
- Navigate to the Kafka directory.
- Start the ZooKeeper server by running the following command:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

3. Start the Kafka Server:

- Open a new terminal or command prompt.
- Navigate to the Kafka directory.
- Start the Kafka server by running the following command:

```bash
bin/kafka-server-start.sh config/server.properties
```

4. Create a Topic:

- Open a new terminal or command prompt.
- Navigate to the Kafka directory.
- Create a new topic named "my-topic" by running the following command:

```bash
bin/kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Code

Now that Kafka is installed and the topic is created, let's write a simple producer and consumer application.

1. Create a Producer:

- Open a text editor and create a file named `producer.py`.
- Add the following code to the file:

```python
from kafka import KafkaProducer

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a message to the "my-topic" topic
producer.send('my-topic', b'Hello, Kafka!')

# Flush the producer to ensure the message is sent
producer.flush()

# Close the producer
producer.close()
```

2. Create a Consumer:

- Open a text editor and create a file named `consumer.py`.
- Add the following code to the file:

```python
from kafka import KafkaConsumer

# Create a Kafka consumer
consumer = KafkaConsumer('my-topic', bootstrap_servers='localhost:9092')

# Consume messages from the "my-topic" topic
for message in consumer:
    print(message.value.decode())

# Close the consumer
consumer.close()
```

3. Run the Producer:

- Open a terminal or command prompt.
- Navigate to the directory containing `producer.py`.
- Run the following command to execute the producer:

```bash
python producer.py
```

4. Run the Consumer:

- Open a new terminal or command prompt.
- Navigate to the directory containing `consumer.py`.
- Run the following command to execute the consumer:

```bash
python consumer.py
```

5. Verify Output:

- Check the terminal or command prompt running the consumer. You should see the message "Hello, Kafka!" printed.

Congratulations! You have successfully created a simple producer and consumer application using Apache Kafka.