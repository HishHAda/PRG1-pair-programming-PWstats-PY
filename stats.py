import os  # Needed to be able to delete files

input_file = "./10000-most-common-passwords.csv"
output_file = "./statistics.csv"
delimiter = ","
password_dictionary = {} 


def delete_existing_output_file(filename):
  if os.path.exists(filename):
    os.remove(filename)


def process_data(input_filename, delimiter):
  with open(input_filename, "r", encoding="utf-8") as file:
    lines = file.read().splitlines()
  
  array = setup_password_array()

  for line in lines:
    elements = line.split(delimiter)
    array = store_length(elements[1],array) # Updates the array at every iteration

    #print(elements)  # Placeholder - you'll likely want to do more with the data
  
  return array # Returns the array to the main program (back to global frame)
  

def setup_password_array(): # Creates an array with 20 nested arrays
  master_array = []
  for num in range(20): 
    formatted_array = [f"CHAR: {num}",f"COUNT:",0]
    master_array.append(formatted_array)
  
  return master_array


def store_length(password,array):
  password_length = len(password)
  # Iterate through array to identify where CHAR num and password length are equal 
  # Proceed to update count within that specific array 
  
  array_position = array[password_length] # [CHAR 0, COUNT:]
  array_position[2] = array_position[2] + 1

  return array

# Writes in array form
"""def write_to_file(output_filename,array): 
  with open(output_filename, "w") as file: 
    for each in array: 
      file.write(str(each)+"\n")"""

# Writes in CSV format
def write_to_file(output_filename,array): 
  with open(output_filename, "w") as file: # Opens file, "w" used as we are not updating contents
    for each in array: # For each nested array within the array
      for element in each: # For each index within the nested array
        try: 
          if element == int(element): # Exception handling used as comparing a string causes an error
            file.write(str(element)+"\n") # This is done as the last element is an integer,
                                          # therefore making it a good identifier for when a new line 
                                          # is required
        except: 
          file.write(str(element)+",") # If the last element is not an integer, we know we are not 
                                       # at the end of the line, therefore we use the appropriate formatting


# Main execution
delete_existing_output_file(output_file)
array_of_processed_data = process_data(input_file, delimiter)
write_to_file(output_file,array_of_processed_data) # Writes processed data to a csv file
