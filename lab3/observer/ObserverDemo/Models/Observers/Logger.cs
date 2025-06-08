namespace ObserverDemo.Models.Observers;

/// <summary>
/// Represents a logger that observes temperature changes and outputs them to the console.
/// </summary>
/// <remarks>
/// This class implements the IObserver interface to receive temperature updates
/// from a subject it is subscribed to.
/// </remarks>
public class Logger : IObserver
{    public void Update(float temperature)
    {
        Console.WriteLine($"[Logger] Temperature recorded: {temperature}°C");
    }
}
