# Tomcat
 
## Onboarding

### What problem does this aim to solve?

Tomcat is a web server and servlet container that addresses the challenge of deploying and running Java web applications. It provides a reliable and efficient environment for hosting Java-based web applications, handling HTTP requests, and managing the execution of servlets and JavaServer Pages (JSPs). Tomcat simplifies the process of deploying web applications by providing a lightweight and easy-to-use server that can be quickly set up and configured.

### What sub-category of technologies is this?

Tomcat falls under the sub-category of application servers within the broader field of web development. It is specifically designed to handle Java-based web applications and provides a runtime environment for executing Java servlets and JSPs. Application servers like Tomcat are responsible for managing the lifecycle of web applications, handling HTTP requests, and providing various services and APIs for developers to build and deploy their applications.
 
## Developer life with/without this tool

### Without Tomcat

#### Manual Server Setup

Developers are responsible for setting up and configuring their own web servers to run Java web applications.
This involves installing and configuring the necessary software, such as Java Development Kit (JDK) and a web server like Apache HTTP Server.

Example setup:

1. Install JDK
2. Install Apache HTTP Server
3. Configure Apache to work with Java web applications

#### Deployment Challenges

Deploying a Java web application involves manually copying the application files to the server, configuring the server to run the application, and managing dependencies.

Example deployment steps:

1. Copy application files to the server
2. Configure the server to run the application
3. Install and manage dependencies manually

#### Debugging and Troubleshooting

Without Tomcat, developers have to rely on manual debugging techniques and log analysis to identify and fix issues in their Java web applications.

### With Tomcat

#### Easy Server Setup

Tomcat provides a pre-configured web server environment specifically designed for running Java web applications.
Developers can simply download and install Tomcat, and it is ready to use out of the box.

Example setup:

1. Download Tomcat
2. Install Tomcat

#### Simplified Deployment

Tomcat provides a straightforward deployment process for Java web applications.
Developers can deploy their applications by simply copying the application files to a specific directory in the Tomcat server.

Example deployment steps:

1. Copy application files to the Tomcat webapps directory
2. Start or restart the Tomcat server

#### Built-in Dependency Management

Tomcat includes a built-in dependency management system that simplifies the management of Java libraries and frameworks.
Developers can include the required dependencies in their application's configuration files, and Tomcat will automatically load and manage them.

Example configuration:

```xml
<dependencies\>
  <dependency\>
    <groupId\>com.example</groupId\>
    <artifactId\>my-library</artifactId\>
    <version\>1.0.0</version\>
  </dependency\>
</dependencies\>
```

#### Integrated Debugging and Troubleshooting

Tomcat provides built-in debugging and logging capabilities that make it easier to identify and fix issues in Java web applications.
Developers can use tools like the Tomcat Manager and access detailed logs to diagnose and troubleshoot problems.

Example debugging steps:

1. Use the Tomcat Manager to monitor and manage applications
2. Analyze Tomcat logs for error messages and stack traces

#### Example Workflow

A developer sets up Tomcat on their machine, deploys their Java web application by copying the application files to the Tomcat server, and uses the Tomcat Manager and logs to debug and troubleshoot any issues.
 
## Core Concepts

### Tomcat Server
Tomcat is an open-source web server and servlet container that is used to run Java-based web applications. It provides a runtime environment for Java web applications to handle HTTP requests, manage sessions, and serve static and dynamic content. Tomcat is widely used in the Java ecosystem and is known for its simplicity and lightweight nature.

### Servlets
Servlets are Java classes that extend the functionality of a web server. They handle HTTP requests and generate dynamic content for web applications. Servlets are the building blocks of Java web applications and are responsible for processing user input, interacting with databases, and generating HTML or other types of responses.

### Web Application
A web application is a collection of web resources (HTML, CSS, JavaScript, etc.) and server-side components (servlets, JSPs, etc.) that work together to provide a specific functionality or service over the internet. Tomcat is used to deploy and run web applications, making them accessible to users through a web browser.

### Context
In Tomcat, a context represents a web application and its associated resources. Each web application deployed in Tomcat has its own context, which defines the configuration and behavior of the application. The context includes information such as the application's base directory, session management settings, and security constraints.

### Deployment
Deployment refers to the process of making a web application available for use on a web server. In the context of Tomcat, deployment involves packaging the web application into a WAR (Web Application Archive) file and placing it in the appropriate directory in the Tomcat server. Tomcat then automatically deploys and starts the application, making it accessible to users.
 
## Core APIs

### `catalina.sh`

- Purpose: Starts, stops, and manages the Tomcat server.
- Usage Example:

```bash
# Starts the Tomcat server
catalina.sh start
```

### `catalina.bat`

- Purpose: Starts, stops, and manages the Tomcat server (Windows).
- Usage Example:

```bash
# Starts the Tomcat server
catalina.bat start
```

### `startup.sh`

- Purpose: Starts the Tomcat server in the background.
- Usage Example:

```bash
# Starts the Tomcat server in the background
startup.sh
```

### `shutdown.sh`

- Purpose: Stops the running Tomcat server.
- Usage Example:

```bash
# Stops the running Tomcat server
shutdown.sh
```

### `catalina.out`

- Purpose: Displays the Tomcat server logs.
- Usage Example:

```bash
# View the Tomcat server logs
cat catalina.out
```

### `webapps`

- Purpose: Directory where web applications are deployed.
- Usage Example:

```bash
# Deploy a web application to Tomcat
cp myapp.war /path/to/tomcat/webapps/
```
 
## Small Running Example

This section provides a practical example of using Apache Tomcat, starting from installation to running a simple web application.

### Installation

1. Install Apache Tomcat:

- Download the latest version of Apache Tomcat from the official website: [https://tomcat.apache.org/download](https://tomcat.apache.org/download).
- Choose the appropriate distribution based on your operating system.
- Extract the downloaded file to a directory of your choice.

2. Verify Installation:

- Open a terminal or command prompt.
- Navigate to the directory where you extracted Apache Tomcat.
- Run the following command to start the Tomcat server:
  - On macOS/Linux: `./bin/startup.sh`
  - On Windows: `.\bin\startup.bat`
- Open a web browser and go to `http://localhost:8080`. You should see the Apache Tomcat homepage if the installation was successful.

### Code

Now that Apache Tomcat is installed, let's create a simple web application and deploy it to the Tomcat server.

1. Create a Simple Web Application:

- Create a new directory for your web application.
- Inside the directory, create a file named `index.jsp` with the following content:

```jsp
<%@ page language=java contentType=text/html; charset=UTF-8 pageEncoding=UTF-8%\>
<!DOCTYPE html\>
<html\>
<head\>
    <title\>Tomcat Example</title\>
</head\>
<body\>
    <h1\>Hello, Tomcat!</h1\>
</body\>
</html\>
```

2. Package the Web Application:

- Create a new directory named `WEB-INF` inside your web application directory.
- Inside the `WEB-INF` directory, create a file named `web.xml` with the following content:

```xml
<?xml version=1.0 encoding=UTF-8?\>
<web-app xmlns=http://xmlns.jcp.org/xml/ns/javaee
         xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance
         xsi:schemaLocation=http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd
         version=4.0\>
    <display-name\>Tomcat Example</display-name\>
    <welcome-file-list\>
        <welcome-file\>index.jsp</welcome-file\>
    </welcome-file-list\>
</web-app\>
```

- Zip the contents of your web application directory, including the `WEB-INF` directory.

3. Deploy the Web Application:

- Stop the Tomcat server if it is running by running the following command:
  - On macOS/Linux: `./bin/shutdown.sh`
  - On Windows: `.\bin\shutdown.bat`
- Copy the zipped web application file to the `webapps` directory inside your Apache Tomcat installation directory.
- Start the Tomcat server again using the startup command mentioned in the installation section.
- Open a web browser and go to `http://localhost:8080/your-web-application-name`. You should see the Hello, Tomcat! message displayed.

Congratulations! You have successfully created and deployed a simple web application using Apache Tomcat.