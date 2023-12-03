from pythonnet import load
load("coreclr")
import clr
import json

clr.AddReference("Aviv.Test")
clr.AddReference("davidProj")
clr.AddReference("System.Memory")


from Aviv.Test.functions import AnalysisUtils


fullpath = "C:\\Users\\avivshi\\source\\repos\\pythonnetTest\\PythonNetTest\\davidObj.json"
file_path = "davidObj.json"

    
with open(fullpath, "r") as file:
    json_data = json.load(file)

json_string = json.dumps(json_data)

print(json_string)

david = AnalysisUtils.DeserializeDavidFromJsonString(json_string)
# Access the properties
# print(f"Name: {david.Name}")
# print(f"Description: {david.Description}")
# print(f"Numbers: {list(david.Numbers)}")
# print(f"Gender: {david.GetGender()}")
# print(f"Type of Gender: {type(david.Gender)}")
print(david.GetNumber(2))
print(list(david.Numbers))


