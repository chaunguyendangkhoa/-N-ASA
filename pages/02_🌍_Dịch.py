import streamlit as st

from gpt_service import ask_ai
from database import Database

db = Database()

st.set_page_config(
    page_title="Dịch văn bản",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Dịch văn bản")

st.write("Nhập nội dung cần dịch và chọn ngôn ngữ đích.")

st.markdown("---")

text = st.text_area(
    "Nhập văn bản",
    height=250,
    placeholder="Ví dụ: Hello everyone, how are you today?"
)

language = st.selectbox(
    "Ngôn ngữ đích",
    [
        "Tiếng Việt",
        "Tiếng Anh",
        "Tiếng Nhật",
        "Tiếng Hàn",
        "Tiếng Trung"
    ]
)

if st.button("🌍 Dịch", use_container_width=True):

    if text.strip() == "":
        st.warning("⚠️ Vui lòng nhập văn bản.")
        st.stop()

    prompt = f"""
Bạn là một dịch giả chuyên nghiệp.

Hãy dịch chính xác nội dung dưới đây sang {language}.

Yêu cầu:

- Giữ nguyên ý nghĩa.
- Giữ nguyên tên riêng nếu có.
- Không thêm lời giải thích.
- Chỉ trả về bản dịch.

Văn bản:

{text}
"""

    with st.spinner("🤖 AI đang dịch..."):

        answer = ask_ai(prompt)

    db.save(
        f"Dịch sang {language}: {text}",
        answer
    )

    st.markdown("---")

    st.subheader("📄 Kết quả")

    st.markdown(answer)

    st.success("✅ Đã lưu vào lịch sử.")