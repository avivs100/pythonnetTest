import clr
<<<<<<< HEAD

clr.AddReference("Aviv.Test")
clr.AddReference("Ice.Domain")
clr.AddReference("Ice.Shared")
=======
clr.AddReference("Test.Infrastructure.DavidUtils")
clr.AddReference("davidProj")
clr.AddReference("System")
import json
from Test.Infrastructure.DavidUtils import Functions
from davidProj import David
>>>>>>> b5189bc38ae2a7f56a145a0e1ab9d826713b6c5b

from Ice.Shared import AnalysisStatus

<<<<<<< HEAD
# david = Analysis()
# david1 = Analysis("analysis","analysisTest")
# david2 = Analysis.Create("analysis2","analysisTest2")
david = AnalysisStatus.Passed
# Access the properties
print(type(david))
# print(david1.Name,david1.Description)
# print(david2.Name,david2.Description)
# print(f"Description: {david.Description}")
# print(f"Numbers: {list(david.Numbers)}")
# print(f"Gender: {david.GetGender()}")
# print(type(david.Gender))


# print(f"Name: {david.Name}")
# print(f"Description: {david.Description}")
# print(f"Numbers: {list(david.Numbers)}")
# print(f"Gender: {david.GetGender()}")
# print(type(david.Gender))
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
=======
fullpath = "C:\\Users\\avivshi\\source\\repos\\pythonnetTest\\PythonNetTest\\davidObj.json"
file_path = "davidObj.json"

    
with open(fullpath, "r") as file:
    json_data = json.load(file)

json_string = json.dumps(json_data)

print(json_string)
david = Functions.DeserializeDavidFromJsonString(json_string)

# Access the properties
print(f"Name: {david.Name}")
print(f"Description: {david.Description}")
print(f"Numbers: {list(david.Numbers)}")
print(f"Gender: {david.GetGender()}")
print(f"Type of Gender: {type(david.Gender)}")
>>>>>>> b5189bc38ae2a7f56a145a0e1ab9d826713b6c5b


