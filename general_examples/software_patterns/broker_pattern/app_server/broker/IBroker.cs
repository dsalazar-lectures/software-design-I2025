using System;

public interface IBroker
{
    string SendRequest(string message);
}