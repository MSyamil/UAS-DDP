import streamlit as st
import plotly.graph_objects as go
import numpy as np
import base64

# Fungsi untuk memuat gambar dari file lokal dan mengkonversinya ke base64
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Menambahkan CSS untuk latar belakang gambar
image_path = "image/bg2.jpg"  # Ganti dengan path gambar yang sesuai
image_base64 = load_image(image_path)

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

# Class untuk Tabung
class Tabung:
    def __init__(self, radius, tinggi):
        self.radius = radius  # Menyimpan radius tabung
        self.tinggi = tinggi  # Menyimpan tinggi tabung

    # Metode untuk menghitung volume dan luas permukaan tabung
    def hitung_luas_volume(self):
        volume = np.pi * self.radius**2 * self.tinggi
        luas = 2 * np.pi * self.radius * (self.radius + self.tinggi)
        return volume, luas

    # Metode untuk visualisasi tabung
    def visualisasi_tabung(self):
        theta = np.linspace(0, 2 * np.pi, 30)  # Sudut untuk permukaan tabung
        X = self.radius * np.cos(theta)  # Koordinat X
        Y = self.radius * np.sin(theta)  # Koordinat Y

        fig = go.Figure()

        # Menghubungkan titik bawah dan atas tabung dengan garis vertikal
        for i in range(len(theta)):
            fig.add_trace(go.Scatter3d(
                x=[X[i], X[i]], y=[Y[i], Y[i]], z=[0, self.tinggi],
                mode='lines', line=dict(color='blue', width=2), showlegend=False
            ))

        # Garis horizontal untuk menutup alas dan penutup tabung
        for i in range(len(theta) - 1):
            fig.add_trace(go.Scatter3d(x=[X[i], X[i+1]], y=[Y[i], Y[i+1]], z=[0, 0], mode='lines', line=dict(color='aqua', width=2), showlegend=False))
            fig.add_trace(go.Scatter3d(x=[X[i], X[i+1]], y=[Y[i], Y[i+1]], z=[self.tinggi, self.tinggi], mode='lines', line=dict(color='aqua', width=2), showlegend=False))

        # Menambahkan garis dari pusat ke tepi untuk alas dan penutup
        for i in range(len(theta)):
            fig.add_trace(go.Scatter3d(x=[0, X[i]], y=[0, Y[i]], z=[0, 0], mode='lines', line=dict(color='cyan', width=2), showlegend=False))
            fig.add_trace(go.Scatter3d(x=[0, X[i]], y=[0, Y[i]], z=[self.tinggi, self.tinggi], mode='lines', line=dict(color='cyan', width=2), showlegend=False))

        fig.update_layout(
            title="Visualisasi Tabung dengan Edges dan Alas/Penutup",
            scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
            margin=dict(l=0, r=0, b=0, t=50)  # Mengatur margin atas agar tidak terhalang oleh teks
        )

        return fig

# Menampilkan input untuk jari-jari dan tinggi
st.title("Perhitungan Luas dan Volume Tabung")
radius = st.number_input("Masukkan Jari-jari (cm)", min_value=0.0, step=0.1)
tinggi = st.number_input("Masukkan Tinggi Tabung (cm)", min_value=0.0, step=0.1)

if radius > 0 and tinggi > 0:
    # Membuat objek Tabung
    tabung = Tabung(radius, tinggi)

    # Hitung luas dan volume
    volume, luas = tabung.hitung_luas_volume()
    
    # Menampilkan hasil perhitungan
    st.write(f"Volume Tabung: {volume:.2f} cm³")
    st.write(f"Luas Permukaan Tabung: {luas:.2f} cm²")
    
    # Tambahkan jarak kosong (spasi) antara teks dan grafik
    st.write("\n")
    
    # Menampilkan visualisasi tabung
    fig = tabung.visualisasi_tabung()
    st.plotly_chart(fig)

else:
    st.write("Masukkan nilai yang valid untuk jari-jari dan tinggi.")
