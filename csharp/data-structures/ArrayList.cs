using System;
using System.Collections;

class MyArrayList
{
    private ArrayList data;
    public MyArrayList(ArrayList list)
    {
        data = list;
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