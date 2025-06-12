/// <summary>
/// Clase que implementa el patrón Strategy para ordenar una lista de palabras en orden alfabético ascendente.
/// </summary>
public class OrdenAlfabeticoAsc : IOrdenamiento
{
    /// <summary>
    /// Ordena una lista de palabras en orden alfabético ascendente.
    /// </summary>
    /// <param name="palabras"> Lista de palabras a ordenar.</param>
    /// <returns> Lista de palabras ordenadas en orden alfabético ascendente.</returns>
    public List<string> Ordenar(List<string> palabras)
    {
        return palabras.OrderBy(p => p).ToList();
    }
}