import os
import streamlit as st

from database import Database
from export_pdf import export_history_to_pdf

db = Database()

st.set_page_config(
    page_title="Lịch sử",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Lịch sử hội thoại")

st.markdown("---")

history = db.get_all()

st.metric("Tổng số hội thoại", len(history))

st.markdown("---")

# ==========================
# Tìm kiếm
# ==========================

keyword = st.text_input(
    "🔍 Tìm kiếm",
    placeholder="Nhập từ khóa..."
)

if keyword.strip():
    history = [
        item for item in history
        if keyword.lower() in item[1].lower()
        or keyword.lower() in item[2].lower()
    ]

# ==========================
# Hiển thị lịch sử
# ==========================

if len(history) == 0:

    st.info("📭 Chưa có lịch sử hội thoại.")

else:

    for item in history:

        with st.expander(f"📝 Hội thoại #{item[0]}"):

            st.markdown("### ❓ Câu hỏi")
            st.write(item[1])

            st.markdown("### 🤖 Trả lời")
            st.write(item[2])

            st.caption(f"🕒 {item[3]}")

# ==========================
# Chức năng
# ==========================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🔄 Làm mới", use_container_width=True):
        st.rerun()

with col2:

    if st.button("🗑 Xóa toàn bộ", use_container_width=True):

        db.delete_all()

        st.success("Đã xóa toàn bộ lịch sử.")

        st.rerun()

with col3:

    if st.button("📄 Xuất PDF", use_container_width=True):

        if len(history) == 0:

            st.warning("Không có dữ liệu để xuất.")

        else:

            os.makedirs("exports", exist_ok=True)

            filename = "exports/history.pdf"

            export_history_to_pdf(
                history,
                filename
            )

            with open(filename, "rb") as f:

                st.download_button(
                    label="⬇️ Tải PDF",
                    data=f,
                    file_name="history.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
