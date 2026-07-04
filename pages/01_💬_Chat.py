import streamlit as st

from gpt_service import ask_ai
from database import Database

db = Database()

st.title("💬 Chat AI")

st.write("Đặt câu hỏi cho AI và nhận câu trả lời trong vài giây.")

question = st.text_area(
    "Nhập câu hỏi",
    height=200,
    placeholder="Ví dụ: SQL JOIN là gì?"
)

if st.button("🚀 Gửi", use_container_width=True):

    if question.strip() == "":
        st.warning("Vui lòng nhập câu hỏi.")
        st.stop()

    with st.spinner("🤖 AI đang xử lý..."):

        answer = ask_ai(question)

    st.markdown("---")

    st.subheader("❓ Câu hỏi")

    st.write(question)

    st.subheader("🤖 AI trả lời")

    st.markdown(answer)

    db.save(question, answer)

    st.success("✅ Đã lưu vào lịch sử.")