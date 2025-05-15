public class UserSqlDTO
{
    public string UserId { get; set; }
    public string FullName { get; set; }
    public string EmailAddress { get; set; }
    public string UserType { get; set; }

    public static UserSqlDTO FromDomain(User user)
    {
        return new UserSqlDTO
        {
            UserId = user.Id,
            FullName = user.Name,
            EmailAddress = user.Email,
            UserType = user.Role
        };
    }

    public User ToDomain()
    {
        return new User(UserId, FullName, EmailAddress, UserType);
    }
}