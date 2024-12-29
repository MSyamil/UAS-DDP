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

st.title('Menghitung Volume dan Luas Permukaan Balok')

# Menentukan nilai x, y, z untuk visualisasi balok
def plot_balok(p, l, t):
    fig = go.Figure()
    x = [0, p, p, 0, 0, p, p, 0]
    y = [0, 0, l, l, 0, 0, l, l]
    z = [0, 0, 0, 0, t, t, t, t]
    
    # Menentukan garis
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]
    
    # Membuat garis dari indeks 0 dan indeks 1
    for edge in edges:
        fig.add_trace(go.Scatter3d(
            x=[x[edge[0]], x[edge[1]]],
            y=[y[edge[0]], y[edge[1]]],
            z=[z[edge[0]], z[edge[1]]],
            mode='lines',
            line=dict(color='blue', width=5)
        ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        title=f"Visualisasi Balok (Panjang={p} cm, Lebar={l} cm, Tinggi={t} cm)",
    )
    return fig

# Input untuk panjang, lebar, dan tinggi balok
p = st.number_input("Masukkan panjang balok (cm):", min_value=0.0, step=0.1)
l = st.number_input("Masukkan lebar balok (cm):", min_value=0.0, step=0.1)
t = st.number_input("Masukkan tinggi balok (cm):", min_value=0.0, step=0.1)

if p > 0 and l > 0 and t > 0:
    # Menampilkan visualisasi balok
    fig = plot_balok(p, l, t)
    st.plotly_chart(fig)
    
    # Menghitung dan menampilkan volume dan luas permukaan
    st.write(f"Volume balok: {p * l * t} cm³")
    luas_permukaan = 2 * (p * l + p * t + l * t)
    st.write(f"Luas Permukaan Balok = {luas_permukaan} cm²")
else:
    st.write("Masukkan nilai yang valid untuk panjang, lebar, dan tinggi.")
