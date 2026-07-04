import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ==========================
# Đăng ký font
# ==========================

FONT_NAME = "Helvetica"

font_path = os.path.join("font", "NotoSans-Regular.ttf")

if os.path.exists(font_path):
    try:
        pdfmetrics.registerFont(
            TTFont("NotoSans", font_path)
        )
        FONT_NAME = "NotoSans"
    except Exception as e:
        print(e)

# ==========================
# Styles
# ==========================

title_style = ParagraphStyle(
    "Title",
    fontName=FONT_NAME,
    fontSize=22,
    alignment=TA_CENTER,
    spaceAfter=20,
    leading=28
)

heading_style = ParagraphStyle(
    "Heading",
    fontName=FONT_NAME,
    fontSize=13,
    spaceBefore=10,
    spaceAfter=6,
    leading=18
)

body_style = ParagraphStyle(
    "Body",
    fontName=FONT_NAME,
    fontSize=11,
    leading=18
)

# ==========================
# Export PDF
# ==========================

def export_history_to_pdf(history, filename):

    doc = SimpleDocTemplate(filename)

    elements = []

    elements.append(
        Paragraph(
            "LỊCH SỬ HỘI THOẠI",
            title_style
        )
    )

    if len(history) == 0:

        elements.append(
            Paragraph(
                "Chưa có dữ liệu.",
                body_style
            )
        )

    else:

        for i, item in enumerate(history, start=1):

            question = str(item[1]).replace("\n", "<br/>")
            answer = str(item[2]).replace("\n", "<br/>")
            created = str(item[3])

            elements.append(
                Paragraph(
                    f"Hội thoại {i}",
                    heading_style
                )
            )

            elements.append(
                Paragraph(
                    "Câu hỏi:",
                    heading_style
                )
            )

            elements.append(
                Paragraph(
                    question,
                    body_style
                )
            )

            elements.append(
                Spacer(1, 8)
            )

            elements.append(
                Paragraph(
                    "Trả lời:",
                    heading_style
                )
            )

            elements.append(
                Paragraph(
                    answer,
                    body_style
                )
            )

            elements.append(
                Spacer(1, 8)
            )

            elements.append(
                Paragraph(
                    f"Thời gian: {created}",
                    body_style
                )
            )

            elements.append(
                Spacer(1, 18)
            )

    doc.build(elements)
