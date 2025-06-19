package testing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import src.OutputFormat;
import src.PlainTextOutputFormat;
import src.Report;
import src.UserReport;


public class UserReportTest {

    @Test
    public void testUserReportPlainText() {
        OutputFormat format = new PlainTextOutputFormat();
        Report report = new UserReport(format, "Ana", "ana@email.com");

        String output = report.generate();
        assertTrue(output.contains("Nombre: Ana"));
    }
}
