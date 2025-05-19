public class Client
{
    private readonly IBroker _broker;

    public Client(IBroker broker)
    {
        _broker = broker;
    }

    public void MakeRequest(string message)
    {
        Console.WriteLine("[Cliente] Enviando solicitud al broker...");
        string result = _broker.SendRequest(message);
        Console.WriteLine($"[Cliente] Recibió respuesta: {result}");
    }
}