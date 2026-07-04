import streamlit as st

from gpt_service import ask_ai
from database import Database

db = Database()

st.set_page_config(
    page_title="Hỗ trợ lập trình",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Hỗ trợ lập trình")

st.write("AI hỗ trợ sinh mã nguồn và giải thích chương trình.")

st.markdown("---")

language = st.selectbox(
    "Ngôn ngữ lập trình",
    [
        "Python",
        "C++",
        "Java",
        "C#",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript"
    ]
)

request = st.text_area(
    "Nhập yêu cầu",
    height=250,
    placeholder="Ví dụ: Viết chương trình quản lý sinh viên bằng Python sử dụng hướng đối tượng."
)

if st.button("💻 Sinh mã nguồn", use_container_width=True):

    if request.strip() == "":
        st.warning("⚠️ Vui lòng nhập yêu cầu.")
        st.stop()

    prompt = f"""
Bạn là lập trình viên cao cấp.

Hãy viết chương trình bằng {language}.

Yêu cầu:

{request}

Quy định:

- Viết đầy đủ mã nguồn.
- Đặt tên biến rõ ràng.
- Có chú thích trong code.
- Sau phần code hãy giải thích chương trình.
- Nếu có nhiều cách thì chọn cách tối ưu.
- Trả lời bằng tiếng Việt.
"""

    with st.spinner("🤖 AI đang sinh mã nguồn..."):

        answer = ask_ai(prompt)

    db.save(
        f"Lập trình ({language}): {request}",
        answer
    )

    st.markdown("---")

    st.subheader("📝 Yêu cầu")

    st.info(request)

    st.subheader("💻 Kết quả")

    st.markdown(answer)

    st.success("✅ Đã lưu vào lịch sử.")