import nbconvert, pathlib
def export(In, Out):
        pathlib.Path(Out).write_text(F"""---\n\n---\n
        {nbconvert.MarkdownExporter(exclude_input=True).from_filename(In)[0]}
        """);
if __name__=='__main__':
    export('ibis_posts/01.md.ipynb', '1.md')