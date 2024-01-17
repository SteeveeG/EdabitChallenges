namespace DartsSolving
{
    public class DartsSolver
    {
        private List<string> resultList = new();
        public string[] TestDartsSolver(int[] sections, int darts, int target)
        {
            resultList.Clear();
            var combinations = GetCombination(sections.ToList(), darts);
            foreach (var combination in combinations)
            {
                combination.Sort();
                var result = combination.Sum();
                if (result != target)
                {
                    continue;
                }

                var resultCombination = "";
                for (var i = 0; i < darts; i++)
                {
                    resultCombination += combination[i];
                    if (i + 1 < darts)
                    {
                        resultCombination += "-";
                    }
                }
                resultList.Add(resultCombination);
            }
            return resultList.ToArray();
        }
    
        private List<List<int>> GetCombination(List<int> list, int k)
        {
            var result = new List<List<int>>();
            GetCombination(list, new List<int>(), k, result);
            return result; 
        }

        private void GetCombination(List<int> list, List<int> data, int k, List<List<int>> result)
        {
            if (data.Count == k)
            {
                result.Add(new List<int>(data));
                return;
            }

            foreach (var listItem in list)
            {
                if (data.Count > 0 && listItem > data[data.Count - 1])  
                {
                    continue;
                }
                data.Add(listItem);
                GetCombination(list, data, k, result);  
                data.RemoveAt(data.Count - 1);
            }
        }

    }
}