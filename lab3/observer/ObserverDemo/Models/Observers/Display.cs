namespace ObserverDemo.Models.Observers;

/// <summary>
/// Represents a display observer that shows temperature updates.
/// </summary>
/// <remarks>
/// This class implements the IObserver interface to receive and display temperature updates
/// from a weather station or similar subject.
/// </remarks>
public class Display : IObserver
{
    public void Update(float temperature)
    {
        Console.WriteLine($"[Display] Temperatura actual: {temperature}°C");
    }
}