using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // Ejemplo de uso del patrón Strategy para ordenar una lista de palabras
        var palabras = new List<string> { "pera", "manzana", "kiwi", "banana", "uva" };
        // Crear una instancia de Ordenador que utilizará diferentes estrategias de ordenamiento
        var ordenador = new Ordenador();

        // Establecer la estrategia de ordenamiento por defecto (alfabético ascendente)
        Console.WriteLine("Orden alfabético ascendente:");
        ordenador.EstablecerEstrategia(new OrdenAlfabeticoAsc());
        ordenador.MostrarOrden(palabras);

        // Cambiar la estrategia a ordenamiento alfabético descendente
        Console.WriteLine("\nOrden alfabético descendente:");
        ordenador.EstablecerEstrategia(new OrdenAlfabeticoDesc());
        ordenador.MostrarOrden(palabras);

        // Cambiar la estrategia a ordenamiento por longitud
        Console.WriteLine("\nOrden por longitud:");
        ordenador.EstablecerEstrategia(new OrdenPorLongitud());
        ordenador.MostrarOrden(palabras);
    }
}
