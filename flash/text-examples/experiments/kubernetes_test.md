# Kubernetes
 
## Onboarding

### What problem does this aim to solve?

Kubernetes addresses the challenges of deploying, scaling, and managing containerized applications in a distributed environment. As organizations adopt containerization technologies like Docker, they face the need to manage and orchestrate these containers across multiple machines or clusters. This can become complex and time-consuming, especially as the number of containers and their dependencies increase. Kubernetes solves this problem by providing a platform for automating the deployment, scaling, and management of containerized applications, allowing developers to focus on building and shipping their applications rather than worrying about the underlying infrastructure.

### What sub-category of technologies is this?

Kubernetes falls under the sub-category of "container orchestration" within the broader field of DevOps (Development and Operations). It is a powerful tool that enables the management of containerized applications at scale. Container orchestration involves automating the deployment, scaling, and management of containers across multiple machines or clusters. Kubernetes provides a robust and flexible platform for container orchestration, allowing developers to easily manage and scale their applications in a distributed environment.
 
## Developer life with/without this tool

### Without Kubernetes

#### Manual Deployment and Scaling

Developers are responsible for manually deploying and scaling applications on individual servers or virtual machines.
This process involves configuring and managing each server individually, which can be time-consuming and error-prone.

#### Resource Management

Without Kubernetes, developers need to manually allocate and manage resources for each application.
This includes monitoring resource usage, optimizing resource allocation, and handling scaling based on demand.

#### High Availability and Fault Tolerance

Ensuring high availability and fault tolerance requires manual configuration and management of redundant servers and load balancing.
This can be complex and time-consuming, especially when dealing with large-scale applications.

#### Example Scenario

A developer needs to deploy a microservice-based application on multiple servers, configure load balancing, and handle scaling based on traffic fluctuations.
This involves manually setting up and managing each server, monitoring resource usage, and ensuring fault tolerance.

### With Kubernetes

#### Automated Deployment and Scaling

Kubernetes automates the deployment and scaling of applications using containerization.
Developers define the desired state of the application using YAML files, and Kubernetes takes care of the rest.

Example YAML file:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: my-app
        image: my-app-image
        ports:
        - containerPort: 8080
```

Kubernetes ensures that the specified number of replicas are running, handles load balancing, and scales the application based on demand.

#### Resource Management and Optimization

Kubernetes provides built-in resource management and optimization features.
Developers can define resource limits and requests for each container, and Kubernetes ensures efficient resource allocation.

Example YAML file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: my-app
    image: my-app-image
    resources:
      limits:
        cpu: "1"
        memory: "1Gi"
      requests:
        cpu: "0.5"
        memory: "512Mi"
```

Kubernetes monitors resource usage and automatically adjusts resource allocation based on demand.

#### High Availability and Fault Tolerance

Kubernetes provides built-in features for ensuring high availability and fault tolerance.
It automatically handles load balancing, service discovery, and fault recovery.

Example YAML file for a load-balanced service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

Kubernetes automatically distributes incoming traffic to the available replicas of the application, ensuring high availability.

#### Example Workflow

A developer defines the desired state of the application using YAML files, deploys the application to Kubernetes (`kubectl apply -f deployment.yaml`), and Kubernetes takes care of managing the application, scaling, load balancing, and fault tolerance.
 
## Core Concepts

### Pods
A pod is the smallest and most basic unit in Kubernetes. It represents a single instance of a running process in a cluster. A pod can contain one or more containers that are tightly coupled and share the same network namespace, storage, and other resources. Pods are ephemeral and can be created, deleted, or replaced by Kubernetes based on the desired state of the system.

### Replication Controllers
Replication Controllers ensure that a specified number of pod replicas are running at all times. They monitor the state of pods and automatically create or delete pods to maintain the desired replica count. Replication Controllers provide fault tolerance and scalability by allowing the distribution of workload across multiple pods.

### Services
Services in Kubernetes provide a stable network endpoint to access a group of pods. They enable load balancing and service discovery within the cluster. A service abstracts the underlying pods and provides a single entry point for clients to access the application. Services can be exposed internally within the cluster or externally to the outside world.

### Deployments
Deployments are a higher-level abstraction that manages the lifecycle of pods and replica sets. They provide a declarative way to define and manage the desired state of applications. Deployments allow for rolling updates and rollbacks, making it easy to deploy new versions of an application without downtime. They also ensure that the desired number of replicas are always running.

### ConfigMaps and Secrets
ConfigMaps and Secrets are Kubernetes resources used to manage configuration data and sensitive information, respectively. ConfigMaps store key-value pairs or configuration files that can be consumed by pods as environment variables or mounted as volumes. Secrets are similar to ConfigMaps but are specifically designed to store sensitive data such as passwords, API keys, or TLS certificates. Both ConfigMaps and Secrets can be updated independently of the pods that use them, allowing for dynamic configuration changes without redeploying the application.
 
## Core APIs

### `kubectl create`

- Purpose: Creates a resource in the Kubernetes cluster.
- Usage Example:

```bash
kubectl create deployment my-app --image=my-image:latest
```

### `kubectl apply`

- Purpose: Applies a configuration to the Kubernetes cluster, creating or updating resources.
- Usage Example:

```bash
kubectl apply -f my-config.yaml
```

### `kubectl get`

- Purpose: Retrieves information about resources in the Kubernetes cluster.
- Usage Example:

```bash
kubectl get pods
```

### `kubectl describe`

- Purpose: Provides detailed information about a specific resource in the Kubernetes cluster.
- Usage Example:

```bash
kubectl describe pod my-pod
```

### `kubectl delete`

- Purpose: Deletes a resource from the Kubernetes cluster.
- Usage Example:

```bash
kubectl delete deployment my-app
```
 
## Small Running Example

This section provides a practical example of using Kubernetes, starting from installation to deploying a simple application.

### Installation

1. Install Kubernetes

- For macOS and Windows:
  - Install Docker Desktop, which includes Kubernetes support.
  - Enable Kubernetes in the Docker Desktop settings.
- For Linux:
  - Use a package manager to install Kubernetes. For example, on Ubuntu:
  ```bash
  sudo apt-get update
  sudo apt-get install -y kubelet kubeadm kubectl
  ```
  - Initialize the cluster with `sudo kubeadm init`.

2. Verify Installation:

- Open a terminal or command prompt.
- Run `kubectl version` to ensure Kubernetes is installed correctly.

### Code

Now that Kubernetes is installed, let's deploy a simple application using a deployment and a service.

1. Create a Deployment:

    Create a file named `deployment.yaml` with the following content:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: hello-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: hello-app
      template:
        metadata:
          labels:
            app: hello-app
        spec:
          containers:
          - name: hello-app
            image: nginx:latest
            ports:
            - containerPort: 80
    ```

    This deployment creates three replicas of an Nginx container.

2. Apply the Deployment:

    In your terminal, apply the deployment using the following command:

    ```bash
    kubectl apply -f deployment.yaml
    ```

3. Create a Service:

    Create a file named `service.yaml` with the following content:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: hello-service
    spec:
      selector:
        app: hello-app
      ports:
      - protocol: TCP
        port: 80
        targetPort: 80
      type: LoadBalancer
    ```

    This service exposes the deployment as a load-balanced service on port 80.

4. Apply the Service:

    In your terminal, apply the service using the following command:

    ```bash
    kubectl apply -f service.yaml
    ```

5. Access the Application:

    Run the following command to get the external IP address of the service:

    ```bash
    kubectl get service hello-service
    ```

    Open a web browser and go to the external IP address. You should see the Nginx welcome page.

Congratulations! You have successfully deployed a simple application on Kubernetes.