public class User
{
    public string Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Role { get; set; }

    public User(string id, string name, string email, string role)
    {
        Id = id;
        Name = name;
        Email = email;
        Role = role;
    }
}
