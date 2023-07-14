# FRISKY-LANGUAGE
i know what youre saying "a scripting language made in python and only in one file? it probablt a piece of shit but trust me it is kind of good? i guess



Certainly! Here's a sample documentation for the Frisky scripting language that you can paste into your GitHub repository:

# Frisky Scripting Language Documentation

Frisky is a simple scripting language designed to be easy to read and write. It provides a set of keywords and constructs for performing various operations, including conditional statements, variable manipulation, file and folder management, and basic graphics and audio functionality.

## Table of Contents

- [Keywords](#keywords)
- [Variables](#variables)
- [Conditional Statements](#conditional-statements)
- [Input and Output](#input-and-output)
- [File and Folder Management](#file-and-folder-management)
- [Graphics and Audio](#graphics-and-audio)
- [Loops](#loops)
- [Importing Modules](#importing-modules)

## Keywords

Frisky includes the following keywords:

- `if`: Used to create conditional statements.
- `else`: Used in combination with `if` to create alternative branches in conditional statements.
- `ifelse`: Used to create conditional statements with two alternative branches.
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
- `end`: Used to mark the end of blocks, such as if statements, loops, and functions.

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

Frisky supports basic graphics and audio functionality through external modules. To use these features, you can import the `frisky_graphics` module and make use of its functions.

Here's an example of creating a window, updating the window, loading an image, and playing a sound:

```frisky
import frisky_graphics

setvariable window = screen_create(500, 500)
window.update()

window.load("example.png")
window.update()

setvariable sound = sound_load("example.wav")
sound.play()
```

In this example, the `screen_create()` function creates a window, `window.update()` updates the window display, `window.load()` loads an image onto the window, and `sound_load()` and `sound.play()` load and play a sound, respectively.

## Loops

Frisky includes the `while` keyword for creating while loops. The code block following the `while` statement will be executed repeatedly as long as the specified condition is true. Here's an example:

```frisky
setvariable counter = 0
while counter < 5
  display.to_console(counter)
  setvariable counter = counter + 1
end
```

In this example, the code block inside the `while` loop is executed as long as the `counter` variable is less than 5. The value of the `counter` variable is printed to the console, incremented by 1, and the loop continues until the condition is no longer true.

## Importing Modules

Frisky allows you to import external Frisky modules or files using the `import` keyword. The imported modules can provide additional functionality or define reusable code.

To import a module, use the `import` keyword followed by the module name. Here's an example:

```frisky
import frisky_graphics
```

In this example, the `frisky_graphics` module is imported and can be used to access its functions and features.

---

This concludes the documentation for the Frisky scripting language. Feel free to customize and expand upon this documentation as needed for your specific project.

Happy scripting with Frisky!
