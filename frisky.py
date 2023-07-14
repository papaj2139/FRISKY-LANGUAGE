import os

class FriskyInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.classes = {}

    def interpret_line(self, line):
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines or comments
        if line == "" or line.startswith("<"):
            return

        # Check for keywords and execute corresponding actions
        if line.startswith("setvariable"):
            self.execute_set_variable(line)
        elif line.startswith("display.to_console"):
            self.execute_display_to_console(line)
        elif line.startswith("if"):
            self.execute_if(line)
        elif line.startswith("else"):
            self.execute_else()
        elif line.startswith("ifelse"):
            self.execute_if_else(line)
        elif line.startswith("and"):
            self.execute_and(line)
        elif line.startswith("or"):
            self.execute_or(line)
        elif line.startswith("not"):
            self.execute_not(line)
        elif line.startswith("return"):
            self.execute_return(line)
        elif line.startswith("switch"):
            self.execute_switch(line)
        elif line.startswith("case"):
            self.execute_case(line)
        elif line.startswith("default"):
            self.execute_default()
        elif line.startswith("end"):
            self.execute_end()
        elif line.startswith("import"):
            self.execute_import(line)
        elif line.startswith("fun"):
            self.execute_function(line)
        elif line.startswith("class"):
            self.execute_class(line)
        else:
            print(f"Invalid syntax: {line}")

    def execute_set_variable(self, line):
        _, expression = line.split("=", 1)
        expression = expression.strip()

        try:
            exec(f"result = {expression}", self.variables)
        except Exception as e:
            print(f"Error setting variable: {e}")
            return

        variable_name = line.split()[1]
        self.variables[variable_name] = self.variables["result"]
        del self.variables["result"]

    def execute_display_to_console(self, line):
        _, expression = line.split("(", 1)
        expression = expression[:-1].strip()

        try:
            print(eval(expression, self.variables))
        except Exception as e:
            print(f"Error displaying to console: {e}")

    def execute_if(self, line):
        _, condition = line.split(" ", 1)

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        if result:
            self.execute_block()

    def execute_else(self):
        self.execute_block()

    def execute_if_else(self, line):
        _, condition = line.split(" ", 1)

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        if result:
            self.execute_block()
        else:
            self.execute_block()

    def execute_and(self, line):
        _, condition = line.split(" ", 1)

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        if result:
            self.execute_block()

    def execute_or(self, line):
        _, condition = line.split(" ", 1)

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        if result:
            self.execute_block()

    def execute_not(self, line):
        _, condition = line.split(" ", 1)

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        if not result:
            self.execute_block()

    def execute_return(self, line):
        _, expression = line.split(" ", 1)
        expression = expression.strip()

        try:
            result = eval(expression, self.variables)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return

        print(f"Return: {result}")

    def execute_switch(self, line):
        _, expression = line.split(" ", 1)
        expression = expression.strip()

        try:
            self.switch_value = eval(expression, self.variables)
            self.is_switch_case = False
        except Exception as e:
            print(f"Error evaluating switch expression: {e}")

    def execute_case(self, line):
        _, expression = line.split(" ", 1)
        expression = expression.strip()

        try:
            case_value = eval(expression, self.variables)
        except Exception as e:
            print(f"Error evaluating case expression: {e}")
            return

        if self.is_switch_case or self.switch_value == case_value:
            self.is_switch_case = True
            self.execute_block()

    def execute_default(self):
        if not self.is_switch_case:
            self.execute_block()

    def execute_block(self):
        indentation = 1
        while True:
            line = input()
            if line.startswith("end"):
                indentation -= 1
                if indentation == 0:
                    break
            if line.endswith(" {"):
                indentation += 1

            self.interpret_line(line)

    def execute_end(self):
        pass

    def execute_import(self, line):
        _, module = line.split()
        module = module.strip()

        try:
            exec(f"import {module}", self.variables)
        except Exception as e:
            print(f"Error importing module: {e}")

    def execute_function(self, line):
        _, function = line.split()
        function = function.strip()

        lines = []
        indentation = 1

        while True:
            line = input()
            if line.endswith(" {"):
                indentation += 1
            if line.startswith("}"):
                indentation -= 1
                if indentation == 0:
                    break
            lines.append(line)

        self.functions[function] = lines

    def execute_class(self, line):
        _, class_name = line.split()
        class_name = class_name.strip()

        lines = []
        indentation = 1

        while True:
            line = input()
            if line.endswith(" {"):
                indentation += 1
            if line.startswith("}"):
                indentation -= 1
                if indentation == 0:
                    break
            lines.append(line)

        self.classes[class_name] = lines

    def run_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    self.interpret_line(line)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error running file: {e}")


interpreter = FriskyInterpreter()
interpreter.run_file("script.frisk")
