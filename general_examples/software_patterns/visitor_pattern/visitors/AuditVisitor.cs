public class AuditVisitor : IEmployeeVisitor
{
    public void Visit(FullTimeEmployee fullTime)
    {
        Console.WriteLine($"[AUDIT] {fullTime.Name}: Salario anual = ${fullTime.AnnualSalary}");
    }

    public void Visit(PartTimeEmployee partTime)
    {
        Console.WriteLine($"[AUDIT] {partTime.Name}: Horas trabajadas = {partTime.HoursWorked}");
    }

    public void Visit(Intern intern)
    {
        Console.WriteLine($"[AUDIT] {intern.Name}: Acceso limitado al sistema.");
    }
}