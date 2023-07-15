import os

class FriskyInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.classes = {}

    def interpret_line(self, line):
        line = line.strip()

        if line == "" or line.startswith("<"):
            return

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
        elif line.startswith("for"):
            self.execute_for(line)
        elif line.startswith("import"):
            self.execute_import(line)
        elif line.startswith("create_file"):
            self.execute_create_file(line)
        elif line.startswith("delete_file"):
            self.execute_delete_file(line)
        elif line.startswith("create_folder"):
            self.execute_create_folder(line)
        elif line.startswith("delete_folder"):
            self.execute_delete_folder(line)
        elif line.startswith("create_list"):
            self.execute_create_list(line)
        elif line.startswith("create_dict"):
            self.execute_create_dict(line)
        elif line.startswith("switch"):
            self.execute_switch(line)
        elif line.startswith("case"):
            self.execute_case(line)
        elif line.startswith("default"):
            self.execute_default()
        elif line.startswith("return"):
            self.execute_return(line)
        elif line.startswith("and"):
            self.execute_and(line)
        elif line.startswith("or"):
            self.execute_or(line)
        elif line.startswith("not"):
            self.execute_not(line)
        elif line.startswith("range"):
            self.execute_range(line)
        elif line.startswith("in"):
            self.execute_in(line)
        elif line.startswith("is"):
            self.execute_is(line)
        elif line.startswith("end"):
            self.execute_end()
        elif line.startswith("fun"):
            self.execute_function(line)
        elif line.startswith("class"):
            self.execute_class(line)
        elif line.startswith("append"):
            self.execute_append(line)
        elif line.startswith("pop"):
            self.execute_pop(line)
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

    def execute_create_file(self, line):
        _, filename = line.split()
        filename = filename.strip()

        try:
            open(filename, "w").close()
        except Exception as e:
            print(f"Error creating file: {e}")

    def execute_delete_file(self, line):
        _, filename = line.split()
        filename = filename.strip()

        try:
            os.remove(filename)
        except Exception as e:
            print(f"Error deleting file: {e}")

    def execute_create_folder(self, line):
        _, foldername = line.split()
        foldername = foldername.strip()

        try:
            os.mkdir(foldername)
        except Exception as e:
            print(f"Error creating folder: {e}")

    def execute_delete_folder(self, line):
        _, foldername = line.split()
        foldername = foldername.strip()

        try:
            os.rmdir(foldername)
        except Exception as e:
            print(f"Error deleting folder: {e}")

    def execute_create_list(self, line):
        _, list_name = line.split()
        list_name = list_name.strip()

        self.variables[list_name] = []

    def execute_create_dict(self, line):
        _, dict_name = line.split()
        dict_name = dict_name.strip()

        self.variables[dict_name] = {}

    def execute_switch(self, line):
        _, expression = line.split(" ", 1)
        expression = expression.strip()

        try:
            value = eval(expression, self.variables)
        except Exception as e:
            print(f"Error evaluating switch expression: {e}")
            return

        while True:
            line = input()
            if line.startswith("case"):
                _, case_value = line.split(" ", 1)
                case_value = case_value.strip()

                if case_value == str(value):
                    self.execute_block()
                    break
            elif line.startswith("default"):
                self.execute_block()
                break
            elif line.startswith("end"):
                break

    def execute_case(self, line):
        pass

    def execute_default(self):
        pass

    def execute_return(self, line):
        _, expression = line.split(" ", 1)
        expression = expression.strip()

        try:
            return_value = eval(expression, self.variables)
        except Exception as e:
            print(f"Error evaluating return expression: {e}")
            return

        self.variables["_return"] = return_value

    def execute_and(self, line):
        _, condition = line.split(" ", 1)
        condition = condition.strip()

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        return result

    def execute_or(self, line):
        _, condition = line.split(" ", 1)
        condition = condition.strip()

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        return result

    def execute_not(self, line):
        _, condition = line.split(" ", 1)
        condition = condition.strip()

        try:
            result = eval(condition, self.variables)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return

        return not result

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

    def execute_append(self, line):
        _, list_name, value = line.split(" ", 2)
        list_name = list_name.strip()
        value = value.strip()

        try:
            self.variables[list_name].append(eval(value, self.variables))
        except Exception as e:
            print(f"Error appending to list: {e}")
    

    def execute_range(self, line):
        _, start, stop, step = line.split()
        start = int(start.strip())
        stop = int(stop.strip())
        step = int(step.strip())

        try:
            result = list(range(start, stop, step))
            self.variables["_range"] = result
        except Exception as e:
            print(f"Error executing range: {e}")

    def execute_in(self, line):
        _, item, container = line.split()
        item = item.strip()
        container = container.strip()

        try:
            result = eval(item, self.variables) in eval(container, self.variables)
            self.variables["_in"] = result
        except Exception as e:
            print(f"Error executing in: {e}")

    def execute_is(self, line):
        _, item1, item2 = line.split()
        item1 = item1.strip()
        item2 = item2.strip()

        try:
            result = eval(item1, self.variables) is eval(item2, self.variables)
            self.variables["_is"] = result
        except Exception as e:
            print(f"Error executing is: {e}")

    def execute_pop(self, line):
        _, list_name = line.split()
        list_name = list_name.strip()

        try:
            self.variables[list_name].pop()
        except Exception as e:
            print(f"Error popping from list: {e}")

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
