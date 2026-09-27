"""Markdown rendering for CMS notes. Currently minimal: plain paragraphs only."""
import html


def render_markdown(source: str) -> str:
    """Render CommonMark source to HTML.

    Current implementation escapes and wraps non-empty lines as paragraphs.
    TODO: full CommonMark 0.31.2 compliance (see README acceptance criteria).
    """
    out = []
    for line in source.splitlines():
        if line.strip():
            out.append(f"<p>{html.escape(line.strip())}</p>")
    return "\n".join(out) + ("\n" if out else "")
