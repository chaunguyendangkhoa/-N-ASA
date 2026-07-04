import streamlit as st

from gpt_service import ask_ai
from database import Database

db = Database()

st.set_page_config(
    page_title="Sinh Email",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Sinh Email")

st.write("AI hỗ trợ tạo Email chuyên nghiệp.")

st.markdown("---")

purpose = st.text_input(
    "Mục đích",
    placeholder="Ví dụ: Xin nghỉ học, Xin việc, Xin thực tập..."
)

receiver = st.text_input(
    "Người nhận",
    placeholder="Ví dụ: Giảng viên, Công ty ABC..."
)

style = st.selectbox(
    "Phong cách",
    [
        "Lịch sự",
        "Chuyên nghiệp",
        "Thân thiện"
    ]
)

if st.button("📝 Tạo Email", use_container_width=True):

    if purpose.strip() == "":
        st.warning("⚠️ Vui lòng nhập mục đích.")
        st.stop()

    if receiver.strip() == "":
        st.warning("⚠️ Vui lòng nhập người nhận.")
        st.stop()

    prompt = f"""
Bạn là chuyên gia soạn thảo Email.

Hãy viết một Email bằng tiếng Việt.

Thông tin:

Mục đích:
{purpose}

Người nhận:
{receiver}

Yêu cầu:

- Phong cách: {style}
- Có tiêu đề Email.
- Có lời chào phù hợp.
- Nội dung mạch lạc, lịch sự.
- Có lời cảm ơn.
- Có lời kết.
- Không thêm giải thích ngoài nội dung Email.
"""

    with st.spinner("🤖 AI đang soạn Email..."):

        answer = ask_ai(prompt)

    db.save(
        f"Email ({style}): {purpose}",
        answer
    )

    st.markdown("---")

    st.subheader("📨 Email được tạo")

    st.markdown(answer)

    st.success("✅ Đã lưu vào lịch sử.")