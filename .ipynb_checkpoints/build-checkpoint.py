import nbconvert, pathlib, yaml
def export(In, Out, **globals):
        pathlib.Path(Out).write_text(F"""---\n{yaml.safe_dump(globals)}\n---\n
        {nbconvert.MarkdownExporter(exclude_input=True).from_filename(In)[0]}
        """);
if __name__=='__main__':
    export('ibis_posts/01.md.ipynb', 'docs/1.md', permalink="/expressions/")