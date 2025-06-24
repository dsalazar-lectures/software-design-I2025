using ObserverDemo.Models;
using ObserverDemo.Models.Observers;

namespace ObserverDemo.Controllers;

/// <summary>
/// Controller for managing temperature sensor operations.
/// </summary>
/// <remarks>
/// This class initializes a temperature sensor and registers various observers (Display, Alarm, Logger)
/// to react to temperature changes. It implements the Observer design pattern to allow multiple
/// components to respond to temperature updates.
/// </remarks>
public class SensorController
{
    private readonly TemperatureSensor _sensor;

    public SensorController()
    {
        _sensor = new TemperatureSensor();
        _sensor.RegisterObserver(new Display());
        _sensor.RegisterObserver(new Alarm());
        _sensor.RegisterObserver(new Logger());
    }

    public void ChangeTemperature(float newTemp)
    
    {
        _sensor.SetTemperature(newTemp);
    }
}
