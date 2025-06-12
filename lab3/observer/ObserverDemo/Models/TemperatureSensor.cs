using System;
using System.Collections.Generic;

namespace ObserverDemo.Models
{
    /// <summary>
    /// Represents a temperature sensor that notifies observers when the temperature changes.
    /// Implements the <see cref="ISubject"/> interface as part of the Observer design pattern.
    /// </summary>
    public class TemperatureSensor : ISubject
    {
        /// <summary>
        /// The list of observers subscribed to this sensor.
        /// </summary>
        private readonly List<IObserver> _observers = new();

        /// <summary>
        /// The current temperature recorded by the sensor.
        /// </summary>
        private float _temperature;

        /// <summary>
        /// Sets a new temperature value and notifies all registered observers.
        /// </summary>
        /// <param name="temperature">The new temperature value in degrees Celsius.</param>
        public void SetTemperature(float temperature)
        {
            Console.WriteLine($"[Sensor] New temperature recorded: {temperature}°C");
            _temperature = temperature;
            NotifyObservers();
        }

        /// <summary>
        /// Registers an observer to receive updates from the sensor.
        /// </summary>
        /// <param name="observer">The observer to register.</param>
        public void RegisterObserver(IObserver observer) => _observers.Add(observer);

        /// <summary>
        /// Removes a previously registered observer.
        /// </summary>
        /// <param name="observer">The observer to remove.</param>
        public void RemoveObserver(IObserver observer) => _observers.Remove(observer);

        /// <summary>
        /// Notifies all registered observers of the current temperature.
        /// </summary>
        public void NotifyObservers()
        {
            foreach (var observer in _observers)
            {
                observer.Update(_temperature);
            }
        }
    }
}
