namespace ObserverDemo.Models;

/// <summary>
/// Defines a standard interface for objects that should be notified of changes in an observable subject.
/// </summary>
/// <remarks>
/// This interface is part of the Observer design pattern, where observers register with a subject
/// and receive updates when the subject's state changes.
/// </remarks>
public interface IObserver
{
    void Update(float temperature);
}