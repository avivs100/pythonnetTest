// See https://aka.ms/new-console-template for more information

using davidProj;


using Newtonsoft.Json;

Console.WriteLine("hii");
string filePath = "D:\\PythonNetTest\\davidObj.json";
David davidObject = DeserializeJsonFile<David>(filePath);


Console.WriteLine("hii");
Console.WriteLine(davidObject.Description + davidObject.Name + davidObject.Gender);
foreach (var num in davidObject.Numbers)
{
    Console.WriteLine(num);
}
Console.WriteLine();

static T DeserializeJsonFile<T>(string filePath)
{
    try
    {

        var jsonContent = File.ReadAllText(filePath);


        T result = JsonConvert.DeserializeObject<T>(jsonContent);

        return result;
    }
    catch (Exception ex)
    {

        Console.WriteLine($"Error deserializing JSON file: {ex.Message}");
        return default(T);
    }
}

