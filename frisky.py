import importlib.util
import os



imported_modules = {}


class FriskyInterpreter:
    def __init__(self):
        self.variables = {}  

    def run(self, code):
        lines = code.split('\n')
        index = 0
        while index < len(lines):
            line = lines[index]
            line = self.remove_comments(line)  
            if line.startswith("if"):
                condition = line[3:]
                if condition:
                    self.interpret_block(lines, index + 1)
                else:
                    index = self.find_end_index(lines, index)
            elif line.startswith("else"):
                index = self.find_end_index(lines, index)
            elif line.startswith("ifelse"):
                condition = line[7:]
                if condition:
                    self.interpret_block(lines, index + 1)
                else:
                    self.interpret_block(lines, index + 1)
            elif line.startswith("display.to_console"):
                content = line.split('(', 1)[1].split(')')[0]
                if content in self.variables:
                    print(self.variables[content])
                else:
                    print(content)
            elif line.startswith("setvariable"):
                parts = line.split('=', 1)
                variable_name = parts[0][12:].strip()
                value = parts[1].strip()
                self.variables[variable_name] = value
            elif line.startswith("lists"):
                parts = line.split('=', 1)
                list_name = parts[0][5:].strip()
                values = parts[1].strip()
                self.variables[list_name] = [value.strip() for value in values.split(',')]
            elif line.startswith("dictionaries"):
                parts = line.split('=', 1)
                dict_name = parts[0][12:].strip()
                entries = parts[1].strip().split(',')
                dictionary = {}
                for entry in entries:
                    key, value = entry.split(':')
                    dictionary[key.strip()] = value.strip()
                self.variables[dict_name] = dictionary
            elif line.startswith("import"):
                module_name = line[7:].strip()
                if module_name.endswith(".frisk"):
                    module_name = module_name[:-6]
                    imported_modules[module_name] = self.import_module(module_name)
            elif line.startswith("ask"):
                parts = line.split('=', 1)
                variable_name = parts[0][12:].strip()
                prompt = parts[1].strip()[1:-1]  
                value = input(prompt)
                self.variables[variable_name] = value
                self.interpret_line(f"display.to_console({variable_name})")  
            elif line.startswith("file.create"):
                file_path = line[12:].strip()[1:-1]  
                with open(file_path, "w") as file:
                    pass
            elif line.startswith("file.delete"):
                file_path = line[12:].strip()[1:-1]  
                if os.path.exists(file_path):
                    os.remove(file_path)
            elif line.startswith("folder.create"):
                folder_path = line[14:].strip()[1:-1]  
                os.makedirs(folder_path, exist_ok=True)
            elif line.startswith("folder.delete"):
                folder_path = line[14:].strip()[1:-1]  
                if os.path.exists(folder_path):
                    os.rmdir(folder_path)
            elif line.startswith("end"):
                return
            elif line.startswith("while"):
                condition = line[6:]
                while condition:
                    index += 1
                    if index < len(lines):
                        self.interpret_line(lines[index])
                    else:
                        break
            else:
                self.evaluate_expression(line)

            index += 1

    def interpret_block(self, lines, start_index):
        block_lines = []
        indent_level = 1
        index = start_index
        while index < len(lines) and indent_level > 0:
            line = lines[index]
            line = self.remove_comments(line)  
            if line.startswith("end"):
                indent_level -= 1
            elif line.startswith("if") or line.startswith("else") or line.startswith("ifelse"):
                indent_level += 1
            block_lines.append(line)
            index += 1

        block_code = '\n'.join(block_lines)
        self.run(block_code)

    def evaluate_expression(self, expression):
        if "math" in expression:
            expression = expression.replace("math", "Math")
        exec(expression, globals(), self.variables)

    def import_module(self, module_name):
        if module_name in imported_modules:
            return imported_modules[module_name]

        module_path = os.path.join("libraries", module_name + ".py")
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        imported_modules[module_name] = module
        return module

    def remove_comments(self, line):
        comment_start = line.find("<")
        comment_end = line.find(">")
        if comment_start != -1 and comment_end != -1:
            line = line[:comment_start] + line[comment_end+1:]
        return line


# Example usage
interpreter = FriskyInterpreter()
interpreter.run("""

""")
