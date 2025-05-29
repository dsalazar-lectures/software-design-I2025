/// <summary>
/// Clase Ordenador que utiliza el patrón Strategy para ordenar una lista de palabras.
/// </summary>
public class Ordenador
{
    /// <summary>
    /// Estrategia de ordenamiento actual.
    /// </summary>
    private IOrdenamiento _estrategia;

    /// <summary>
    /// Constructor de la clase Ordenador que establece una estrategia por defecto.
    /// </summary>
    /// <param name="estrategia"> Estrategia de ordenamiento a utilizar.</param>
    public void EstablecerEstrategia(IOrdenamiento estrategia)
    {
        _estrategia = estrategia;
    }

    /// <summary>
    /// Muestra el resultado del ordenamiento de una lista de palabras utilizando la estrategia actual.
    /// </summary>
    /// <param name="palabras"> Lista de palabras a ordenar.</param>
    public void MostrarOrden(List<string> palabras)
    {
        var resultado = _estrategia.Ordenar(palabras);
        Console.WriteLine(string.Join(", ", resultado));
    }
}