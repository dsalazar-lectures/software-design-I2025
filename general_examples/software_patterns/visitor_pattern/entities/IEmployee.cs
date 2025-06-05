public interface IEmployee
{
    void Accept(IEmployeeVisitor visitor);
    string Name { get; }
}