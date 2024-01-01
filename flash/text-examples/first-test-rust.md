# Rust
 
## Onboarding

### What problem does this aim to solve?

Rust aims to address the challenges of writing safe and efficient systems-level software. Traditionally, languages like C and C++ have been used for such tasks, but they often introduce memory safety issues, such as null pointer dereferences, buffer overflows, and data races. Rust provides a solution by combining the performance of low-level languages with strong memory safety guarantees. It enforces strict compile-time checks to prevent common programming errors, making it easier to write reliable and secure code.

### What sub-category of technologies is this?

Rust falls under the sub-category of systems programming languages within the broader field of programming languages. Systems programming languages are designed for developing low-level software, such as operating systems, device drivers, embedded systems, and performance-critical applications. Rust distinguishes itself by prioritizing memory safety without sacrificing performance, making it an ideal choice for systems programming tasks.
 
## Developer life with/without this tool

### Without Rust

#### Memory Management

Developers are responsible for manually managing memory allocation and deallocation, which can lead to memory leaks, null pointer errors, and other memory-related bugs.

#### Concurrency

Writing concurrent code without proper abstractions can be challenging and error-prone. Developers need to handle low-level synchronization and thread management.

#### Safety

C and C++ languages allow for unsafe operations, which can lead to vulnerabilities like buffer overflows and undefined behavior.

#### Example Scenario

A developer forgets to deallocate memory after using it, causing a memory leak that gradually consumes system resources.

### With Rust

#### Memory Safety

Rust's ownership system and borrow checker ensure memory safety by preventing common memory-related bugs like null pointer errors, use-after-free, and data races.

Example Code:

```rust
fn main() {
    let mut data = String::from(Hello, Rust!);

    // Ownership transfer
    let new_data = data;

    // Error: value borrowed here after move
    println!({}, data);
}
```

#### Concurrency with Safety

Rust provides high-level abstractions for concurrent programming, such as threads and message passing, while ensuring memory safety and preventing data races.

Example Code:

```rust
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!(Hello from a thread!);
    });

    handle.join().unwrap();
}
```

#### Safe Abstractions

Rust encourages safe programming practices by providing safe abstractions and preventing unsafe operations by default. Developers can opt into unsafe code when necessary.

Example Code:

```rust
unsafe fn unsafe_function() {
    // Unsafe code block
}

fn main() {
    unsafe {
        unsafe_function();
    }
}
```

#### Example Scenario

A developer writes code that attempts to access a null pointer, but the Rust compiler catches the error at compile-time, preventing a potential crash or vulnerability.
 
## Core Concepts

### Ownership
Ownership is a fundamental concept in Rust that ensures memory safety and eliminates data races. Every value in Rust has a unique owner, and there can only be one owner at a time. When a value goes out of scope, its owner is responsible for cleaning up the memory associated with it. Ownership is transferred through moves, where the ownership of a value is transferred from one variable to another. This ensures that there are no dangling pointers or memory leaks.

### Borrowing and References
In Rust, borrowing allows multiple references to access a value without taking ownership. Borrowing can be done either as immutable references (&T) or mutable references (&mut T). Immutable references allow read-only access to the value, while mutable references allow both read and write access. The borrow checker enforces strict rules to prevent data races and ensure memory safety.

### Lifetimes
Lifetimes in Rust ensure that references are always valid and prevent the use of dangling references. A lifetime is a scope during which a reference is valid. The Rust compiler analyzes the code to determine the minimum lifetime required for each reference and ensures that references do not outlive the data they refer to. Lifetimes are denoted using apostrophes ('a) and are specified in function signatures and data structures.

### Error Handling with Result and Option
Rust provides two types, Result<T, E> and Option<T>, for handling errors and optional values respectively. Result<T, E> represents the possibility of an operation returning either a value of type T or an error of type E. Option<T> represents the possibility of a value being present (Some<T>) or absent (None). These types encourage explicit error handling and help prevent unexpected runtime errors.

### Pattern Matching
Pattern matching is a powerful feature in Rust that allows you to match values against a set of patterns and execute different code based on the match. It is commonly used with enums and match expressions. Pattern matching enables concise and expressive code, making it easier to handle different cases and control flow in your programs.
 
## Core APIs

### `cargo new`

- Purpose: Creates a new Rust project with the necessary project structure and files.
- Usage Example:

```bash
# Creates a new Rust project named my_project
cargo new my_project
```

### `cargo build`

- Purpose: Compiles the Rust project and generates the executable or library output.
- Usage Example:

```bash
# Compiles the Rust project in the current directory
cargo build
```

### `cargo run`

- Purpose: Builds and runs the Rust project in a single command.
- Usage Example:

```bash
# Builds and runs the Rust project in the current directory
cargo run
```

### `cargo test`

- Purpose: Runs the tests defined in the Rust project.
- Usage Example:

```bash
# Runs the tests in the Rust project
cargo test
```

### `cargo doc`

- Purpose: Generates documentation for the Rust project based on the code comments and doc comments.
- Usage Example:

```bash
# Generates documentation for the Rust project
cargo doc
```

### `cargo publish`

- Purpose: Publishes the Rust project to the crates.io registry, making it available for others to use.
- Usage Example:

```bash
# Publishes the Rust project to the crates.io registry
cargo publish
```
 
# Rust

## Small Running Example

This section provides a practical example of using Rust, starting from installation to running a simple program.

### Installation

1. Install Rust:

- For macOS and Linux:
  - Open a terminal.
  - Run the following command:
    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```
  - Follow the instructions in the terminal to complete the installation.

- For Windows:
  - Download the Rust installer from the Rust website.
  - Run the installer and follow the instructions.

2. Verify Installation:

- Open a terminal or command prompt.
- Run `rustc --version` to ensure Rust is installed correctly.

### Code

Now that Rust is installed, let's create a simple Hello, World! program.

1. Create a New Rust Project:

- Open a terminal or command prompt.
- Run the following command to create a new Rust project:
  ```bash
  cargo new hello_world
  ```
- Navigate into the project directory:
  ```bash
  cd hello_world
  ```

2. Write the Code:

- Open the project in a text editor.
- Replace the contents of the `src/main.rs` file with the following code:
  ```rust
  fn main() {
      println!(Hello, World!);
  }
  ```

3. Build and Run the Program:

- In the terminal, navigate to the project directory if you're not already there.
- Run the following command to build and run the program:
  ```bash
  cargo run
  ```

4. Output:

- You should see the following output in the terminal:
  ```
  Hello, World!
  ```

Congratulations! You have successfully created and run a simple Rust program.