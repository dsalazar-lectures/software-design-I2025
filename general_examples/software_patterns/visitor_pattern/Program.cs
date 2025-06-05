public class Program
{
    public static void Main(string[] args)
    {
        List<IEmployee> employees = new List<IEmployee>
        {
            new FullTimeEmployee("Laura", 60000),
            new PartTimeEmployee("Carlos", 20, 100),
            new Intern("Sofía")
        };

        Console.WriteLine("== Calculo de Bonos ==");
        var bonusVisitor = new BonusCalculatorVisitor();
        foreach (var emp in employees)
        {
            emp.Accept(bonusVisitor);
        }

        Console.WriteLine("\n== Auditoría ==");
        var auditVisitor = new AuditVisitor();
        foreach (var emp in employees)
        {
            emp.Accept(auditVisitor);
        }
    }
}