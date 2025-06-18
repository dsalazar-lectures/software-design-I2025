abstract class Report {
    protected OutputFormat format;

    public Report(OutputFormat format) {
        this.format = format;
    }

    public abstract String generate();
}
