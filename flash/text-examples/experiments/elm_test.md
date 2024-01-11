# Elm
 
## Onboarding

### What problem does this aim to solve?

Elm is a functional programming language that aims to solve the challenges of building reliable and maintainable web applications. Traditional JavaScript frameworks often suffer from issues such as runtime errors, unpredictable behavior, and difficulties in refactoring and scaling codebases. Elm addresses these problems by providing a strongly-typed, statically-checked language that compiles to JavaScript. It enforces immutability and pure functions, which leads to more predictable and reliable code.

### What sub-category of technologies is this?

Elm falls under the sub-category of "frontend web development frameworks" within the broader field of web development. It is specifically designed for building user interfaces and focuses on providing a clean architecture and a functional programming paradigm. Elm is often used alongside HTML, CSS, and JavaScript to create interactive and responsive web applications.
 
## Developer life with/without this tool

### Without Elm

#### JavaScript Development Challenges

Developing complex web applications in JavaScript can be challenging due to the lack of a strong type system.
Debugging runtime errors and type-related issues can be time-consuming and error-prone.

#### Scalability and Maintainability

As JavaScript applications grow in size and complexity, it becomes harder to maintain and refactor code.
Lack of a clear architecture and enforced conventions can lead to inconsistent codebases.

#### Example Scenario

A developer working on a JavaScript project encounters a runtime error due to a type mismatch, spending hours debugging and tracing the issue.

### With Elm

#### Strongly Typed Language

Elm is a statically typed language that enforces type safety, eliminating many runtime errors.
The compiler catches type-related issues during development, reducing debugging time.

Example Elm code:

```elm
type alias User =
    { name : String
    , age : Int
    }

user : User
user =
    { name = "John"
    , age = 25
    }
```

#### Scalable Architecture

Elm promotes a clear and scalable architecture called the Elm Architecture (TEA).
TEA provides a structured way to organize code, making it easier to maintain and refactor as the application grows.

Example TEA structure:

```elm
type alias Model =
    { count : Int
    }

type Msg
    = Increment
    | Decrement

update : Msg -> Model -> Model
update msg model =
    case msg of
        Increment ->
            { model | count = model.count + 1 }

        Decrement ->
            { model | count = model.count - 1 }

view : Model -> Html Msg
view model =
    div []
        [ button [ onClick Increment ] [ text "+" ]
        , div [] [ text (String.fromInt model.count) ]
        , button [ onClick Decrement ] [ text "-" ]
        ]
```

#### Improved Developer Experience

Elm provides a smooth development experience with features like hot reloading, time-travel debugging, and a helpful compiler error messages.
The language encourages writing pure functions and immutable data, leading to more predictable and testable code.

#### Example Workflow

A developer starts an Elm project, writes code using the Elm Architecture, and compiles the code using the Elm compiler (`elm make Main.elm`).
The compiler catches any type errors and provides helpful error messages for quick debugging.
The developer can use hot reloading to see immediate changes in the browser while making modifications to the code.
 
## Core Concepts

### The Elm Architecture
The Elm Architecture is a pattern for building web applications in Elm. It consists of three main components: Model, View, and Update. The Model represents the state of the application, the View is responsible for rendering the user interface based on the current state, and the Update handles user interactions and updates the state accordingly. This architecture promotes a clear separation of concerns and makes it easy to reason about the application's behavior.

### Immutability
In Elm, data is immutable, meaning that once a value is created, it cannot be changed. Instead, any modifications to the data result in the creation of a new value. This approach ensures that the state of the application remains consistent and makes it easier to reason about the behavior of the program. Elm provides built-in functions and syntax for working with immutable data, such as the `update` function for updating the model.

### Type System and Static Typing
Elm has a strong and statically typed system, which means that every value in the program has a specific type that is checked at compile-time. This helps catch errors early and provides better guarantees about the correctness of the code. Elm's type system also includes features like type inference, which automatically infers the types of expressions, and algebraic data types, which allow for the creation of complex data structures with pattern matching.

### Functional Programming
Elm is a functional programming language, which means that functions are first-class citizens and can be passed around as values. Functional programming encourages writing pure functions that do not have side effects and are deterministic, meaning that given the same input, they always produce the same output. This approach makes the code easier to test, reason about, and maintain. Elm also provides a rich set of functional programming features, such as higher-order functions, function composition, and list manipulation functions.
 
## Core APIs

### `elm init`

- Purpose: Initializes a new Elm project in your current directory, setting up the necessary project structure and configuration files.
- Usage Example:

```bash
mkdir MyElmProject
cd MyElmProject
# Initializes a new Elm project in the current directory
elm init
```

### `elm make`

- Purpose: Compiles Elm source code into JavaScript, generating a JavaScript file that can be executed in a web browser.
- Usage Example:

```bash
# Compiles the Elm source code in Main.elm into JavaScript
elm make src/Main.elm --output=main.js
```

### `elm reactor`

- Purpose: Starts a development server that provides a live-reloading environment for Elm projects, allowing you to view and interact with your Elm application in a web browser.
- Usage Example:

```bash
# Starts the Elm reactor server
elm reactor
```

### `elm install`

- Purpose: Installs Elm packages from the official package repository, allowing you to use external libraries and dependencies in your Elm project.
- Usage Example:

```bash
# Installs the elm/http package
elm install elm/http
```

### `elm repl`

- Purpose: Starts the Elm REPL (Read-Eval-Print Loop), which provides an interactive environment for experimenting with Elm code and evaluating expressions.
- Usage Example:

```bash
# Starts the Elm REPL
elm repl
```

### `elm-test`

- Purpose: Runs tests written in Elm, allowing you to verify the correctness of your Elm code.
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
    { message = "Hello, Elm!" }


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
- You should see the Elm application running with the message "Hello, Elm!" displayed.

5. Make Changes:

- Open the `Main.elm` file in a text editor.
- Update the `message` field in the `init` function to a new message.
- Save the file.
- Refresh the browser to see the updated message.

Congratulations! You have successfully created and run a simple Elm application.