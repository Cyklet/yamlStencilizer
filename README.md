# YAML Parser for Stencil Templates

The python script that ingest a YAML file and generates code based on provided stencil templates. It supports specifying the target and template path via optional command-line arguments.

## Usage

```sh
python yaml_parser.py <yaml_path> [--target <target>] [--template_path <template_path>] [--final_file_name <file_name>] [--final_file_extension <file_extension>]
```

## Arguments

- `yaml_path`: Path to the YAML file containing the data.
- `--target <target>`: Optional. Specify the target for code generation at the moment available are swift_openapi && kotlin_openapi.
- `--template_path <template_path>`: Optional. Path to the stencil template file used for code generation.
- `final_file_name`: Name of the output file to save the generated code.
- `final_file_extension`: Extension of the output file to save the generated code.

## Example
```sh
python yaml_parser.py sample.yaml --target swift_openapi
```
OR

```sh
python yaml_parser.py sample.yaml --template_path custom_kotlin_template.stencil --final_file_name output_file --final_file_extension kt
```