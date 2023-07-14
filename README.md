# FRISKY-LANGUAGE
i know what youre saying "a scripting language made in python and only in one file? it probablt a piece of shit but trust me it is kind of good? i guess
AND BTW I DONT REALLY KNOW IF IT WORKS WELL I DIDNT REALLY TEST IT





Certainly! Here's an updated version of the documentation with added examples and a basic tutorial on how to create libraries:

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
- [Creating Libraries](#creating-libraries)

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
display.to_console("Hello, " + name)
```

In this example, the user is prompted with the question "What is your name?" and their input is stored in the `name` variable. The greeting message is then displayed.

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

Frisky also includes a built-in `graphics` library for graphics-related operations. It provides functions for creating a screen, updating the screen, loading images, and drawing shapes. Here's an example:

```frisky
import sdl2

setvariable window = screen_create(500, 500)
window.update()

window.load("example.png")
window.update()

graphics.draw_rect(window, (255, 255, 255), (50, 50, 100, 100))
window.update()
```

In this example, a window is created, an image is loaded onto the window, and a rectangle is drawn on the window using the `graphics.draw_rect()` function.

## Loops

Frisky includes the `while` keyword for creating while loops. The code block following the `while` statement will be executed repeatedly

 as long as the specified condition is true. Here's an example:

```frisky
setvariable counter = 0
while counter < 5
  display.to_console(counter)
  setvariable counter = counter + 1
end
```

In this example, the code block inside the `while` loop is executed as long as the `counter` variable is less than 5. The value of the `counter` variable is printed to the console, incremented by 1, and the loop continues until the condition is no longer true.

## Switch Cases

Frisky includes support for switch cases, allowing you to perform different actions based on the value of a variable. The `switch` keyword is used to start a switch case block, followed by one or more `case` statements to define specific cases, and an optional `default` statement for the default case. Here's an example:

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

## Importing Modules

Frisky allows you to import external Frisky modules or files using the `import` keyword. The imported modules can provide additional functionality or define reusable code. Here's an example:

```frisky
import mymodule

mymodule.my_function()
```

In this example, the `mymodule` module is imported, and the `my_function` function from the module is called.

## Creating Libraries

Frisky provides the ability to create libraries for encapsulating reusable code and functionality. Here's a basic tutorial on how to create libraries in Frisky:

1. Start by creating a new Frisky file with the desired name for your library. For example, `mylibrary.frisky`.

2. Define the functions and classes that make up your library. For example:

   ```frisky
   fun greet(name)
     display.to_console("Hello, " + name)
   end

   class Circle
     setvariable radius

     fun __init__(self, radius)
       self.radius = radius
     end

     fun area(self)
       return 3.14 * self.radius * self.radius
     end
   end
   ```

   In this example, the library includes a function `greet` that displays a greeting message and a class `Circle` that represents a circle with a given radius and provides a method to calculate its area.

3. Save the file `mylibrary.frisky` with your library code.

4. To use your library in another Frisky script, you can import it using the `import` keyword:

   ```frisky
   import mylibrary

   mylibrary.greet("Frisky")
   setvariable c = mylibrary.Circle(5)
   display.to_console("Area: " + c.area())
   ```

   In this example, the `mylibrary` is imported, and the `greet` function and `Circle` class from the library are used.

5. Save the script file that uses your library and run it using the Frisky interpreter.

By following these steps, you can create and use your own libraries in Frisky to encapsulate and reuse code.

---

This concludes the documentation for the Frisky scripting language. Use the provided keywords, constructs, and examples to write your own Frisky scripts and libraries. Have fun exploring the possibilities of Frisky!
