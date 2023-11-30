import clr
clr.AddReference("Test.Infrastructure.DavidUtils")
clr.AddReference("davidProj")
clr.AddReference("System")
import json
from Test.Infrastructure.DavidUtils import Functions
from davidProj import David


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


