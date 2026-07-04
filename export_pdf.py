import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ==========================
# Font
# ==========================

font_path = os.path.join("fonts", "arial.ttf")

if os.path.exists(font_path):

    pdfmetrics.registerFont(
        TTFont("Arial", font_path)
    )

    FONT_NAME = "Arial"

else:

    FONT_NAME = "Helvetica"

styles = getSampleStyleSheet()

styles["Title"].fontName = FONT_NAME
styles["BodyText"].fontName = FONT_NAME


# ==========================
# Export PDF
# ==========================

def export_history_to_pdf(history, filename):

    doc = SimpleDocTemplate(filename)

    elements = []

    elements.append(
        Paragraph(
            "LỊCH SỬ HỘI THOẠI",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    for item in history:

        question = item[1].replace("\n", "<br/>")

        answer = item[2].replace("\n", "<br/>")

        elements.append(
            Paragraph(
                f"<b>Câu hỏi:</b><br/>{question}",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 8)
        )

        elements.append(
            Paragraph(
                f"<b>Trả lời:</b><br/>{answer}",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 8)
        )

        elements.append(
            Paragraph(
                f"<b>Thời gian:</b> {item[3]}",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 25)
        )

    doc.build(elements)