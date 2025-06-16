/// <summary>
/// Clase que implementa el patrón Strategy para ordenar una lista de palabras en orden alfabético descendente.
/// </summary>
public class OrdenAlfabeticoDesc : IOrdenamiento
{
    /// <summary>
    /// Ordena una lista de palabras en orden alfabético descendente.
    /// </summary>
    /// <param name="palabras"> Lista de palabras a ordenar.</param>
    /// <returns> Lista de palabras ordenadas en orden alfabético descendente.</returns>
    public List<string> Ordenar(List<string> palabras)
    {
        return palabras.OrderByDescending(p => p).ToList();
    }
}