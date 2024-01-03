# Dagster
 
## Onboarding

### What problem does this aim to solve?

Dagster is a data orchestrator that aims to solve the challenges of building, testing, and deploying data pipelines. In the world of data engineering, pipelines are used to extract, transform, and load (ETL) data from various sources into a desired format for analysis or storage. However, building and managing these pipelines can be complex and error-prone. Dagster addresses these challenges by providing a framework for defining, testing, and executing data pipelines in a reliable and scalable manner.

With Dagster, developers can easily define the dependencies between different steps in a pipeline, handle data quality checks, and monitor the execution of pipelines. It also provides a unified interface for managing the configuration and deployment of pipelines, making it easier to collaborate and iterate on data engineering projects.

### What sub-category of technologies is this?

Dagster falls under the sub-category of data engineering tools within the broader field of data processing and analytics. It is specifically designed to address the challenges of building and managing data pipelines, which are a critical component of data engineering workflows. Data engineering tools like Dagster enable developers to efficiently process and transform large volumes of data, ensuring the reliability and quality of the data pipelines.
 
## Developer life with/without this tool

### Without Dagster

#### Data Pipeline Development

Developing data pipelines involves writing custom code to handle data extraction, transformation, and loading (ETL) processes.
Developers need to manually handle error handling, retries, and monitoring.

#### Dependency Management

Managing dependencies between different components of the data pipeline can be challenging.
Developers need to ensure that each component is executed in the correct order and handle dependencies manually.

#### Testing and Validation

Testing and validating data pipelines can be time-consuming and error-prone.
Developers need to write custom tests and validation scripts to ensure the correctness of the pipeline.

#### Monitoring and Observability

Monitoring the execution of data pipelines and gaining insights into their performance can be difficult.
Developers need to implement custom monitoring solutions to track the progress and health of the pipeline.

### With Dagster

#### Declarative Data Pipeline Development

Dagster provides a declarative way to define data pipelines using a Python-based DSL (Domain-Specific Language).
Developers can define the pipeline's structure, dependencies, and error handling in a more intuitive and readable manner.

Example Pipeline Definition:

```python
@solid
def extract_data(context):
    # Extract data from source

@solid
def transform_data(context, data):
    # Transform data

@solid
def load_data(context, transformed_data):
    # Load data to destination

@pipeline
def my_pipeline():
    load_data(transform_data(extract_data()))
```

#### Dependency Management and Execution

Dagster automatically manages the dependencies between different pipeline components.
It ensures that each component is executed in the correct order based on their dependencies.

#### Testing and Validation Framework

Dagster provides a testing and validation framework that simplifies the process of testing data pipelines.
Developers can define test cases and assertions to validate the correctness of the pipeline.

Example Test Case:

```python
@solid
def test_my_pipeline(context):
    # Define test inputs
    inputs = ...

    # Execute the pipeline with test inputs
    result = execute_pipeline(my_pipeline, inputs)

    # Assert the expected outputs
    assert result.success
    assert result.output_for_solid(load_data) == expected_output
```

#### Built-in Monitoring and Observability

Dagster provides built-in monitoring and observability features.
Developers can easily track the progress, health, and performance of the data pipeline using the Dagster UI and integration with other monitoring tools.

Example Dagster UI:

![Dagster UI](dagster_ui.png)

#### Extensibility and Ecosystem

Dagster is highly extensible and integrates well with other tools and frameworks in the data ecosystem.
Developers can leverage existing libraries and frameworks to enhance their data pipelines, such as using Pandas for data transformation or Airflow for scheduling and orchestration.
 
## Core Concepts

### Dagster
Dagster is an open-source data orchestrator that helps you build, test, and operate data pipelines. It provides a unified programming model for defining and executing data workflows, making it easier to manage complex data pipelines.

### Solids
In Dagster, solids are the fundamental building blocks of a data pipeline. A solid represents a unit of computation or a data transformation. It encapsulates a specific piece of logic that takes inputs, performs some processing, and produces outputs. Solids can be combined and connected to form a pipeline.

### Pipeline
A pipeline in Dagster is a collection of connected solids that define the data flow and dependencies between different computations. It represents the entire workflow and orchestrates the execution of solids. Pipelines provide a structured way to organize and manage complex data processing tasks.

### Input and Output
Inputs and outputs are the means by which solids communicate with each other in a Dagster pipeline. Solids can declare inputs that they require from other solids and outputs that they produce. Inputs and outputs define the data dependencies between solids and enable the automatic resolution of those dependencies during pipeline execution.

### Configuration
Configuration in Dagster allows you to parameterize your pipeline and solids. It provides a way to specify inputs, outputs, and behavior of solids at runtime. Configuration values can be used to control the behavior of your pipeline and make it more flexible and reusable. Dagster provides a type system for configuration values, ensuring type safety and validation.

## Core APIs

### `@solid`

- Purpose: Decorator used to define a solid, which is the fundamental unit of computation in Dagster. A solid represents a function or a piece of code that performs a specific task.
- Usage Example:

```python
@solid
def add_numbers(context, num1, num2):
    result = num1 + num2
    context.log.info(fThe sum of {num1} and {num2} is {result})
    return result
```

### `@pipeline`

- Purpose: Decorator used to define a pipeline, which is a collection of solids and their dependencies. A pipeline represents a data processing workflow in Dagster.
- Usage Example:

```python
@pipeline
def my_pipeline():
    add_numbers()
```

### `@input_schema` / `@output_schema`

- Purpose: Decorators used to define the schema of the inputs and outputs of a solid. Schemas define the expected data types and shapes of the inputs and outputs.
- Usage Example:

```python
@solid
@input_schema(Int)
@output_schema(Int)
def double_number(context, num):
    result = num * 2
    context.log.info(fThe double of {num} is {result})
    return result
```

### `@solid_config`

- Purpose: Decorator used to define the configuration schema for a solid. Configuration allows you to parameterize the behavior of a solid without modifying its code.
- Usage Example:

```python
@solid(config_schema={factor: Field(Int, default_value=1)})
def multiply_number(context, num):
    factor = context.solid_config[factor]
    result = num * factor
    context.log.info(fThe product of {num} and {factor} is {result})
    return result
```

### `@resource`

- Purpose: Decorator used to define a resource, which represents an external dependency required by solids in a pipeline. Resources can be used to manage connections to databases, APIs, or other external systems.
- Usage Example:

```python
@resource
def my_database_resource():
    return MyDatabaseConnection()

@solid(required_resource_keys={database})
def query_database(context):
    database = context.resources.database
    # Perform database query
    ...
```
 
## Small Running Example

This section provides a practical example of using Dagster, starting from installation to running a simple pipeline.

### Installation

1. Install Dagster:

- For macOS and Linux:
  - Open a terminal.
  - Run the following command to install Dagster:
  ```
  pip install dagster
  ```
- For Windows:
  - Open a command prompt.
  - Run the following command to install Dagster:
  ```
  pip install dagster
  ```

2. Verify Installation:

- Open a terminal or command prompt.
- Run `dagster --version` to ensure Dagster is installed correctly.

### Code

Now that Dagster is installed, let's create a simple pipeline that reads data from a CSV file and writes it to a PostgreSQL database.

1. Create a New Directory:

    Make a new directory and navigate into it.

2. Create a Python File:

    Create a new Python file named `my_pipeline.py` with the following content:

    ```python
    import os
    from dagster import pipeline, solid, InputDefinition, OutputDefinition, execute_pipeline
    import pandas as pd
    from sqlalchemy import create_engine

    @solid(
        input_defs=[InputDefinition(name=csv_path, dagster_type=str)],
        output_defs=[OutputDefinition(name=dataframe, dagster_type=pd.DataFrame)],
    )
    def read_csv(context, csv_path):
        dataframe = pd.read_csv(csv_path)
        return dataframe

    @solid(
        input_defs=[InputDefinition(name=dataframe, dagster_type=pd.DataFrame)],
        output_defs=[OutputDefinition(name=success, dagster_type=bool)],
    )
    def write_to_postgres(context, dataframe):
        engine = create_engine(postgresql://username:password@localhost:5432/mydatabase)
        dataframe.to_sql(mytable, engine, if_exists=replace, index=False)
        return True

    @pipeline
    def my_pipeline():
        dataframe = read_csv()
        write_to_postgres(dataframe)

    if __name__ == __main__:
        csv_path = os.path.join(os.getcwd(), data.csv)
        execute_pipeline(my_pipeline, {solids: {read_csv: {inputs: {csv_path: csv_path}}}})
    ```

3. Create a CSV File:

    In the same directory, create a file named `data.csv` and populate it with some data.

4. Update PostgreSQL Connection Details:

    Replace `username`, `password`, and `mydatabase` in the `create_engine` function with your PostgreSQL connection details.

5. Run the Pipeline:

    In your terminal or command prompt, navigate to the directory containing `my_pipeline.py` and run the following command:

    ```bash
    dagster pipeline execute -f my_pipeline.py
    ```

    This will execute the pipeline, reading the data from the CSV file and writing it to the PostgreSQL database.

6. Verify Data in PostgreSQL:

    Connect to your PostgreSQL database and check if the data from the CSV file has been successfully written to the `mytable` table.
