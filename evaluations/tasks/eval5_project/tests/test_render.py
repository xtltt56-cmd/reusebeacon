"""Visible tests for markdown rendering (do not modify).

Expected HTML taken verbatim from the CommonMark 0.31.2 spec examples.
"""
from markdown_render import render_markdown


def test_plain_paragraph():
    assert render_markdown("hello world\n") == "<p>hello world</p>\n"


def test_atx_heading():
    assert render_markdown("# foo\n") == "<h1>foo</h1>\n"


def test_strong_emphasis():
    assert render_markdown("**foo**\n") == "<p><strong>foo</strong></p>\n"


def test_code_span():
    assert render_markdown("`foo`") == "<p><code>foo</code></p>\n"


def test_two_paragraphs():
    assert render_markdown("aaa\n\nbbb\n") == "<p>aaa</p>\n<p>bbb</p>\n"
