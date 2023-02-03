using System;
using System.Collections.Generic;

class MyDictionary
{
    private Dictionary<int, string> data;
    public MyDictionary()
    {
        data = new Dictionary<int, string>();
    }
    public void Add(int key, string value)
    {
        data.Add(key, value);
    }
    public void Update(int key, string value)
    {
        data[key] = value;
    }
    public void Remove(int key)
    {
        data.Remove(key);
    }
    public string GetValue(int key)
    {
        return data[key];
    }
    public void PrintAll()
    {
        foreach (string val in data.Values)
        {
            Console.WriteLine(val);
        }
    }
}