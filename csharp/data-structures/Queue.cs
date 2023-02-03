using System;
using System.Collections;

class MyQueue
{
    private Queue queue;
    public MyQueue()
    {
        queue = new Queue();
    }
    public void Add(string val)
    {
        queue.Enqueue(val);
    }
    public void Remove()
    {
        queue.Dequeue();
    }
    public void Clear()
    {
        queue.Clear();
    }
    public void PrintAll()
    {
        foreach (var elem in queue)
        {
            Console.WriteLine(elem);
        }
    }
}