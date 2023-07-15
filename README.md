# FRISKY-LANGUAGE
i know what youre saying "a scripting language made in python and only in one file? it probablt a piece of shit but trust me it is kind of good? i guess
AND BTW I DONT REALLY KNOW IF IT WORKS WELL I DIDNT REALLY TEST IT





# Frisky Scripting Language Documentation

Frisky is a high-level scripting language designed to be easy to read and write. It provides a set of keywords and constructs for performing various operations, including conditional statements, variable manipulation, file and folder management, basic graphics and audio functionality, and more.

## Table of Contents

- [Introduction](#introduction)
- [Language Type](#language-type)
- [Keywords](#keywords)
- [Variables](#variables)
- [Conditional Statements](#conditional-statements)
- [Input and Output](#input-and-output)
- [File and Folder Management](#file-and-folder-management)
- [Graphics and Audio](#graphics-and-audio)
- [Loops](#loops)
- [Switch Cases](#switch-cases)
- [Functions](#functions)
- [Classes](#classes)
- [Modules](#modules)
- [Language Possibilities](#language-possibilities)
- [Conclusion](#conclusion)

## Introduction

Frisky is a versatile scripting language that provides an easy-to-understand syntax for writing scripts. It is designed to be beginner-friendly while still offering powerful features for more advanced users. Frisky allows you to automate tasks, create simple applications, and explore creative programming ideas.

## Language Type

Frisky is a high-level scripting language. It abstracts away many low-level details and provides a simplified syntax that is easier to read and write compared to low-level languages like C or assembly. Frisky prioritizes developer productivity and readability, making it suitable for rapid prototyping and scripting tasks.

## Keywords

Frisky includes a set of keywords that provide the foundation for writing scripts. These keywords are used to define control flow, manipulate variables, perform input and output operations, manage files and folders, create graphics and audio, and more. Some of the keywords include:

- `if`, `else`, `ifelse`: Conditionals for branching execution based on conditions.
- `for`: Loop construct for repeating a block of code a specified number of times.
- `display.to_console()`: Outputs text to the console.
- `setvariable`: Assigns values to variables.
- `create_file`, `delete_file`: Creates and deletes files.
- `create_folder`, `delete_folder`: Creates and deletes folders.
- `create_list`: Creates a list (array) to store multiple values.
- `append`, `pop`: Modifies lists by adding or removing elements.
- `import`: Imports external Frisky modules or files.
- `switch`, `case`, `default`: Enables branching based on a variable's value.
- `fun`: Defines functions.
- `class`: Defines classes for object-oriented programming.

These keywords form the building blocks of Frisky scripts and allow you to express complex logic and operations concisely.

## Variables

Frisky supports variables, which are used to store and manipulate data during script execution. Variables in Frisky are dynamically typed, meaning you don't have to specify their type explicitly. They can hold various types of values, including numbers, strings, lists, and dictionaries.

Variables are created and assigned values using the `setvariable` keyword. For example:

```frisky
setvariable x = 10
setvariable name = "Frisky"
```

In this example, `x` is assigned the value 10, and `name` is assigned the string "Frisky". Variables can be accessed and modified throughout the script, enabling you to store and manipulate data as needed.

## Conditional Statements

Frisky provides conditional statements to control the flow of execution based on specific conditions. These statements allow you to perform different actions depending on whether a condition is true or false.

The `if` statement is used to create a basic condition. Here's an example:

```frisky
if x > 0
  display.to_console("Positive")
end
```

In this example, the code block inside the `if` statement is executed if the value of `x` is greater than 0.

Frisky also supports `else` and `ifelse` statements to create alternative branches in conditional statements. The `else` statement defines a block of code to execute when the condition is not met. The `ifelse` statement combines both conditions. Here's an example:

```frisky
if x > 0
  display.to_console("Positive")
else
  display.to_console("Non-positive")
end
```

In this example, if the value of `x` is greater than 0, "Positive" is displayed. Otherwise, "Non-positive" is displayed.

## Input and Output

Frisky provides functions for input and output operations. The `display.to_console()` function is used to print text to the console. It takes a string as an argument and displays it on the console output. Here's an example:

```frisky
display.to_console("Hello, Frisky!")
```

The output of this code would be:

```
Hello, Frisky!
```

To get user input, Frisky provides the `ask()` function. It takes a prompt as an argument and returns the user's input. Here's an example:

```frisky
setvariable name = ask("

What is your name?")
```

In this example, the user is prompted with the question "What is your name?" and their input is stored in the `name` variable.

## File and Folder Management

Frisky provides functions for creating, reading, and deleting files and folders. These functions allow you to perform basic file and folder operations within your scripts.

The `create_file()` function is used to create a new file, while `delete_file()` is used to delete a file. Here's an example:

```frisky
create_file("output.txt")
delete_file("output.txt")
```

The above code creates a file named "output.txt" and then deletes it.

Similarly, the `create_folder()` function creates a new folder, and `delete_folder()` deletes a folder. Here's an example:

```frisky
create_folder("data")
delete_folder("data")
```

In this example, a folder named "data" is created and then deleted.

## Graphics and Audio

Frisky supports basic graphics and audio functionality through external modules. To use these features, you can import external Frisky modules or files using the `import` keyword.

Frisky also includes a built-in `graphics` library for graphics-related operations. It provides functions for creating a screen, updating the screen, loading images, and drawing shapes. Here's an example:

```frisky
import graphics

setvariable window = screen_create(500, 500)
window.update()

window.load("example.png")
window.update()

graphics.draw_rect(window, (255, 255, 255), (50, 50, 100, 100))
window.update()
```

In this example, a window is created, an image is loaded onto the window, and a rectangle is drawn on the window using the `graphics.draw_rect()` function.

## Loops

Frisky includes the `for` loop construct for iterating over a sequence of values a specified number of times. The code block inside the loop is executed repeatedly for each iteration. Here's an example:

```frisky
for i in range(5)
  display.to_console(i)
end
```

In this example, the code block inside the `for` loop is executed five times, with the value of `i` ranging from 0 to 4. The value of `i` is displayed on the console for each iteration.

## Switch Cases

Frisky provides support for switch cases, allowing you to perform different actions based on the value of a variable. The `switch` keyword is used to start a switch case block, followed by one or more `case` statements to define specific cases, and an optional `default` statement for the default case. Here's an example:

```frisky
switch x
  case 1
    display.to_console("Case 1")
  case 2
    display.to_console("Case 2")
  default
    display.to_console("Default Case")
end
```

In this example, the code block inside the corresponding `case` statement is executed based on the value of the variable `x`. If `x` is 1, "Case 1" is displayed. If `x` is 2, "Case 2" is displayed. Otherwise, if none of the cases match, "Default Case" is displayed.

## Functions

Frisky allows you to define and call functions using the `fun` keyword. Functions are defined with a name and a block of code. Here's an example:

```frisky
fun greet(name)
  display.to_console("Hello, " + name)
end

greet("Frisky")
```

In this example, a function named `greet` is defined with a parameter `name`. The function displays a greeting message with the provided name. The function is then called with the argument "Frisky".

## Classes

Frisky supports object-oriented programming with classes. Classes can be defined using the `class` keyword, followed by the class name and a block of code. Here's an example:

```frisky
class Person
  setvariable name

  fun __init__(self, name)
    self.name = name
  end

  fun greet(self)
    display.to_console("Hello, " + self.name)
  end
end

setvariable person = Person("Frisky")
person.greet()
```

In this example, a class named `Person` is defined with an `__init__` method for initialization and a `greet` method for greeting. An instance of the `Person` class is created with the name "Frisky", and the `greet` method is called on the instance.

## Modules

Frisky allows you to import external Frisky modules or files using the `import` keyword. The imported modules can provide additional functionality or define reusable code. Here's an example:

```frisky
import mymodule

mymodule.my_function()
```

In this example, the `mymodule` module is imported, and the `my_function` function from the module is called.

## Language Possibilities

Frisky offers a wide range of possibilities for script development. Some potential use cases and areas where Frisky can be applied include:

- Scripting automation tasks: Frisky can be used to automate repetitive tasks and simplify

 complex workflows.
- Rapid prototyping: Frisky's easy-to-read syntax and high-level abstractions make it suitable for quickly testing ideas and building prototypes.
- Simple application development: Frisky can be used to develop lightweight applications, such as command-line tools or small utilities.
- Data processing and analysis: Frisky provides features for handling files, folders, and data structures, making it suitable for data processing and analysis tasks.
- Game development: Frisky's graphics and audio capabilities, combined with its simplicity, make it a viable option for developing simple games and interactive experiences.

The possibilities are not limited to these examples, as Frisky's flexibility allows you to explore various domains and tailor the language to suit your specific needs.

## Conclusion

Frisky is a high-level scripting language that offers an accessible and expressive syntax for writing scripts. It provides a comprehensive set of keywords and constructs for performing a wide range of operations. Whether you're a beginner or an experienced programmer, Frisky's simplicity and versatility make it a valuable tool for automating tasks, prototyping ideas, and exploring creative programming concepts.

Explore the Frisky language, experiment with its features, and unleash your programming potential!
