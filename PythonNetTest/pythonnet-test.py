from pythonnet import load
load("coreclr")
import clr
import json

clr.AddReference("Ice.Shared")
clr.AddReference("Ice.Domain")

from Ice.Domain.Analyses.Functions import AnalysisInput


fullpath = "C:\\Users\\avivshi\\Desktop\\PythonNetTest\\ShotAnalysisInput1phase1runb19c.json"

    
with open(fullpath, "r") as file:
    json_data = json.load(file)

json_string = json.dumps(json_data)

# print(json_string)

# david = AnalysisInput.DeserializeFromJsonString(json_string)

print(AnalysisInput.Parameters)


