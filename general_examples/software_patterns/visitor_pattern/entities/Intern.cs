public class Intern : IEmployee
{
    public string Name { get; }

    public Intern(string name)
    {
        Name = name;
    }

    public void Accept(IEmployeeVisitor visitor)
    {
        visitor.Visit(this);
    }
}