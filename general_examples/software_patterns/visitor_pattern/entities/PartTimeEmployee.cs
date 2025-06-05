public class PartTimeEmployee : IEmployee
{
    public string Name { get; }
    public double HourlyRate { get; }
    public int HoursWorked { get; }

    public PartTimeEmployee(string name, double hourlyRate, int hoursWorked)
    {
        Name = name;
        HourlyRate = hourlyRate;
        HoursWorked = hoursWorked;
    }

    public void Accept(IEmployeeVisitor visitor)
    {
        visitor.Visit(this);
    }
}