using System;
using System.Collections;

class MyQueue
{
    public MyQueue()
    {
        Queue myQueue = new Queue();

        myQueue.Enqueue("1");
        myQueue.Enqueue("2");
        myQueue.Enqueue('3');

        foreach (var elem in myQueue)
        {
            Console.WriteLine(elem);
        }
    }
}