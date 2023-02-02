using System;
using System.Collections;

class MyStack
{
    public MyStack()
    {
        Stack myStack = new Stack();

        myStack.Push("1");
        myStack.Push("2");
        myStack.Push('3');

        foreach (var elem in myStack)
        {
            Console.WriteLine(elem);
        }
    }
}