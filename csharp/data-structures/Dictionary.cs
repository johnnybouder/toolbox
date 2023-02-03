using System;
using System.Collections.Generic;

class MyDictionary
{
    private Dictionary<int, string> data;
    public MyDictionary(Dictionary<int, string> list)
    {
        data = list;
    }
    public string GetValue(int key)
    {
        return data[key];
    }
    public void Add(int key, string value)
    {
        data.Add(key, value);
    }
    public void Remove(int key)
    {
        data.Remove(key);
    }
    public void PrintAll()
    {
        foreach (string val in data.Values)
        {
            Console.WriteLine(val);
        }
    }
}