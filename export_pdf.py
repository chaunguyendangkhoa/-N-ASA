import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ==========================
# Font
# ==========================

FONT_NAME = "Helvetica"

font_path = os.path.join(
    "font",
    "NotoSans-Regular.ttf"
)

if os.path.exists(font_path):

    try:

        pdfmetrics.registerFont(
            TTFont(
                "NotoSans",
                font_path
            )
        )

        FONT_NAME = "NotoSans"

    except Exception as e:

        print("Không thể đăng ký font:", e)

        FONT_NAME = "Helvetica"

else:

    print("Không tìm thấy font:", font_path)

# ==========================
# Styles
# ==========================

styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.fontName = FONT_NAME
title_style.fontSize = 22
title_style.leading = 28
title_style.alignment = TA_CENTER

body_style = styles["BodyText"]
body_style.fontName = FONT_NAME
body_style.fontSize = 11
body_style.leading = 18

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

    elements.append(
        Spacer(1, 20)
    )

    if len(history) == 0:

        elements.append(
            Paragraph(
                "Chưa có dữ liệu.",
                body_style
            )
        )

    else:

        for index, item in enumerate(history, start=1):

            question = str(item[1]).replace("\n", "<br/>")
            answer = str(item[2]).replace("\n", "<br/>")
            created = str(item[3])

            elements.append(
                Paragraph(
                    f"<b>Hội thoại #{index}</b>",
                    body_style
                )
            )

            elements.append(
                Spacer(1, 8)
            )

            elements.append(
                Paragraph(
                    f"<b>Câu hỏi:</b><br/>{question}",
                    body_style
                )
            )

            elements.append(
                Spacer(1, 8)
            )

            elements.append(
                Paragraph(
                    f"<b>Trả lời:</b><br/>{answer}",
                    body_style
                )
            )

            elements.append(
                Spacer(1, 8)
            )

            elements.append(
                Paragraph(
                    f"<b>Thời gian:</b> {created}",
                    body_style
                )
            )

            elements.append(
                Spacer(1, 20)
            )

    doc.build(elements)
