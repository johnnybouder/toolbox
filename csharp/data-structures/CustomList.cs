class CustomObject
{
    public int Key { get; set; }
    public string Val { get; set; }
    public CustomObject(int key, string val)
    {
        Key = key;
        Val = val;
    }
}

class MyCustomList
{
    public List<CustomObject> list { get; set; }
    public MyCustomList(List<CustomObject> list)
    {
        this.list = list;
    }
    public void SortObjectsAsc()
    {
        list.Sort((x, y) => x.Key.CompareTo(y.Key));
    }
    public void SortObjectsDesc()
    {
        list.Sort((y, x) => x.Key.CompareTo(y.Key));
    }
    public void PrintAll()
    {
        foreach (CustomObject obj in list)
        {
            Console.WriteLine(obj.Val);
        }
    }
}