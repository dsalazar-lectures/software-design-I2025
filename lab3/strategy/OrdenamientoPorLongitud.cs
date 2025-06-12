/// <summary>
/// Clase que implementa el patrón Strategy para ordenar una lista de palabras por longitud.
/// </summary>
public class OrdenPorLongitud : IOrdenamiento
{
    /// <summary>
    /// Ordena una lista de palabras por su longitud.
    /// </summary>
    /// <param name="palabras"> Lista de palabras a ordenar.</param>
    /// <returns> Lista de palabras ordenadas por longitud.</returns>
    public List<string> Ordenar(List<string> palabras)
    {
        return palabras.OrderBy(p => p.Length).ToList();
    }
}