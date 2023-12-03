

using System.Text.Json;


<<<<<<< HEAD
using Newtonsoft.Json;

Console.WriteLine("hii");
string filePath = "D:\\PythonNetTest\\davidObj.json";
var davidObject = DeserializeJsonFile<David>(filePath);
=======
>>>>>>> b5189bc38ae2a7f56a145a0e1ab9d826713b6c5b


//David davidObject = Functions.DeserializeDavidFromJson(filePath);
//David davidObject = DeserializeJsonFile<David>(filePath);


//Console.WriteLine("hii");
//Console.WriteLine(davidObject.Description + davidObject.Name + davidObject.Gender);
//foreach (var num in davidObject.Numbers)
//{
//    Console.WriteLine(num);
//}
//Console.WriteLine();

static T DeserializeJsonFile<T>(string filePath)
{
    try
    {

        var jsonContent = File.ReadAllText(filePath);


        T result = JsonSerializer.Deserialize<T>(jsonContent);

        return result;
    }
    catch (Exception ex)
    {

        Console.WriteLine($"Error deserializing JSON file: {ex.Message}");
        return default(T);
    }
}