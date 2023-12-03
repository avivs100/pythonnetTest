using System.Text.Json;
using davidProj;

var david = David.Create();
var jsonString = JsonSerializer.Serialize(david);
File.WriteAllText("C:\\Users\\AVIVSHI\\Desktop\\davidObj.json", jsonString);