namespace Aviv.Test.functions;

public class AnalysisInput
{
    public int Index { get; set; }
    public double Value { get; set; }

    public int GetIndex() { return Index; }

    public double Increment()
    {
        return ++Value;
    }

    public static AnalysisInput Create(int index, double value) => new() { Index = index, Value = value };
}