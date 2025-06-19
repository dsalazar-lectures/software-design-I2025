package testing;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import src.OutputFormat;          // Importá la interfaz
import src.HTMLOutputFormat;     // Importá la clase que implementa la interfaz

public class HTMLOutputFormatTest {

    @Test
    public void testHTMLOutputFormat() {
        OutputFormat format = new HTMLOutputFormat();
        String title = format.formatTitle("Mi Título");
        assertEquals("<h1>Mi Título</h1>\n", title);
    }
}
