import os  # Needed to be able to delete files

input_file = "./10000-most-common-passwords.csv"
output_file = "./statistics.csv"
delimiter = ","


def delete_existing_output_file(filename):
  if os.path.exists(filename):
    os.remove(filename)


def process_data(input_filename, delimiter):
  with open(input_filename, "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

  for line in lines:
    elements = line.split(delimiter)
    print(elements)  # Placeholder - you'll likely want to do more with the data


# Main execution
delete_existing_output_file(output_file)
process_data(input_file, delimiter)
