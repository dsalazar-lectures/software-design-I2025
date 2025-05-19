public class Program
{
    public static void Main()
    {
        Server server = new Server();
        IBroker broker = new ConcreteBroker(server);
        Client client = new Client(broker);

        client.MakeRequest("Dame el estado del sistema");
    }
}