import base64
import streamlit as st

# Fungsi untuk memuat gambar dari file lokal dan mengkonversinya ke base64
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set halaman
st.set_page_config(
    page_title="Halaman Utama",
    page_icon="🏠",
    layout="wide"
)

# Memuat gambar latar belakang dari folder 'image' dengan nama file 'bg1.jpg'
image_path = "image/bg1.jpg"
image_base64 = load_image(image_path)

# Menambahkan CSS untuk latar belakang gambar
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{image_base64}');
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Kolom untuk layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("Halaman Utama")
    st.write("Selamat Datang di Aplikasi Menghitung Bangun Ruang")
