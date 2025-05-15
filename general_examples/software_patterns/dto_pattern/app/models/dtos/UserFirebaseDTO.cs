public class UserFirebaseDTO
{
    public string id { get; set; }
    public string name { get; set; }
    public string email { get; set; }
    public string role { get; set; }

    public static UserFirebaseDTO FromDomain(User user)
    {
        return new UserFirebaseDTO
        {
            id = user.Id,
            name = user.Name,
            email = user.Email,
            role = user.Role
        };
    }

    public User ToDomain()
    {
        return new User(id, name, email, role);
    }
}