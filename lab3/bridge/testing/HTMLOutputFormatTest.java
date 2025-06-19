package testing;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import src.OutputFormat;
import src.HTMLOutputFormat;

public class HTMLOutputFormatTest {

    @Test
    public void testHTMLOutputFormat() {
        OutputFormat format = new HTMLOutputFormat();
        String title = format.formatTitle("Mi Título");
        assertEquals("<h1>Mi Título</h1>\n", title);
    }
}
