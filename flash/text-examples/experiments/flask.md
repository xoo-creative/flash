# Flask
 
## Onboarding

### What problem does this aim to solve?

Flask is a web framework that aims to simplify the process of building web applications in Python. It addresses the challenge of developing web applications by providing a lightweight and flexible framework that allows developers to quickly and easily create web applications with minimal boilerplate code. Flask provides a set of tools and libraries that handle common web development tasks, such as routing, request handling, and template rendering, allowing developers to focus on building the core functionality of their applications.

### What sub-category of technologies is this?

Flask falls under the sub-category of web frameworks within the broader field of web development. Web frameworks provide a structured approach to building web applications by providing a set of tools and libraries that handle common tasks, such as routing, request handling, and database integration. Flask is specifically designed for Python developers and is known for its simplicity and minimalistic approach, making it a popular choice for building small to medium-sized web applications.
 
## Developer life with/without this tool

### Without Flask

#### Manual Routing

Developers have to manually handle routing in their web applications, mapping URLs to specific functions or views.

Example code:

```python
@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/about')
def about():
    return 'This is the about page'
```

#### Tedious Request Handling

Handling HTTP requests and responses requires manual parsing and processing of data.

Example code:

```python
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    # Process the submitted data
    return 'Data submitted successfully'
```

#### No Built-in Templating

Developers have to manually write HTML code within their Python code, making it difficult to separate the presentation layer from the application logic.

Example code:

```python
@app.route('/user/<username\>')
def user_profile(username):
    # Fetch user data from the database
    return f'''
    <h1\>{username\}'s Profile</h1\>
    <p\>Email: {user.email\}</p\>
    <p\>Age: {user.age\}</p\>
    '''
```

### With Flask

#### Simplified Routing

Flask provides a built-in routing system that allows developers to define routes and associate them with specific functions or views.

Example code:

```python
@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/about')
def about():
    return 'This is the about page'
```

#### Easy Request Handling

Flask automatically handles HTTP requests and provides convenient access to request data.

Example code:

```python
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    # Process the submitted data
    return 'Data submitted successfully'
```

#### Integrated Templating

Flask comes with a built-in templating engine that allows developers to separate the presentation layer from the application logic using templates.

Example code:

```python
@app.route('/user/<username\>')
def user_profile(username):
    # Fetch user data from the database
    return render_template('user_profile.html', username=username, user=user)
```

In `user_profile.html`:

```html
<h1\>{{ username \}\}'s Profile</h1\>
<p\>Email: {{ user.email \}\}</p\>
<p\>Age: {{ user.age \}\}</p\>
```

#### Flask Extensions

Flask has a rich ecosystem of extensions that provide additional functionality, such as database integration, authentication, and API development.

Example code:

```python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)
```

In `users.html`:

```html
<ul\>
{% for user in users %\}
    <li\>{{ user.username \}\} - {{ user.email \}\}</li\>
{% endfor %\}
</ul\>
```

Flask and its extensions simplify web development by providing a framework for routing, request handling, templating, and integrating with databases. It allows developers to focus on building the application logic and user experience without getting bogged down by low-level details.
 
## Core Concepts

### Flask Application
A Flask application is a web application built using the Flask framework. It is the foundation of any Flask project and is responsible for handling incoming requests and generating responses. A Flask application is typically defined in a Python file and can include routes, views, templates, and other components.

### Routes
Routes in Flask define the URLs that the application can handle. Each route is associated with a specific function, called a view function, that is executed when the corresponding URL is accessed. Routes are defined using decorators, such as `@app.route('/path')`, and can include dynamic parameters to handle variable parts of the URL.

### Views
Views in Flask are the functions that handle requests and generate responses. Each view function is associated with a specific route and is responsible for processing the request data, performing any necessary computations or database operations, and returning a response to the client. Views can render templates, return JSON data, or perform other actions based on the application's requirements.

### Templates
Templates in Flask are used to generate dynamic HTML pages that are sent as responses to client requests. Templates allow for the separation of logic and presentation, making it easier to build complex web pages. Flask uses the Jinja templating engine, which provides a powerful and flexible syntax for embedding dynamic content in HTML templates.

### Flask Extensions
Flask extensions are additional libraries or modules that provide extra functionality to a Flask application. These extensions can be used to add features such as database integration, authentication, form handling, and more. Flask extensions are typically installed using pip and can be easily integrated into a Flask project by importing and configuring them in the application code.
 
## Core APIs

### `flask.Flask`

- Purpose: Creates a Flask application instance.
- Usage Example:

```python
from flask import Flask

app = Flask(__name__)
```

### `app.route`

- Purpose: Decorator that associates a URL route with a view function.
- Usage Example:

```python
@app.route('/')
def home():
    return 'Hello, World!'
```

### `app.run`

- Purpose: Runs the Flask application on a local development server.
- Usage Example:

```python
if __name__ == '__main__':
    app.run()
```

### `request`

- Purpose: Provides access to incoming request data.
- Usage Example:

```python
from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Perform login logic
```

### `render_template`

- Purpose: Renders a template with the given context variables.
- Usage Example:

```python
from flask import render_template

@app.route('/profile/<username\>')
def profile(username):
    # Retrieve user data
    return render_template('profile.html', username=username)
```
 
## Small Running Example

This section provides a practical example of using Flask, starting from installation to running a simple web application.

### Installation

1. Install Python:

- For macOS and Linux:
  - Python is usually pre-installed on macOS and most Linux distributions. You can check if Python is installed by running `python --version` in your terminal.
  - If Python is not installed, you can download and install it from the official Python website: <https://www.python.org/downloads/\>.
- For Windows:
  - Download the Python installer from the official Python website: <https://www.python.org/downloads/windows/\>.
  - Run the installer and follow the installation instructions.

2. Verify Installation:

- Open a terminal or command prompt.
- Run `python --version` to ensure Python is installed correctly.

3. Install Flask:

- Open a terminal or command prompt.
- Run the following command to install Flask using pip, the Python package installer:

```bash
pip install flask
```

### Code

Now that Flask is installed, let's create a simple web application.

1. Create a New Directory and File:

- Open a terminal or command prompt.
- Create a new directory for your Flask application:

```bash
mkdir flask-app
cd flask-app
```

- Create a new file named `app.py` with the following content:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

2. Run the Flask Application:

- In the terminal or command prompt, navigate to the directory where `app.py` is located (`flask-app` in this example).
- Run the following command to start the Flask development server:

```bash
python app.py
```

3. Access the Application:

- Open a web browser and go to <http://localhost:5000\>. You should see Hello, Flask! displayed.

Congratulations! You have successfully created and run a simple Flask web application. You can modify the `app.py` file to add more routes and functionality to your application.