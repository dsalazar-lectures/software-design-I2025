package src;

public class UserReport extends Report {
    private String name;
    private String email;

    public UserReport(OutputFormat format, String name, String email) {
        super(format);
        this.name = name;
        this.email = email;
    }

    public String generate() {
        StringBuilder sb = new StringBuilder();
        sb.append(format.formatTitle("Reporte de Usuario"));
        sb.append(format.formatLine("Nombre", name));
        sb.append(format.formatLine("Email", email));
        return sb.toString();
    }
}
