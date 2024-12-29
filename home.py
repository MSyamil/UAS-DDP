import streamlit as st

st.set_page_config(
    page_title="Halaman Utama",
    page_icon="🏠",
    layout="wide"
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("Halaman Utama")
    st.write("Selamat Datang di Aplikasi Menghitung Bangun Ruang")
