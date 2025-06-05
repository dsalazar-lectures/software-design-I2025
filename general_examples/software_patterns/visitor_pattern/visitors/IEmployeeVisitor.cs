public interface IEmployeeVisitor
{
    void Visit(FullTimeEmployee fullTime);
    void Visit(PartTimeEmployee partTime);
    void Visit(Intern intern);
}
