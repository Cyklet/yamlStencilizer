from enum import Enum
# https://github.com/yaml/pyyaml
from pyyaml import safe_load
# https://github.com/pallets/jinja
from jinja2 import Environment, BaseLoader

class DataLoader:
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    def parse(self):
        try:
            with open(self.yaml_path, 'r') as yaml_file:
                return safe_load(yaml_file)
        except FileNotFoundError:
            raise ValueError(f"File '{self.yaml_path}' not found.")


class Template:
    def __init__(self, target=None, template_path=None, final_file_name=None, final_file_extension=None):
        self.final_file_name = final_file_name if final_file_name is not None else "default_output_file"
    
        if target is not None:
            self.template_path = target.stencil()
            self.final_file_extension = target.file_extension()
        elif template_path is not None:
            self.template_path = template_path
            self.final_file_extension = final_file_extension if final_file_extension is not None else "txt"
        else:
            raise ValueError("You must provide either 'target' or 'template_path' argument.")
 
    def generate(self, data):
        try:
            with open(self.template_path, 'r') as template_file:
                template_content = template_file.read()
        except FileNotFoundError:
            raise ValueError(f"File '{self.template_path}' not found.")
        env = Environment(loader=BaseLoader())
        template = env.from_string(template_content)
        rendered_content = template.render(data=data)
        self.__save(rendered_content)

    def __save(self, content):
        # Save the generated content to a new file
        file_name = f"temporary/{self.final_file_name}.{self.final_file_extension}"
        try:
            with open(file_name, 'w') as output_file:
                print("Absolute File Path:", output_file.name)
                output_file.write(content)
            return True
        except Exception as e:
            raise ValueError(f"Failed to save the file '{file_name}'. {e}")

 
class Target(Enum):
    SWIFT_OPEN_API = "swift_openapi"
    KOTLIN_OPEN_API = "kotlin_openapi"

    def file_extension(self):
        file_extensions = {
            Target.SWIFT_OPEN_API: "swift",
            Target.KOTLIN_OPEN_API: "kt"
        }
        return file_extensions[self]
    
    def stencil(self):
        file_extensions = {
            Target.SWIFT_OPEN_API: "resources/swift_open_api.stencil",
            Target.KOTLIN_OPEN_API: "resources/kotlin_open_api.stencil"
        }
        return file_extensions[self]


def generate(yaml_path, target, template_path, final_file_name, final_file_extension):
    data = DataLoader(yaml_path).parse()
    if target is not None:
        try:
            target_enum = Target(target.lower())
        except ValueError:
            raise ValueError(f"Invalid target '{target}'.")
        Template(target=target_enum, final_file_name=final_file_name).generate(data)
    elif template_path is not None:
        Template(template_path=template_path, final_file_name=final_file_name, final_file_extension=final_file_extension).generate(data)
    else:
        raise ValueError("You must provide either 'target' or 'template_path' argument.")
