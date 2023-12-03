import json
from clr_loader import get_coreclr
runtime = get_coreclr()
from pythonnet import load
load("coreclr")

import clr
clr.AddReference("Test.Infrastructure.DavidUtils")
from Test.Infrastructure.DavidUtils import Functions


fullpath = "C:\\Users\\avivshi\\source\\repos\\pythonnetTest\\PythonNetTest\\davidObj.json"
file_path = "davidObj.json"

try:
    # Read the JSON content from the file
    with open(file_path, "r") as file:
        json_data = json.load(file)

    # Convert Python dictionary to JSON string
    json_string = json.dumps(json_data)

    print(json_string)
    # Call the DeserializeDavidFromJson function from the .NET assembly
    david = Functions.DeserializeDavidFromJsonString(json_string)

    # Access the properties
    print(f"Name: {david.Name}")
    print(f"Description: {david.Description}")
    print(f"Numbers: {list(david.Numbers)}")
    print(f"Gender: {david.GetGender()}")
    print(f"Type of Gender: {type(david.Gender)}")

except Exception as e:
    print(f"Error: {e}")
# print(f"Name: {david_instance.Name}")
# print(f"Description: {david_instance.Description}")
# print(f"Numbers: {list(david_instance.Numbers)}")
# print(f"Gender: {david_instance.GetGender()}")
# print(type(david_instance.Gender))
# Ensure "Numbers" is a list of floats (converted from integers)
# numbers_list = [float(number) for number in json_data.get("Numbers", [])]

# # Convert the Python list to a .NET array of floats
# numbers_array = Array[float](numbers_list)

# # Create a .NET instance of the David class using PythonNET
# gender_mapping = {"Male": Gender.Male, "Female": Gender.Female}
# gender_enum = gender_mapping.get(json_data.get("Gender", "Male"), Gender.Male)  # Assuming "Male" is a default value if "Gender" is not present
# david_instance = David(json_data.get("Name", ""), json_data.get("Description", ""), numbers_array, gender_enum)

# # Access the properties
# print(david_instance.Name)
# print(david_instance.Description)
# print(list(david_instance.Numbers))
# print(david_instance.GetGender())







# gender = Gender.Male
# numbers_list = [1.2, 1, 2.5, 8.5]

# # Convert the Python list to a .NET array
# numbers_array = Array[float](numbers_list)

# david = David("david1", "davidTest", numbers_array, gender)
# print(list(david.numbers))