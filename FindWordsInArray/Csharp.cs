using System;
using System.Collections.Generic;

public class Solution
{
    public IList<int> FindWordsContaining(string[] words, char x)
    {
        List<int> result = new List<int>();
        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].Contains(x))
            {
                result.Add(i);
            }
        }
        return result;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Solution solution = new Solution();
        string[] words = { "hello", "world", "example", "test" };
        char x = 'e';
        IList<int> indices = solution.FindWordsContaining(words, x);

        foreach (int index in indices)
        {
            Console.WriteLine(index);
        }
    }
}