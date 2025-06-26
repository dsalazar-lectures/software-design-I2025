package src;

public class HTMLOutputFormat implements OutputFormat {
    public String formatTitle(String title) {
        return "<h1>" + title + "</h1>\n";
    }

    public String formatLine(String key, String value) {
        return "<p><strong>" + key + ":</strong> " + value + "</p>\n";
    }
}
