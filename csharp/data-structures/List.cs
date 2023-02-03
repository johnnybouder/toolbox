using System;
using System.Collections.Generic;

class MyList
{
    private List<int> data;
    public MyList()
    {
        data = new List<int>();
    }
    public void SortAsc()
    {
        data.Sort();
    }
    public void SortDesc()
    {
        data.Sort(new Comparison<int>((i1, i2) => i2.CompareTo(i1)));
    }
    public void Reverse()
    {
        data.Reverse();
    }
    public int GetFirst()
    {
        return data[0];
    }
    public int GetLast()
    {
        return data[data.Count - 1];
    }
    public void AddToStart(int val)
    {
        data.Insert(0, val);
    }
    public void Add(int val)
    {
        data.Add(val);
    }
    public void RemoveFirst()
    {
        data.RemoveAt(0);
    }
    public void Remove()
    {
        data.RemoveAt(data.Count - 1);
    }
    public void PrintAll()
    {
        foreach (int num in data)
        {
            Console.WriteLine(num);
        }
    }
}