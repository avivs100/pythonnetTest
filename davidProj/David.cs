using System.Text.Json;


namespace davidProj;

public class David
{
    public string Name { get; set; }
    public string Description { get; set; }
    public List<double> Numbers { get; set; }
    public Gender Gender { get; set; }

    public David(string name, string description, IEnumerable<double> numbers, Gender gender)
    {
        Name = name;
        Description = description;
        Numbers = numbers.ToList();
        Gender = gender;
    }

    public David()
    {
    }

    public void AddNumber(double number)
    {
        Numbers.Add(number);
    }

    private double GetNumber(int index)
    {
        return Numbers[index];
    }

    public Gender GetGender() { return Gender; }

    public void SaveToJson(string filePath)
    {
        // Create a JSON representation of the David instance
        string json = JsonSerializer.Serialize(this);

        // Write the JSON to the specified file
        File.WriteAllText(filePath, json);
    }

    public static David create(/* string path*/)
    {
        //add here deserial logic and return the object
        return new David("david", "david1", new List<double> { 1.1, 2.2, 3.3, 4.4 }, Gender.Fluid);
    }
}