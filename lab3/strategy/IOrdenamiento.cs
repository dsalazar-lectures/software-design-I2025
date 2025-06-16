/// <summary>
/// Interfaz IOrdenamiento que define el método para ordenar una lista de palabras.
/// </summary>
public interface IOrdenamiento
{
    /// <summary>
    /// Lista de palabras a ordenar.
    /// </summary>
    /// <param name="palabras"> Lista de palabras a ordenar.</param>
    /// <returns> Lista de palabras ordenadas.</returns>
    List<string> Ordenar(List<string> palabras);
}