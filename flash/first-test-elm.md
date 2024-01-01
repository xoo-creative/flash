# Elm

## Onboarding

### What problem does this aim to solve?

Elm is a functional programming language that aims to solve the challenges of building reliable and maintainable web applications. Traditional JavaScript frameworks often suffer from issues such as runtime errors, unpredictable behavior, and difficulties in refactoring and scaling codebases. Elm addresses these problems by providing a strongly-typed, statically-checked language that enforces immutability and pure functions. This leads to more predictable and robust code, reducing the likelihood of runtime errors and making it easier to reason about and maintain complex applications.

### What sub-category of technologies is this?

Elm falls under the sub-category of frontend web development frameworks within the broader field of web development. It is specifically designed for building user interfaces and focuses on providing a functional and declarative approach to UI development. Elm's architecture is inspired by the Model-View-Controller (MVC) pattern, but with a functional twist, making it a unique and powerful tool for frontend development.
 
## Developer life with/without this tool

### Without Elm

#### JavaScript Development Challenges

Developing complex web applications in JavaScript can be challenging due to the lack of strong typing and the potential for runtime errors.
Debugging and fixing errors can be time-consuming and frustrating.

#### Managing State

Managing state in JavaScript applications can be difficult, especially as the application grows in complexity.
Developers need to manually handle state changes and ensure consistency across different components.

#### Scaling and Refactoring

As JavaScript applications grow, maintaining code quality and scalability becomes increasingly challenging.
Refactoring code can be error-prone and time-consuming, as there are no strict guarantees about the behavior of the code.

#### Example Scenario

A developer is working on a large JavaScript application and encounters a bug that is difficult to trace due to the lack of strong typing.
The bug is caused by an incorrect type being passed to a function, but it is not immediately obvious where the error originates.

### With Elm

#### Strong Typing and Compiler Checks

Elm is a statically typed language that provides strong guarantees about the types of values and how they can be used.
The Elm compiler catches many errors at compile-time, reducing the likelihood of runtime errors.

Example Elm code:

```elm
type User = User { name : String, age : Int }

getName : User -> String
getName (User user) = user.name
```

#### Immutable State and Message Passing

Elm enforces immutability, making it easier to reason about state changes.
State updates are done through message passing, ensuring a clear and predictable flow of data.

Example Elm code:

```elm
type Msg = Increment | Decrement

update : Msg -> Model -> Model
update msg model =
    case msg of
        Increment ->
            { model | count = model.count + 1 }

        Decrement ->
            { model | count = model.count - 1 }
```

#### Scalability and Refactoring

Elm's strong typing and compiler checks make it easier to refactor code and maintain code quality as the application grows.
The compiler provides helpful error messages and guides developers in making correct changes.

#### Example Workflow

A developer working with Elm creates a new component, defines its type and behavior, and receives immediate feedback from the compiler about any errors or inconsistencies.
The developer can confidently refactor code, knowing that the compiler will catch any potential issues.

Overall, Elm improves the developer experience by providing strong typing, immutability, and a helpful compiler, leading to more reliable and maintainable code.
 
## Core Concepts

### The Elm Architecture
The Elm Architecture is a pattern for building web applications in Elm. It consists of three main components: Model, View, and Update. The Model represents the state of the application, the View is responsible for rendering the user interface based on the current state, and the Update handles user interactions and updates the state accordingly. This architecture promotes a clear separation of concerns and makes it easy to reason about the application's behavior.

### Immutability
In Elm, data is immutable, meaning that once a value is created, it cannot be changed. Instead, any modifications to the data result in the creation of a new value. This approach ensures that the state of the application remains consistent and makes it easier to reason about the behavior of the program. Elm provides built-in functions and syntax for working with immutable data, such as the `update` function for updating the model.

### Type System and Static Typing
Elm has a strong and statically typed system, which means that every value in the program has a specific type that is checked at compile-time. This helps catch errors early and provides better tooling and autocompletion support. Elm's type system also includes features like type inference, which allows the compiler to automatically infer the types of expressions without explicit annotations, reducing the amount of boilerplate code.

### Functional Programming
Elm is a functional programming language, which means that it emphasizes the use of pure functions and immutable data. Pure functions do not have side effects and always produce the same output given the same input, making them easier to test and reason about. Elm provides a rich set of functional programming features, such as higher-order functions, pattern matching, and function composition, which enable developers to write concise and expressive code.

### Virtual DOM
Elm uses a virtual DOM (Document Object Model) to efficiently update the user interface. The virtual DOM is a lightweight representation of the actual DOM, and any changes to the state of the application are first applied to the virtual DOM. Elm then calculates the minimal set of changes needed to update the actual DOM based on the differences between the previous and current virtual DOM. This approach improves performance by reducing the number of DOM manipulations and ensures a smooth user experience.
 
## Core APIs

### `elm init`

- Purpose: Initializes a new Elm project in the current directory, setting up the necessary project structure and configuration files.
- Usage Example:

```bash
mkdir MyElmProject
cd MyElmProject
# Initializes a new Elm project in the current directory
elm init
```

### `elm make`

- Purpose: Compiles Elm source code into JavaScript, generating a JavaScript file that can be executed in the browser.
- Usage Example:

```bash
# Compiles the Elm source code into JavaScript
elm make src/Main.elm --output=main.js
```

### `elm reactor`

- Purpose: Starts a development server that provides a live-reloading environment for Elm projects.
- Usage Example:

```bash
# Starts the Elm reactor server
elm reactor
```

### `elm install`

- Purpose: Installs Elm packages from the official package repository, allowing you to use external libraries in your Elm project.
- Usage Example:

```bash
# Installs the elm/http package
elm install elm/http
```

### `elm repl`

- Purpose: Starts the Elm REPL (Read-Eval-Print Loop), which provides an interactive environment for experimenting with Elm code.
- Usage Example:

```bash
# Starts the Elm REPL
elm repl
```

### `elm-test`

- Purpose: Runs tests written in Elm, allowing you to verify the correctness of your code.
- Usage Example:

```bash
# Runs all tests in the tests/ directory
elm-test
```
 
## Small Running Example

This section provides a practical example of using Elm, starting from installation to running a simple application.

### Installation

1. Install Elm:

- For macOS and Linux:
  - Open a terminal.
  - Run the following command to install Elm:
  ```
  npm install -g elm
  ```

- For Windows:
  - Open a command prompt.
  - Run the following command to install Elm:
  ```
  npm install -g elm
  ```

2. Verify Installation:

- Open a terminal or command prompt.
- Run `elm --version` to ensure Elm is installed correctly.

### Code

Now that Elm is installed, let's create a simple Elm application and run it in the browser.

1. Create a New Elm Project:

- Create a new directory for your project.
- Navigate into the project directory.
- Run the following command to initialize a new Elm project:
```
elm init
```
This will create the necessary files and folders for your Elm project.

2. Create a Simple Elm App:

- In the project directory, create a new file named `Main.elm` with the following content:

```elm
module Main exposing (..)

import Browser
import Html exposing (Html, div, text)


main =
    Browser.sandbox { init = init, update = update, view = view }


type alias Model =
    { message : String }


init : Model
init =
    { message = Hello, Elm! }


type Msg
    = NoOp


update : Msg -> Model -> Model
update msg model =
    case msg of
        NoOp ->
            model


view : Model -> Html Msg
view model =
    div [] [ text model.message ]
```

3. Run the Elm Application:

- In the terminal or command prompt, navigate to the project directory.
- Run the following command to compile and run the Elm application:
```
elm reactor
```
This will start the Elm development server.

4. Access the Application:

- Open a web browser and go to <http://localhost:8000>.
- You should see the Elm application running with the message Hello, Elm! displayed.

5. Make Changes:

- Open the `Main.elm` file in a text editor.
- Update the `message` field in the `init` function to a new message.
- Save the file.
- Refresh the browser to see the updated message.

Congratulations! You have successfully created and run a simple Elm application.