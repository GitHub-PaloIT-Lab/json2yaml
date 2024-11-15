import os
import json
import yaml



class Converter:
    def __init__(self, data=None, file_path=None):
        self.file_path = file_path
        if data:
            self.raw_data = data
        elif file_path:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} does not exist.")
            self.load_data_from_file(file_path)

        self.data_type = self.determine_data_type()

    def get_data_type(self):
        return self.data_type

    def is_valid_type(self):
        return self.data_type != 'unknown'

    def get_desired_output_data_type(self):
        if self.data_type == 'json':
            return 'yaml'
        elif self.data_type == 'yaml':
            return 'json'
        else:
            return 'unknown'

    def load_data(self):
        if self.data_type == 'json':
            try:
                return json.loads(self.raw_data)
            except ValueError as ve:
                return "Invalid JSON data. Error: " + str(ve)
        elif self.data_type == 'yaml':
            try:
                return yaml.safe_load(self.raw_data)
            except yaml.YAMLError as ye:
                return "Invalid YAML data. Error: " + str(ye)
        else:
            return "unknown"

    def determine_data_type(self):
        try:
            json.loads(self.raw_data)
            return 'json'
        except ValueError:
            pass
        try:
            yaml.safe_load(self.raw_data)
            return 'yaml'
        except yaml.YAMLError:
            pass
        return 'unknown'

    def to_json(self):
        return json.dumps(self.load_data())

    def to_yaml(self):
        return yaml.dump(self.load_data())

    def convert(self):
        if self.file_path:
            self.write_data_to_file()
            return self.convert_string()
        else:
            return self.convert_string()

    def convert_string(self):
        if self.data_type == 'json':
            return self.to_yaml()
        elif self.data_type == 'yaml':
            return self.to_json()
        else:
            return "Invalid data type."

    def load_data_from_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
        with open(file_path, 'r') as file:
            self.raw_data = file.read()
        #self.data_type = self.determine_data_type()
        #return self.load_data()
            #self.data_type = self.determine_data_type()
            return True

    def get_new_output_type(self):
        if self.data_type == 'json':
            return 'yaml'
        elif self.data_type == 'yaml':
            return 'json'
        else:
            return 'unknown'

    def get_output_file_path(self):
        if self.data_type == 'json':
            return self.file_path.replace('.json', '.yaml')
        elif self.data_type == 'yaml':
            return self.file_path.replace('.yaml', '.json')
        else:
            return f"{self.file_path}.{self.get_new_output_type()}"

    def write_data_to_file(self):
        output_file_path = self.get_output_file_path()
        print(f"Writing converted data to {output_file_path}")
        if self.get_new_output_type() == 'json':
            output = self.to_json()
        elif self.get_new_output_type() == 'yaml':
            output = self.to_yaml()
        with open(output_file_path, 'w') as file:
            file.write(output)
