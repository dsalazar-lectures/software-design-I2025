/// <summary>
/// Clase que implementa el patr�n Strategy para ordenar una lista de palabras en orden alfab�tico ascendente.
/// </summary>
public class OrdenAlfabeticoAsc : IOrdenamiento
{
    /// <summary>
    /// Ordena una lista de palabras en orden alfab�tico ascendente.
    /// </summary>
    /// <param name="palabras"> Lista de palabras a ordenar.</param>
    /// <returns> Lista de palabras ordenadas en orden alfab�tico ascendente.</returns>
    public List<string> Ordenar(List<string> palabras)
    {
        return palabras.OrderBy(p => p).ToList();
    }
}