namespace ObserverDemo.Models;

/// <summary>
/// Defines the methods that a subject in the Observer pattern must implement.
/// A subject is an object that maintains a list of observers and notifies them
/// of state changes.
/// </summary>
public interface ISubject
{
    void RegisterObserver(IObserver observer);
    void RemoveObserver(IObserver observer);
    void NotifyObservers();
}