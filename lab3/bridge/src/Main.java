package src;

public class Main {
    public static void main(String[] args) {
        OutputFormat plain_text = new PlainTextOutputFormat();
        OutputFormat html = new HTMLOutputFormat();

        Report user_plain_report = new UserReport(plain_text, "Ana", "ana@email.com");
        Report user_html_report = new UserReport(html, "Ana", "ana@email.com");

        System.out.println("=== Reporte Usuario Texto Plano ===");
        System.out.println(user_plain_report.generate());

        System.out.println("=== Reporte Usuario HTML ===");
        System.out.println(user_html_report.generate());


	Report finance_plain_report = new FinanceReport(plain_text, 10000.0, 4500.0);
	Report finance_html_report = new FinanceReport(html, 10000.0, 4500.0);

	System.out.println("=== Reporte Financiero Texto Plano ===");
	System.out.println(finance_plain_report.generate());

	System.out.println("=== Reporte Financiero HTML ===");
	System.out.println(finance_html_report.generate());


    }
}
