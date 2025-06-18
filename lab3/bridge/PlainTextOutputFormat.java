class PlainTextOutputFormat implements OutputFormat {
    public String formatTitle(String title) {
        return "==== " + title + " ====\n";
    }

    public String formatLine(String key, String value) {
        return key + ": " + value + "\n";
    }
}
