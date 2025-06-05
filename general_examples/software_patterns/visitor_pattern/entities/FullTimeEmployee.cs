public class FullTimeEmployee : IEmployee
{
    public string Name { get; }
    public double AnnualSalary { get; }

    public FullTimeEmployee(string name, double salary)
    {
        Name = name;
        AnnualSalary = salary;
    }

    public void Accept(IEmployeeVisitor visitor)
    {
        visitor.Visit(this);
    }
}