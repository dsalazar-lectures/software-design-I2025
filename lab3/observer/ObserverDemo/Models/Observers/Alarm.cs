namespace ObserverDemo.Models.Observers;

/// <summary>
/// Represents an alarm that monitors temperature changes.
/// This class implements the IObserver interface to receive temperature updates.
/// </summary>
/// <remarks>
/// When the temperature exceeds 30 degrees, the alarm triggers and outputs a warning message.
/// </remarks>
public class Alarm : IObserver
{    public void Update(float temperature)
    {
        if (temperature > 30)
            Console.WriteLine("[Alarm] High temperature detected!");
    }
}