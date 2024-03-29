using System;

class MyArray
{
    private int[] data;
    public MyArray(int size)
    {
        data = new int[size];
    }
    public void Add(int index, int val)
    {
        data[index] = val;
    }
    public void Update(int index, int val)
    {
        data[index] = val;
    }
    public void SortAsc()
    {
        Array.Sort(data);
    }
    public void SortDesc()
    {
        Array.Sort<int>(data, new Comparison<int>((i1, i2) => i2.CompareTo(i1)));
    }
    public void Reverse()
    {
        Array.Reverse(data);
    }
    public void PrintAll()
    {
        foreach (int num in data)
        {
            Console.WriteLine(num);
        }
    }
}