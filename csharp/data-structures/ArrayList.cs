using System;
using System.Collections;

class MyArrayList
{
    private ArrayList data;
    public MyArrayList()
    {
        data = new ArrayList();
    }
    public void Add(int val)
    {
        data.Add(val);
    }
    public void Update(int index, int val)
    {
        data[index] = val;
    }
    public void SortAsc()
    {
        data.Sort();
    }
    public void Reverse()
    {
        data.Reverse();
    }
    public void PrintAll()
    {
        foreach (int num in data)
        {
            Console.WriteLine(num);
        }
    }
}