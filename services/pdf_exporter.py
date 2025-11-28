import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf_file(session):
    out_dir = "exports"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"quiz_{session.user_id}.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    y = height - 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, "Quiz Summary")
    y -= 20
    c.setFont("Helvetica", 11)
    c.drawString(40, y, f"Mode: {session.mode} | Total: {session.total}")
    y -= 20
    c.drawString(40, y, f"Attempted: {session.stats['attempted']} | Correct: {session.stats['correct']} | Wrong: {session.stats['wrong']} | Skipped: {session.stats['skipped']} | Saved: {session.stats['saved']}")
    y -= 30

    for q in session.questions[:20]:
        qd = q.to_dict()
        c.setFont("Helvetica-Bold", 11)
        c.drawString(40, y, f"Q{qd['serial']}: {qd['question']}")
        y -= 15
        c.setFont("Helvetica", 10)
        for label in ["A","B","C","D"]:
            c.drawString(50, y, f"{label}: {qd['options'][label]}")
            y -= 12
        c.drawString(50, y, f"Explanation: {qd['explanation']}")
        y -= 20
        if y < 80:
            c.showPage()
            y = height - 40

    c.save()
    return path
