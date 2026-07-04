import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

# ===========================
# Sidebar
# ===========================

with st.sidebar:

    st.title("🤖 AI Study Assistant")

    st.markdown("---")

    st.success("Đề tài")

    st.write("Ứng dụng AI tạo sinh hỗ trợ học tập")

    st.markdown("---")

    st.success("Công nghệ")

    st.write("🐍 Python")
    st.write("🌐 Streamlit")
    st.write("⚡ Groq API")
    st.write("🦙 Llama 3.3 70B")
    st.write("🗄 SQLite")

    st.markdown("---")

    st.success("Thông tin sinh viên")

    st.write("**Họ tên:**")
    st.write("Chau Nguyễn Đăng Khoa")

    st.write("**MSSV:**")
    st.write("00000000000")

    st.markdown("---")

    st.write("Phiên bản")

    st.success("Version 2.0")

    st.markdown("---")

    st.info("Chọn chức năng ở menu bên trái.")

# ===========================
# Nội dung chính
# ===========================

st.title("🤖 AI Study Assistant")

st.subheader("Đồ án ứng dụng AI tạo sinh hỗ trợ học tập")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.header("📖 Giới thiệu")

    st.write("""
AI Study Assistant là ứng dụng hỗ trợ học tập sử dụng Trí tuệ nhân tạo (AI).

Ứng dụng được xây dựng bằng Python và Streamlit, sử dụng Groq API để truy cập mô hình ngôn ngữ lớn (LLM).

Hệ thống hỗ trợ học tập, lập trình, dịch thuật, tóm tắt văn bản và giải thích kiến thức.
""")

with col2:

    st.header("⭐ Chức năng")

    st.write("💬 Chat AI")
    st.write("🌍 Dịch văn bản")
    st.write("📄 Tóm tắt")
    st.write("📚 Giải thích bài học")
    st.write("💻 Hỗ trợ lập trình")
    st.write("📝 Sinh Email")
    st.write("📜 Lịch sử")
    st.write("📊 Thống kê")

st.markdown("---")

st.header("🚀 Hướng dẫn sử dụng")

st.markdown("""
1. Chọn chức năng ở menu bên trái.

2. Nhập nội dung cần xử lý.

3. Nhấn nút **Thực hiện**.

4. AI sẽ trả lời sau vài giây.

5. Lịch sử được lưu vào SQLite.
""")

st.markdown("---")

st.success("✅ Hệ thống đã sẵn sàng.")

st.info("""
**Mô hình AI:** Llama 3.3 70B (Groq API)

**Cơ sở dữ liệu:** SQLite

**Framework:** Streamlit
""")

st.markdown("---")

st.caption("© 2026 AI Study Assistant | Đồ án AI tạo sinh")
