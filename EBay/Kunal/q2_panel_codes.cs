static List<string> Solution(string panel, List<string> codes)
    {
        List<string> results = new List<string>();

        foreach (string code in codes)
        {
            for (int i = 1; i < code.Length; i++)
            {
                int index = int.Parse(code.Substring(0, i));
                string pattern = code.Substring(i);
                if (index >= 0 && index < panel.Length && panel.Substring(index, Math.Min(pattern.Length, panel.Length - index)) == pattern)
                {
                    results.Add(pattern);
                }
                else
                {
                    results.Add("not found");
                }
            }
        }

        return results;
    }