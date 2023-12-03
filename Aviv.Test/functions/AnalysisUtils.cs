using System.Text.Json;
using davidProj;

namespace Aviv.Test.functions;

public static class AnalysisUtils
{
    public static David DeserializeDavidFromJsonString(string jsonString)
    {
        return JsonSerializer.Deserialize<David>(jsonString) ?? David.Create();
    }
}