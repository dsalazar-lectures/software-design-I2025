public class FirebaseUserRepository : IRepository<User>
{
    private Dictionary<string, UserFirebaseDTO> _database = new Dictionary<string, UserFirebaseDTO>();

    public bool Add(User user)
    {
        var dto = UserFirebaseDTO.FromDomain(user);
        _database[user.Id] = dto;
        Console.WriteLine($"User {user.Name} added to Firebase.");
        return true;
    }

    public bool Delete(string id)
    {
        Console.WriteLine($"User with ID {id} deleted from Firebase.");
        return _database.Remove(id);
    }

    public User Get(string id)
    {
        if (_database.TryGetValue(id, out var dto))
        {
            Console.WriteLine($"User with ID {id} retrieved from Firebase.");
            return dto.ToDomain();
        }
        Console.WriteLine($"User with ID {id} not found in Firebase.");
        return null;
    }
}