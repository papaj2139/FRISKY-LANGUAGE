# FRISKY-LANGUAGE
i know what youre saying "a scripting language made in python and only in one file? it probablt a piece of shit but trust me it is kind of good? i guess
AND BTW I DONT REALLY KNOW IF IT WORKS WELL I DIDNT REALLY TEST IT AND SOMETIMES WAS TOO LAZY





# Frisky Scripting Language Documentation

Frisky is a simple scripting language designed to be easy to read and write. It provides a set of keywords and constructs for performing various operations, including variable manipulation, control flow, file and folder management, function definition, and more.

## Table of Contents

- [Introduction](#introduction)
- [Keywords](#keywords)
- [Variables](#variables)
- [Control Flow](#control-flow)
- [Input and Output](#input-and-output)
- [File and Folder Management](#file-and-folder-management)
- [Functions](#functions)
- [Classes](#classes)
- [Importing Libraries](#importing-libraries)
- [Garbage Collection](#garbage-collection)

## Introduction

Frisky is a dynamic scripting language that is interpreted at runtime. It is designed to provide a high-level interface for performing common tasks while maintaining simplicity and readability. Frisky scripts consist of a series of statements that are executed sequentially.

## Keywords

Frisky includes the following keywords:

- `setvariable`: Assigns a value to a variable.
- `display.to_console`: Displays a value on the console.
- `if`, `else`, `ifelse`: Conditional statements for control flow.
- `for`: Looping construct for iteration.
- `import`: Imports a Frisky library.
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

Variables in Frisky are dynamically typed and can hold various types of values, including numbers, strings, lists, and dictionaries. Variables are created using the `setvariable` keyword followed by the variable name and the assigned value. Here's an example:

```frisky
setvariable x = 5
```

In this example, a variable `x` is created and assigned the value of 5.

## Control Flow

Frisky provides conditional statements (`if`, `else`, `ifelse`) and looping constructs (`for`) for controlling the flow of execution.

### Conditional Statements

Frisky supports `if` statements for executing different blocks of code based on certain conditions. The `if` statement is used to define a condition, and the code block following it is executed only if the condition is true. Optionally, an `else` statement can be used to define a code block that is executed when the condition is false. The `ifelse` statement combines both conditions. Here's an example:

```frisky
if condition
  # code block executed when condition is true
else
  # code block executed when condition is false
end
```

### Looping Constructs

Frisky includes the `for` keyword for creating loops. The `for` loop iterates over a range of values or elements in a container. The code block following the `for` statement is executed for each iteration. Here's an example:

```frisky
for item in container
  # code block executed for each item in the container
end
```

In this example, the variable `item` takes on each value or element in the `container`, and the code block is executed for each iteration.

## Input and Output

Frisky provides functions for input and output operations.

### Output

The `display.to_console` keyword is used to print text or values to the console. It takes an expression or a string as an argument and displays it on the console output. Here's an example:

```frisky
display.to_console("Hello, Frisky!")
```

The output of this code would be:

```
Hello, Frisky!
```

### Input

The `ask` keyword is used to request user input. It takes a prompt as an argument and returns the user's input. Here's an example:

```frisky
setvariable name = ask("Enter your name: ")
```

In this example, the user is prompted with the message "Enter your name: ", and their input is stored in the `name` variable.

## File and Folder Management

Frisky provides functions for creating, deleting, and managing files and folders.

### File Management

The `create_file` keyword is used to create a new file with the specified filename. Here's an example:

```frisky
create_file("output.txt")
```

In this example, a file named "output.txt" is created.

The `delete_file` keyword is used to delete an existing file with the specified filename. Here's an example:

```frisky
delete_file("output.txt")
```

In this example, the file named "output.txt" is deleted.

### Folder Management

The `create_folder` keyword is used to create a new folder with the specified folder name. Here's an example:

```frisky
create_folder("data")
```

In this example, a folder named "data" is created.

The `delete_folder` keyword is used to delete an existing folder with the specified folder name. Here's an example:

```frisky
delete_folder("data")
```

In this example, the folder named "data" is deleted.

## Functions

Frisky allows you to define and call functions using the `fun` keyword. Functions encapsulate a block of code that can be called multiple times with different arguments. Here's an example:

```frisky
fun greet(name)
  display.to_console("Hello, " + name + "!")
end

greet("Alice")
greet("Bob")
```

In this example, a function named `greet` is defined with a single parameter `name`. The function displays a personalized greeting based on the provided name. The function is then called twice with different arguments.

## Classes

Frisky supports basic object-oriented programming with classes. Classes are defined using the `class` keyword, and objects are created using the class name followed by parentheses. Here's an example:

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

## Importing Libraries

Frisky allows you to import Frisky libraries using the `import` keyword. Imported libraries provide additional functionality or access to pre-defined functions and classes. Here's an example:

```frisky
import discord.frisk
```

In this example, a Frisky library named `discord.frisk` is imported.

To import default Python libraries or Frisky libraries located in the `libraries` folder without specifying the file extension, you can simply use the library name. Here's

 an example:

```frisky
import math
import mylibrary
```

In this example, the Python `math` library and the Frisky library `mylibrary.frisk` are imported.

## Garbage Collection

Frisky includes the `gc.collect` keyword, which performs garbage collection to free up memory occupied by unused objects. Here's an example:

```frisky
gc.collect()
```

This command triggers the garbage collection process.

Note: This documentation provides a general overview of the Frisky language and its features. For more detailed information and examples, please refer to the official Frisky documentation or tutorials.
