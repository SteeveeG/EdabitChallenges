using System.Data;

namespace MiserableParodyOfACalculator;

public class Calculator
{
    public double Calculate(string str)
    {
        DataTable dataTable = new DataTable();
        var result = dataTable.Compute(str, "");
        return Convert.ToDouble(result);
    }
}


