public class BonusCalculatorVisitor : IEmployeeVisitor
{
    public void Visit(FullTimeEmployee fullTime)
    {
        double bonus = fullTime.AnnualSalary * 0.1;
        Console.WriteLine($"[BONUS] {fullTime.Name}: ${bonus} (10% de salario)");
    }

    public void Visit(PartTimeEmployee partTime)
    {
        double bonus = partTime.HoursWorked * partTime.HourlyRate * 0.05;
        Console.WriteLine($"[BONUS] {partTime.Name}: ${bonus} (5% de ingreso estimado)");
    }

    public void Visit(Intern intern)
    {
        Console.WriteLine($"[BONUS] {intern.Name}: $0 (los pasantes no reciben bono)");
    }
}