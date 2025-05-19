public class ConcreteBroker : IBroker
{
    private readonly Server _server;

    public ConcreteBroker(Server server)
    {
        _server = server;
    }

    public string SendRequest(string message)
    {
        Console.WriteLine("[Broker] Recibió solicitud del cliente...");
        var response = _server.ProcessRequest(message);
        Console.WriteLine("[Broker] Respuesta recibida del servidor.");
        return response;
    }
}