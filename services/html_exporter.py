import os
from jinja2 import Template

TEMPLATE = """
<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Quiz Export</title></head>
<body>
<h1>Quiz Summary</h1>
<p>Mode: {{ mode }}</p>
<p>Total: {{ total }}</p>
<p>Attempted: {{ stats.attempted }} | Correct: {{ stats.correct }} | Wrong: {{ stats.wrong }} | Skipped: {{ stats.skipped }} | Saved: {{ stats.saved }}</p>
<p>Config: {{ config }}</p>
<h2>Questions</h2>
<ol>
{% for q in questions %}
<li><strong>{{ q.question }}</strong>
<ul>
<li>A: {{ q.options.A }}</li>
<li>B: {{ q.options.B }}</li>
<li>C: {{ q.options.C }}</li>
<li>D: {{ q.options.D }}</li>
</ul>
<p>Explanation: {{ q.explanation }}</p>
</li>
{% endfor %}
</ol>
</body></html>
"""

def export_html_file(session):
    out_dir = "exports"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"quiz_{session.user_id}.html")
    html = Template(TEMPLATE).render(
        mode=session.mode,
        total=session.total,
        stats=session.stats,
        config=session.config,
        questions=[q.to_dict() for q in session.questions]
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path
