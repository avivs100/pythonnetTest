import clr

clr.AddReference("Aviv.Test")
clr.AddReference("Ice.Domain")
clr.AddReference("Ice.Shared")

from Ice.Shared import AnalysisStatus

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







# gender = Gender.Male
# numbers_list = [1.2, 1, 2.5, 8.5]

# # Convert the Python list to a .NET array
# numbers_array = Array[float](numbers_list)

# david = David("david1", "davidTest", numbers_array, gender)
# print(list(david.numbers))