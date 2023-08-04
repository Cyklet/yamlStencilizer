import argparse
import file_generator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OpenAPI YAML code files for provided templates.")
    parser.add_argument("yaml_path", type=str, help="The path to the YAML file.")
    parser.add_argument("--target", type=str, help="The target for which to generate code.")
    parser.add_argument("--template_path", type=str, help="The path to the template file.")
    parser.add_argument("--final_file_name", type=str, help="The name of the final file.")
    parser.add_argument("--final_file_extension", type=str, help="The extension of the final file.")
    args = parser.parse_args()
    
    file_generator.generate(yaml_path=args.yaml_path, target=args.target, template_path=args.template_path, final_file_name=args.final_file_name, final_file_extension=args.final_file_extension)