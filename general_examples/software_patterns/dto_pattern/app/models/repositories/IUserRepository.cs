public interface IRepository<T>
{
    bool Add(T item);
    bool Delete(string id);
    T Get(string id);
}