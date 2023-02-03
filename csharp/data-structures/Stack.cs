using System;
using System.Collections;

class MyStack
{
    private Stack stack;
    public MyStack()
    {
        stack = new Stack();
    }
    public void Add(string val)
    {
        stack.Push(val);
    }
    public void Remove()
    {
        stack.Pop();
    }
    public void Clear()
    {
        stack.Clear();
    }
    public void PrintAll()
    {
        foreach (var elem in stack)
        {
            Console.WriteLine(elem);
        }
    }
}