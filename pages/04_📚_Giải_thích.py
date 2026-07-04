import streamlit as st

from gpt_service import ask_ai
from database import Database

db = Database()

st.set_page_config(
    page_title="Giải thích bài học",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Giải thích bài học")

st.write("AI hỗ trợ giải thích kiến thức theo nhiều mức độ.")

st.markdown("---")

topic = st.text_input(
    "Nhập chủ đề",
    placeholder="Ví dụ: SQL JOIN, Machine Learning, Định luật Newton..."
)

level = st.selectbox(
    "Chọn mức độ",
    [
        "Dễ",
        "Trung bình",
        "Nâng cao"
    ]
)

if st.button("📚 Giải thích", use_container_width=True):

    if topic.strip() == "":
        st.warning("⚠️ Vui lòng nhập chủ đề.")
        st.stop()

    prompt = f"""
Bạn là một giảng viên đại học giàu kinh nghiệm.

Hãy giải thích chủ đề sau:

{topic}

Yêu cầu:

- Mức độ: {level}
- Trả lời bằng tiếng Việt.
- Giải thích rõ ràng, logic và dễ hiểu.
- Chia thành các mục có tiêu đề.
- Đưa ra ví dụ minh họa.
- Nếu có công thức thì trình bày rõ ràng.
- Nếu có ưu điểm và nhược điểm thì liệt kê.
- Nếu phù hợp, hãy nêu ứng dụng thực tế.
"""

    with st.spinner("🤖 AI đang giải thích..."):

        answer = ask_ai(prompt)

    db.save(
        f"Giải thích ({level}): {topic}",
        answer
    )

    st.markdown("---")

    st.subheader("📖 Chủ đề")

    st.info(topic)

    st.subheader("🤖 AI giải thích")

    st.markdown(answer)

    st.success("✅ Đã lưu vào lịch sử.")