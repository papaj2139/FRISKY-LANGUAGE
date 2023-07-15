# FRISKY-LANGUAGE
i know what youre saying "a scripting language made in python and only in one file? it probablt a piece of shit but trust me it is kind of good? i guess
AND BTW I DONT REALLY KNOW IF IT WORKS WELL I DIDNT REALLY TEST IT AND SOMETIMES WAS TOO LAZY





# Frisky Scripting Language Documentation

Frisky is a simple scripting language designed to be easy to read and write. It provides a set of keywords and constructs for performing various operations, including conditional statements, variable manipulation, file and folder management, basic graphics and audio functionality, and more.

## Table of Contents

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
- [Importing Modules](#importing-modules)

## Keywords

Frisky includes the following keywords:

- `if`: Used to create conditional statements.
- `else`: Used in combination with `if` to create alternative branches in conditional statements.
- `ifelse`: Used to create conditional statements with two alternative branches.
- `and`: Used to combine conditions with logical AND.
- `or`: Used to combine conditions with logical OR.
- `not`: Used to negate a condition.
- `return`: Used to return a value from a function.
- `switch`: Used to start a switch case block.
- `case`: Used to define a case within a switch case block.
- `default`: Used to define the default case within a switch case block.
- `display.to_console()`: Used to print text to the console.
- `setvariable`: Used to create and assign values to variables.
- `lists`: Used to create lists (arrays) of values.
- `dictionaries`: Used to create dictionaries (key-value pairs).
- `import`: Used to import external Frisky modules or files.
- `ask()`: Used to get user input.
- `file.create()`: Used to create files.
- `file.delete()`: Used to delete files.
- `folder.create()`: Used to create folders.
- `folder.delete()`: Used to delete folders.
- `while`: Used to create while loops.
- `end`: Used to mark the end of blocks, such as if statements, loops, functions, and classes.
- `range`: Used to generate a list of numbers within a specified range.
- `in`: Used to check if an item is present in a container.
- `is`: Used to check if two objects are the same.

## Variables

Variables in Frisky are dynamically typed and can hold various types of values, such as numbers, strings, lists, and dictionaries. Variables are created using the `setvariable` keyword followed by the variable name and the assigned value. Here's an example:

```frisky
setvariable x = 5
```



In this example, a variable `x` is created and assigned the value of 5.

## Conditional Statements

Frisky supports conditional statements for executing different blocks of code based on certain conditions. The `if` statement is used to create a basic condition, while `else` is used to define an alternative block of code to execute when the condition is not met. The `ifelse` statement combines both conditions. Here's an example:

```frisky
if x > 0
  display.to_console("Positive")
else
  display.to_console("Non-positive")
end
```

In this example, the code block inside the `if` statement is executed if the value of `x` is greater than 0. Otherwise, the code block inside the `else` statement is executed.

Frisky also provides logical operators such as `and`, `or`, and `not` to combine and negate conditions.

## Input and Output

Frisky provides the `display.to_console()` function for printing text to the console. It takes a string as an argument and displays it on the console output. Here's an example:

```frisky
display.to_console("Hello, Frisky!")
```

The output of this code would be:

```
Hello, Frisky!
```

To get user input, Frisky provides the `ask()` function. It takes a prompt as an argument and returns the user's input. Here's an example:

```frisky
setvariable name = ask("What is your name?")
```

In this example, the user is prompted with the question "What is your name?" and their input is stored in the `name` variable.

## File and Folder Management

Frisky provides functions for creating and deleting files and folders. The `file.create()` function is used to create a new file, while `file.delete()` is used to delete a file. Here's an example:

```frisky
file.create("output.txt")
file.delete("output.txt")
```

The above code creates a file named "output.txt" and then deletes it.

Similarly, the `folder.create()` function creates a new folder, and `folder.delete()` deletes a folder. Here's an example:

```frisky
folder.create("data")
folder.delete("data")
```

In this example, a folder named "data" is created and then deleted.

## Graphics and Audio

Frisky supports basic graphics and audio functionality through external modules. To use these features, you can import external Frisky modules or files using the `import` keyword.

Frisky includes a built-in `sdl2` module for graphics and audio operations. It provides functions for creating a screen, updating the screen, loading images, and drawing shapes. Here's an example:

```frisky
import sdl2

setvariable window = sdl2.screen_create(500, 500)
window.update()

window.load("example.png")
window.update()

sdl2.draw_rect(window, (255, 255, 255), (50, 50, 100, 100))
window.update()
```

In this example, a window is created, an image is loaded onto the window, and a rectangle is drawn on the window using the `sdl2.draw_rect()` function.

## Loops

Frisky includes the `while` keyword for creating while loops and the `for` keyword for creating for loops. The code block following the `while` or `for` statement will be executed repeatedly as long as the specified condition is true or for each item in a container. Here's an example of a `while` loop:

```frisky
setvariable counter = 0
while counter < 5
  display.to_console(counter)
  setvariable counter = counter + 1
end
```

In this example, the code block inside the `while` loop is executed as long as the `counter` variable is less than 5. The value of the `counter` variable is printed to the console, incremented by 1, and the loop continues until the condition is no longer true.

Here's an example of a `for` loop:

```frisky
for i in range(5)
  display.to_console(i)
end
```

In this example, the code block inside the `for` loop is executed for each value in the range from 0 to 4.

## Switch Cases

Frisky provides the `switch`, `case`, and `default` keywords for creating switch case statements. A switch case statement allows you to compare a value against multiple cases

 and execute different code blocks based on the matched case. Here's an example:

```frisky
switch x
  case 1
    display.to_console("One")
  case 2
    display.to_console("Two")
  default
    display.to_console("Other")
end
```

In this example, the value of `x` is compared against the cases. If `x` is 1, the code block inside the first case is executed. If `x` is 2, the code block inside the second case is executed. If `x` doesn't match any case, the code block inside the `default` case is executed.

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

## Importing Modules

Frisky allows you to import external Frisky modules or files using the `import` keyword. Imported modules or files can provide additional functionality or access to external libraries. Here's an example:

```frisky
import mymodule

mymodule.myfunction()
```

In this example, a module named `mymodule` is imported, and a function named `myfunction` from that module is called.

Note: This documentation provides a general overview of the Frisky language and its features. For more detailed information and examples, please refer to the official Frisky documentation or tutorials.
```

You can now copy and paste the updated documentation into your GitHub repository.
