public class Server
{
    public string ProcessRequest(string message)
    {
        return $"[Server] Procesando: {message}";
    }
}