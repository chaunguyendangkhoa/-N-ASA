import streamlit as st

from gpt_service import ask_ai
from database import Database

db = Database()

st.set_page_config(
    page_title="Tóm tắt văn bản",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Tóm tắt văn bản")

st.write("AI hỗ trợ tóm tắt văn bản nhanh chóng và chính xác.")

st.markdown("---")

text = st.text_area(
    "Nhập văn bản cần tóm tắt",
    height=300,
    placeholder="Dán nội dung cần tóm tắt vào đây..."
)

summary_type = st.selectbox(
    "Kiểu tóm tắt",
    [
        "Ngắn gọn",
        "Chi tiết",
        "Gạch đầu dòng"
    ]
)

if st.button("📄 Tóm tắt", use_container_width=True):

    if text.strip() == "":
        st.warning("⚠️ Vui lòng nhập văn bản.")
        st.stop()

    if summary_type == "Ngắn gọn":

        prompt = f"""
Bạn là chuyên gia tóm tắt văn bản.

Hãy tóm tắt nội dung sau thật ngắn gọn (khoảng 3–5 câu).

Chỉ trả về phần tóm tắt.

Văn bản:

{text}
"""

    elif summary_type == "Chi tiết":

        prompt = f"""
Bạn là chuyên gia tóm tắt văn bản.

Hãy tóm tắt đầy đủ các ý chính của nội dung dưới đây.

Giữ nguyên ý nghĩa.

Văn bản:

{text}
"""

    else:

        prompt = f"""
Bạn là chuyên gia tóm tắt văn bản.

Hãy tóm tắt nội dung dưới dạng danh sách gạch đầu dòng.

Mỗi ý là một dòng.

Văn bản:

{text}
"""

    with st.spinner("🤖 AI đang tóm tắt..."):

        answer = ask_ai(prompt)

    db.save(
        f"Tóm tắt ({summary_type}): {text}",
        answer
    )

    st.markdown("---")

    st.subheader("📄 Kết quả")

    st.markdown(answer)

    st.success("✅ Đã lưu vào lịch sử.")