using System;

class Program
{
    static void Main(string[] args)
    {
        // Firebase Example
        var firebaseRepo = new FirebaseUserRepository();
        var firebaseService = new UserService(firebaseRepo);

        var user1 = new User("1", "John Doe", "john@example.com", "Admin");
        firebaseService.CreateUser(user1);

        // SQL Example
        var sqlRepo = new SqlUserRepository();
        var sqlService = new UserService(sqlRepo);

        var user2 = new User("2", "Jane Smith", "jane@example.com", "User");
        sqlService.CreateUser(user2);
    }
}