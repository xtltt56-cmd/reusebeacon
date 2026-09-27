# External grader audit notes

## T5 task/grader conflict found at N rep1

The frozen task says the output should be an HTML string ending in a newline. The frozen external grader asserts `render_markdown("") == ""`, and official CommonMark example 207 also expects the empty string. N rep1 returned `"\n"` and therefore failed both assertions. This is a task/grader conflict, not clear evidence of a model defect. Keep the grader and results unchanged; report raw results and a separately labeled interpretation excluding this conflict.

N rep1 also differs from CommonMark examples 218, 239 and 240 only in its serialization of an empty blockquote (`<blockquote></blockquote>` versus `<blockquote>\n</blockquote>`). The official corpus compares exact HTML text, so these remain raw test failures. Assess whether they affect the stated goal separately.

T5 rep2 N self-reported 649/652 official examples and only three blockquote differences. The independent grader observed four official example failures, including example 207, because the project function adds a newline to an empty result. Report the independent result (648/652); mark the agent's self-reported count inaccurate.
