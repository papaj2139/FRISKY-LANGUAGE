# FRISKY-LANGUAGE
i know what youre saying "a scripting language made in python and only in one file? it probablt a piece of shit but trust me it is kind of good? i guess
AND BTW I DONT REALLY KNOW IF IT WORKS WELL I DIDNT REALLY TEST IT AND SOMETIMES WAS TOO LAZY





# Frisky Scripting Language Documentation

Frisky is a low-level scripting language designed to provide direct control over hardware resources and system operations. It offers a minimalistic syntax and a small set of keywords for efficient and precise programming. This documentation outlines the key features, usage, and philosophy of Frisky as a low-level language.

## Table of Contents

- [Introduction](#introduction)
- [Why Frisky is Low-Level](#why-frisky-is-low-level)
- [Keywords](#keywords)
- [Variables](#variables)
- [Conditional Statements](#conditional-statements)
- [Loops](#loops)
- [Input and Output](#input-and-output)
- [File and Folder Management](#file-and-folder-management)
- [Data Structures](#data-structures)
- [Switch Statements](#switch-statements)
- [Functions](#functions)
- [Classes](#classes)
- [Garbage Collection](#garbage-collection)
- [User Input](#user-input)

## Introduction

Frisky is designed as a low-level scripting language to provide developers with fine-grained control over system resources and operations. It aims to bridge the gap between high-level languages and low-level programming by offering a simplified syntax and a focused feature set. Frisky is well-suited for tasks that require direct interaction with hardware, system APIs, and performance optimization.

## Why Frisky is Low-Level

Frisky is considered low-level due to the following reasons:

1. **Direct Hardware Access:** Frisky allows developers to interact directly with hardware components and system resources. This level of control enables optimizations and customization not easily achievable in higher-level languages.

2. **Minimal Abstractions:** Frisky avoids excessive abstractions and layers of complexity often found in higher-level languages. It provides a simplified syntax and minimal feature set, allowing developers to work at a closer, more granular level.

3. **Efficient Memory Management:** Frisky provides manual memory management, allowing developers to allocate and deallocate memory resources explicitly. This level of control is essential for performance-critical applications and resource-constrained environments.

4. **Access to Low-Level APIs:** Frisky exposes low-level APIs and system calls, enabling developers to interface directly with operating system features, libraries, and external hardware.

## Keywords

Frisky offers a concise set of keywords that provide essential functionality for controlling program flow, data manipulation, and system interactions. The following keywords are available in Frisky:

- `setvariable`: Assigns a value to a variable.
- `display.to_console`: Displays a value on the console.
- `if`, `else`, `ifelse`: Conditional statements for control flow.
- `for`: Looping construct for iteration.
- `import`: Imports a module.
- `create_file`, `delete_file`: File management operations.
- `create_folder`, `delete_folder`: Folder management operations.
- `create_list`, `create_dict`: Data structure creation.
- `switch`, `case`, `default`: Switch statement for multi-way branching.
- `return`: Returns a value from a function.
- `and`, `or`, `not`: Logical operators.
- `fun`: Defines a function.
- `class`: Defines a class.
- `gc.collect`: Performs garbage collection.
- `ask`: Requests user input.

## Variables

Frisky supports variables for storing and manipulating data. Variables in Frisky are dynamically typed, allowing them to hold various types of values, such as numbers, strings, lists, and dictionaries. Variables are created using the `setvariable` keyword followed by the variable name and the assigned value.

Example:
```frisky
setvariable x = 5
setvariable name = "John"
setvariable fruits = create_list("apple", "banana", "cherry")
```

In this example, variables `x`, `name`, and `fruits` are assigned the values 5, "John", and a list of fruits, respectively.

## Conditional Statements

Frisky provides conditional statements (`if`, `else`, `ifelse`) for controlling program flow based on specified conditions. These statements allow developers to execute different blocks of code depending on whether the conditions evaluate to `true` or `false`. Logical operators (`and`, `or`, `not`) can be used to combine and negate conditions for more complex evaluations.

Example:
```frisky
setvariable age = 18

if age >= 18
  display.to_console("You are an adult.")
else
  display.to_console("You are a minor.")
end

```

In this example, the output of the code depends on the value of the `age` variable. If `age` is greater than or equal to 18, the message "You are an adult." is displayed. Otherwise, the message "You are a minor." is displayed.

## Loops

The `for` keyword in Frisky is used for creating loops that iterate over a sequence of values. It allows developers to repeat a block of code for each item in a list, range, or other iterable data structures.

Example:
```frisky
for i in range(5)
  display.to_console(i)
end
```

In this example, the code block inside the `for` loop is executed five times, with the variable `i` taking values from 0 to 4. The value of `i` is displayed on the console in each iteration.

## Input and Output

Frisky provides the `display.to_console` keyword for displaying values on the console. This is useful for debugging purposes or providing feedback to the user during program execution.

Example:
```frisky
display.to_console("Hello, Frisky!")
```

The output of this code would be:
```
Hello, Frisky!
```

## File and Folder Management

Frisky provides keywords for managing files and folders. The `create_file` and `delete_file` keywords allow developers to create and delete files, while the `create_folder` and `delete_folder` keywords enable the creation and deletion of folders.

Example:
```frisky
create_file("data.txt")
delete_file("data.txt")
```

In this example, a file named "data.txt" is created using the `create_file` keyword, and then it is deleted using the `delete_file` keyword.

## Data Structures

Frisky supports the creation of lists and dictionaries using the `create_list` and `create_dict` keywords, respectively. Lists are used for storing an ordered collection of items, while dictionaries store key-value pairs for efficient lookup.

Example:
```frisky
setvariable numbers = create_list(1, 2, 3, 4, 5)
setvariable student = create_dict("name": "John", "age": 20, "grade": "A")
```

In this example, the `numbers` variable is assigned a list of numbers, and the `student` variable is assigned a dictionary with key-value pairs representing student information.

## Switch Statements

The `switch`, `case`, and `default` keywords in Frisky enable developers to create switch statements. Switch statements allow for multi-way branching based on the value of a variable or expression. The code block associated with the matching case is executed.

Example:
```frisky
setvariable day = "Monday"

switch day
  case "Monday"
    display.to_console("It's Monday!")
  case "Tuesday"
    display.to_console("It's Tuesday!")
  default
    display.to_console("It's another day.")
end
```

In

 this example, the output depends on the value of the `day` variable. If `day` is "Monday", the message "It's Monday!" is displayed. If `day` is "Tuesday", the message "It's Tuesday!" is displayed. Otherwise, the message "It's another day." is displayed.

## Functions

Frisky allows the creation and use of functions using the `fun` keyword. Functions encapsulate a block of code that can be called multiple times with different arguments. They provide a way to modularize code and improve code reuse.

Example:
```frisky
fun greet(name)
  display.to_console("Hello, " + name + "!")
end

greet("Alice")
greet("Bob")
```

In this example, a function named `greet` is defined with a single parameter `name`. The function displays a personalized greeting based on the provided name. The function is then called twice with different arguments.

## Classes

Frisky supports basic object-oriented programming with classes. Classes are defined using the `class` keyword, and objects are created using the class name followed by parentheses. Classes allow for encapsulating related data and functions into a single entity.

Example:
```frisky
class Person
  setvariable name = ""
  
  fun set_name(new_name)
    setvariable name = new_name
  end
  
  fun display_name()
    display.to_console("Name: " + name)
  end
end

setvariable person = Person()
person.set_name("Alice")
person.display_name()
```

In this example, a class named `Person` is defined with a variable `name` and two functions: `set_name` to set the name and `display_name` to display the name. An object `person` is created from the `Person` class, the name is set to "Alice", and then the name is displayed.

## Garbage Collection

Frisky provides the `gc.collect` keyword for performing garbage collection. Garbage collection is the process of automatically freeing memory occupied by objects that are no longer in use. The `gc.collect` keyword helps manage memory resources efficiently.

Example:
```frisky
gc.collect()
```

In this example, the `gc.collect` keyword triggers the garbage collection process, freeing up memory occupied by unused objects.

## User Input

Frisky offers the `ask` keyword for requesting user input during program execution. It prompts the user for input and returns the entered value, which can be stored in variables or used in further computations.

Example:
```frisky
setvariable name = ask("What is your name?")
display.to_console("Hello, " + name + "!")
```

In this example, the user is prompted with the question "What is your name?" and their input is stored in the `name` variable. The greeting message is then displayed using the entered name.

