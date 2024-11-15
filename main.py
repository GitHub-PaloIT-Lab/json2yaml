import argparse
from converter import Converter  # Assuming the Converter class is in a file named converter.py

def main():
    parser = argparse.ArgumentParser(description='Convert JSON to YAML and vice versa.')
    parser.add_argument('--data', help='The data to be converted.')
    parser.add_argument('--file', help='The file containing the data to be converted.')
    args = parser.parse_args()

    converter = Converter(args.data, args.file)
    valid_data = converter.is_valid_type()
    if not valid_data:
        print("Invalid data type.")
        return
    print("Data type: " + converter.get_data_type())
    converted_data = converter.convert()
    print("New Data Type: " + converter.get_desired_output_data_type())
    print(" ")
    print("Converted Data:")
    print("---------------------------")
    print(converted_data)

if __name__ == '__main__':
    main()
