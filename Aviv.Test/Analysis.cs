using Aviv.Test.functions;

namespace Aviv.Test
{
    public class Analysis
    {
        public Analysis()
        {
            
        }
        public Analysis(string name, string description)
        {
            Name = name;
            Description = description;
        }

        public string Name { get; set; }
        public string Description { get; set; }

        public bool Analyze(AnalysisInput ai)
        {
            return ai.Value < 10 && Description.Length < 10;
        }

        public static Analysis Create(string name, string description) => new() { Name = name, Description = description};
    }
}