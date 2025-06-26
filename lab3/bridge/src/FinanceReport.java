package src;

public class FinanceReport extends Report {
    private double ingresos;
    private double egresos;

    public FinanceReport(OutputFormat format, double ingresos, double egresos) {
        super(format);
        this.ingresos = ingresos;
        this.egresos = egresos;
    }

    public String generate() {
        StringBuilder sb = new StringBuilder();
        sb.append(format.formatTitle("Reporte Financiero"));
        sb.append(format.formatLine("Ingresos", String.format("$%.2f", ingresos)));
        sb.append(format.formatLine("Egresos", String.format("$%.2f", egresos)));
        sb.append(format.formatLine("Balance", String.format("$%.2f", ingresos - egresos)));
        return sb.toString();
    }
}
