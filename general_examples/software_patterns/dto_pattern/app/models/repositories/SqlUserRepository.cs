public class SqlUserRepository : IRepository<User>
{
    private Dictionary<string, UserSqlDTO> _database = new Dictionary<string, UserSqlDTO>();

    public bool Add(User user)
    {
        var dto = UserSqlDTO.FromDomain(user);
        _database[user.Id] = dto;
        Console.WriteLine($"User {user.Name} added to SQL database.");
        return true;
    }

    public bool Delete(string id)
    {
        Console.WriteLine($"User with ID {id} deleted from SQL database.");
        return _database.Remove(id);
    }

    public User Get(string id)
    {
        if (_database.TryGetValue(id, out var dto))
        {
            Console.WriteLine($"User with ID {id} retrieved from SQL database.");
            return dto.ToDomain();
        }
        Console.WriteLine($"User with ID {id} not found in SQL database.");
        return null;
    }
}