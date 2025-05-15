using System.Collections.Generic;
using System.Linq;

public class UserService
{
    private readonly IRepository<User> _repository;

    public UserService(IRepository<User> repository)
    {
        _repository = repository;
    }

    public bool CreateUser(User user)
    {
        return _repository.Add(user);
    }

    public bool DeleteUser(string id)
    {
        return _repository.Delete(id);
    }

    public User GetUser(string id)
    {
        return _repository.Get(id);
    }
}
