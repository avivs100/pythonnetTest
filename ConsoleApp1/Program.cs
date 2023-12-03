using System.Text.Json;
using davidProj;

var david = David.Create();
var jsonString = JsonSerializer.Serialize(david);
File.WriteAllText("C:\\Users\\AVIVSHI\\Desktop\\davidObj.json", jsonString);



//David davidObject = Functions.DeserializeDavidFromJson(filePath);
//David davidObject = DeserializeJsonFile<David>(filePath);


//Console.WriteLine("hii");
//Console.WriteLine(davidObject.Description + davidObject.Name + davidObject.Gender);
//foreach (var num in davidObject.Numbers)
//{
//    Console.WriteLine(num);
//}
//Console.WriteLine();