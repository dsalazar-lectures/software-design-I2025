using ObserverDemo.Controllers;

/// <summary>
/// Entry point for the Observer design pattern demonstration.
/// It simulates a temperature sensor that notifies multiple observers
/// when the temperature changes.
/// </summary>
class Program
{
    /// <summary>
    /// Main method that starts the application loop.
    /// It repeatedly asks the user to input a new temperature,
    /// which is then processed by the SensorController.
    /// </summary>
    static void Main()
    {
        var controller = new SensorController();

        while (true)
        {
            Console.Write("\nEnter a new temperature (or 'exit'): ");

            // Read user input
            string? input = Console.ReadLine();
            if (input is null) continue;

            // Exit condition
            if (input.ToLower() == "salir" || input.ToLower() == "exit") break;

            // Try to parse the input as a float and update temperature
            if (float.TryParse(input, out float temperature))
                controller.ChangeTemperature(temperature);
            else
                Console.WriteLine("Invalid input.");
        }
    }
}
