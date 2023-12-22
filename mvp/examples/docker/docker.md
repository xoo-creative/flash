# Docker

## Onboarding

## What problem does this aim to solve?

Docker addresses a fundamental challenge in software development: the "it works on my machine" syndrome. This problem arises when software runs well in the developer's environment but encounters issues in different environments due to variations in operating systems, software versions, and other dependencies. Docker resolves this by enabling developers to package an application with all of its dependencies into a standardized unit called a container. This containerization ensures that the application runs consistently across any computing environment.

## What sub-category of technologies is this?

Docker falls under the sub-category of "containerization technology" within the broader field of DevOps (Development and Operations). It is a tool that facilitates the creation, deployment, and running of applications by using containers. Containerization, as a concept, is part of a larger trend towards microservices architectures in software development, where applications are broken down into smaller, independent parts that can be deployed and managed dynamically.

## Developer life with/without this tool

### Without Docker

#### Environment Setup

Individual developers are responsible for setting up their development environments, which includes installing Python, Flask, and other dependencies.
Variability in OS and dependency versions can lead to inconsistencies.

Example Setup:

```bash
# Install Python
# Install Flask
pip install flask
```

#### Development Challenges

Discrepancies between local development environments can lead to bugs that are hard to trace.
Time-consuming setup for new team members to mirror the environment accurately.

#### Deployment Hurdles

Ensuring that the production server matches the development environment is error-prone.
Manual environment setup is required for each deployment.

Example Deployment Steps:

```bash
# On server
# Install Python, Flask, and other dependencies
# Set environment variables
# Deploy the application
```

#### Version Control Issues

Keeping track of which versions of dependencies are used across different development and production environments can be challenging.

### With Docker

#### Consistent Environment Setup

Dockerfile defines the exact environment, including the OS, Python version, and dependencies.
Example Dockerfile:

```Dockerfile
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
```

Environment setup is consistent across all developers' machines and production.

#### Streamlined Development Process

Developers focus on writing code rather than managing environments.
Containers ensure that the application runs in an isolated environment, avoiding conflicts with other projects.

Example Commands to Build and Run Container:

```bash
# Build Docker image
docker build -t my-flask-app .

# Run Docker container
docker run -p 5000:5000 my-flask-app
```

#### Simplified Deployment

Deployment is as simple as running the container on any server with Docker installed.
The application runs in the same environment as it does in development, minimizing deployment issues.

Example Deployment Commands:

```bash
# On server
# Pull Docker image and run the container
docker pull my-flask-app
docker run -p 5000:5000 my-flask-app
```

#### Version Control and Maintenance

Dockerfile serves as documentation for the environment setup, making it easy to track and update dependencies.
Simplifies updates and maintenance of the application environment.

## Core Concepts

### Docker Images

A Docker image is a lightweight package that includes everything needed to run a piece of software: code, runtime, libraries, environment variables, and config files. It serves as a blueprint for creating containers, ensuring consistent application execution across environments. Images simplify the sharing and distribution of application environments, often through registries like Docker Hub.

### Docker Containers

Containers are runnable instances of Docker images, encapsulating the application and its environment. They provide isolation and consistency, allowing applications to run uniformly across different setups. Containers are central to Docker's efficiency in various environments, from development to production.

### Dockerfile

A Dockerfile is a script containing commands to assemble an image, automating the creation of Docker images. It's essential for scripting the setup of an environment tailored to an application's needs, ensuring all dependencies and configurations are uniformly handled.

### Docker Registries

Docker registries, such as Docker Hub, are repositories for storing Docker images. They are vital for the sharing and collaboration of Docker images, facilitating the consistent deployment of applications across different stages of the development cycle.

### Docker Compose

Docker Compose is a tool for managing multi-container applications, using a YAML file for configuration. It simplifies orchestrating applications that comprise multiple interconnected containers, such as those needing web servers, databases, and caching systems.

## Core APIs

### `docker run`

- Purpose: Creates and starts a Docker container from an image.
- Usage Example:

```bash
docker run -d -p 80:80 my-web-app
```

- Mock Output:

```bash
a1b2c3d4e5f6 
# This output signifies that the container has been created and started, displaying the container ID.
```

### `docker build`

- Purpose: Builds an image from a Dockerfile.
- Usage Example:

```bash
docker build -t my-web-app .
```

- Mock Output:

```bash
Successfully built 7a8b9c0d1e2f
Successfully tagged my-web-app:latest
# Indicates successful image creation with the assigned tag.
```

### `docker pull` / `docker push`

- Purpose: Fetches (pull) or uploads (push) images to/from a Docker registry.
- Usage Examples:

```bash
# Pull
docker pull ubuntu

# Push
docker push my-web-app
```

Mock Output:

```bash
# Pull
Using default tag: latest
latest: Pulling from library/ubuntu
Digest: sha256:12345abcdef
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest

# Push
The push refers to repository [docker.io/my-web-app]
5f70bf18a086: Pushed 
latest: digest: sha256:67890ghijkl size: 528
```

### `docker ps`

- Purpose: Lists running containers.
- Usage Example:

```bash
docker ps
```

Mock Output:

```bash
CONTAINER ID   IMAGE         COMMAND             CREATED         PORTS                  NAMES
a1b2c3d4e5f6   my-web-app    "python app.py"   2 minutes ago     0.0.0.0:80->80/tcp     hopeful_meitner
```

### `docker-compose up` / `docker-compose down`

- Purpose: Starts/stops multi-container Docker applications defined by docker-compose.yml.
- Usage Examples:

```bash
# Up
docker-compose up

#Down
docker-compose down
```

Mock Output:

```bash
# Up
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done

# Down
Stopping myapp_web_1 ... done
Removing myapp_web_1 ... done
Removing network myapp_default
```

## Small Running Example

This section provides a practical example of using Docker, starting from installation to running a simple application.

### Installation

1. Install Docker

- For macOS and Windows:
  - Download Docker Desktop from the Docker website.
  - Follow the installation instructions.
- For Linux:
  - Use the package manager to install Docker. For example, on Ubuntu:
  ```
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```
- After installation, ensure the Docker daemon is running. This usually happens automatically, especially on Windows and macOS.

2. Verify Installation:

- Open a terminal or command prompt.
- Run `docker --version` to ensure Docker is installed correctly.

### Code
Now that Docker is installed, let's create a simple Python Flask application and containerize it.

1. Create a Simple Flask App:

    Make a new directory and navigate into it.
    Create a new directory and a file named `app.py` with the following content:

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, Docker!'

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
    ```

2. Create a Dockerfile:

    In the same directory, create a file named Dockerfile with the following content:

    ```Dockerfile
    FROM python:3.8
    WORKDIR /app
    COPY . /app
    RUN pip install flask
    CMD ["python", "app.py"]
    ```
    This Dockerfile uses the official Python image, sets up a working directory, installs Flask (the only dependency), and specifies the command to run the Flask app.

3. Build the Docker Image:

    In your terminal, in the directory containing your Dockerfile, run:

    ```bash
    docker build -t flask-sample-app .
    ```

4. Run the Docker Container:

    Once the image is built, run the container:
    ```bash
    docker run -p 5000:5000 flask-sample-app
    ```
    This command maps port 5000 of the container to port 5000 on the host.

5. Access the Application:

    Open a web browser and go to <http://localhost:5000>. You should see "Hello, Docker!" displayed.

## Real Life Examples

### Example Voting App:

- Description: A distributed application demonstrating Docker's multi-container management capabilities, integrating Docker Compose, Swarm, and Kubernetes.
- URL: https://github.com/dockersamples/example-voting-app

### Wordsmith:

- Description: Showcases Docker containers under Kubernetes, highlighting container orchestration.
- URL: https://github.com/dockersamples/wordsmith

### Compose-Dev-Env:

- Description: Illustrates Docker's use in development environments, focusing on compose applications.
- URL: https://github.com/dockersamples/compose-dev-env