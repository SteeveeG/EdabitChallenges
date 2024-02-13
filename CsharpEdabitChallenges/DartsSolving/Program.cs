using DartsSolving;
//Link To Challenge: https://edabit.com/challenge/5K28RRq4RZQB7r9tj

Console.WriteLine("DartsSolver:");
var dartSolver = new DartsSolver();
var results = new List<string[]>();

results.Add(dartSolver.TestDartsSolver(new[] { 3, 6, 8, 11, 15, 19, 22 }, 3, 35));
results.Add(dartSolver.TestDartsSolver(new[] { 2, 4, 7, 10, 13, 18, 24 }, 3, 29));
results.Add(dartSolver.TestDartsSolver(new[] { 3, 7, 11, 14, 18, 20, 25 }, 3, 40));
results.Add(dartSolver.TestDartsSolver(new[] { 3, 7, 11, 14, 18, 20, 25 }, 3, 8));
results.Add(dartSolver.TestDartsSolver(new[] { 3, 7, 11, 14, 18, 20, 25 }, 3, 32));
results.Add(dartSolver.TestDartsSolver(new[] { 3, 7, 11, 14, 18, 20, 25, 29, 34 }, 3, 67));
results.Add(dartSolver.TestDartsSolver(new[] { 3, 7, 11, 14, 18, 20, 25 }, 4, 23));

foreach (var result in results)
{
    foreach (var re in result)
    {
        Console.Write(re + " ");
    }
    Console.WriteLine("");
}
Console.ReadKey();