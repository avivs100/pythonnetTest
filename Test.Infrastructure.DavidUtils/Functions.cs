using davidProj;
namespace Test.Infrastructure.DavidUtils;
using System.Text.Json;

public static class Functions
{
    public static David DeserializeDavidFromJsonString(string davidJson)
    {
        var david = JsonSerializer.Deserialize<David>(davidJson) ?? throw new Exception("error");
        return david;
    }

    //public static David DeserializeDavidFromJson(string path)
    //{
    //    var jsonContent = File.ReadAllText(path);
    //    var david = JsonConvert.DeserializeObject<David>(jsonContent) ?? throw new Exception("Could not map the JSON string to David object");
    //    return david;
    //}

    //public static T DeserializeJsonFile<T>(string filePath)
    //{
    //    try
    //    {

    //        var jsonContent = File.ReadAllText(filePath);


    //        T result = JsonConvert.DeserializeObject<T>(jsonContent);

    //        return result;
    //    }
    //    catch (Exception ex)
    //    {

    //        Console.WriteLine($"Error deserializing JSON file: {ex.Message}");
    //        return default(T);
    //    }
    //}

    //public static T DeserializeJsonString<T>(string objString)
    //{
    //    T result = JsonConvert.DeserializeObject<T>(objString) ?? throw new InvalidOperationException();
    //    return result;
    //}
}
