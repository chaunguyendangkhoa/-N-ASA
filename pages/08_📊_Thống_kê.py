import streamlit as st

from database import Database

db = Database()

st.set_page_config(
    page_title="Thống kê",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Thống kê hệ thống")

st.markdown("---")

count = db.get_count()

history = db.get_all()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        label="📝 Tổng số hội thoại",
        value=count
    )

with col2:

    if count > 0:
        latest = history[0][3]
    else:
        latest = "Chưa có"

    st.metric(
        label="🕒 Hội thoại gần nhất",
        value=latest
    )

st.markdown("---")

if count == 0:

    st.info("Hiện chưa có dữ liệu để thống kê.")

else:

    st.success(f"Hệ thống đã lưu {count} hội thoại.")

    st.progress(min(count / 100, 1.0))

    total_question = sum(len(item[1]) for item in history)
    total_answer = sum(len(item[2]) for item in history)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "📄 Tổng ký tự câu hỏi",
            total_question
        )

    with col4:
        st.metric(
            "🤖 Tổng ký tự câu trả lời",
            total_answer
        )

st.markdown("---")

st.subheader("📌 Thông tin hệ thống")

st.write("🤖 AI Model: Llama 3.3 70B Versatile (Groq API)")
st.write("☁️ AI Service: Groq Cloud")
st.write("🌐 Framework: Streamlit")
st.write("🗄 Database: SQLite")
st.write("💻 Ngôn ngữ: Python")

st.markdown("---")

st.info(
    "Dữ liệu thống kê được lấy từ cơ sở dữ liệu SQLite. "
    "Việc xử lý ngôn ngữ được thực hiện thông qua Groq API."
)