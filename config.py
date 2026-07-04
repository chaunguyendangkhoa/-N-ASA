import streamlit as st
import os

APP_NAME = "AI Study Assistant"
VERSION = "1.0"
AUTHOR = "Châu Nguyễn Đăng Khoa"

MODEL_NAME = "llama-3.3-70b-versatile"

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

DATABASE_NAME = "database/history.db"

EXPORT_FOLDER = "exports"
UPLOAD_FOLDER = "uploads"
