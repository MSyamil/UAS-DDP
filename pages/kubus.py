import streamlit as st
import plotly.graph_objects as go
import base64

st.set_page_config(
    page_title="Visualisasi Kubus",
    page_icon="https://cdn.icon-icons.com/icons2/2334/PNG/96/box_cube_d_perspective_shape_icon_142362.png",
    layout="wide"
)

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

# Definisikan kelas Kubus
class Kubus:
    def __init__(self, sisi, warna, warna_tepi):
        self.sisi = sisi  # Variabel sisi kubus
        self.warna = warna  # Variabel warna kubus
        self.warna_tepi = warna_tepi  # warna garis tepi

    # Fungsi untuk menghitung luas permukaan kubus
    def hitung_luas_permukaan(self):
        return 6 * self.sisi ** 2  # Menghitung luas permukaan kubus
    
    # Fungsi untuk menghitung volume kubus
    def hitung_volume(self):
        return self.sisi ** 3  # Menghitung volume kubus

    # Fungsi untuk menampilkan visualisasi kubus 3D dengan garis
    def tampilkan_kubus_3d(self):
        # Koordinat titik-titik sudut kubus
        x = [0, self.sisi, self.sisi, 0, 0, self.sisi, self.sisi, 0]
        y = [0, 0, self.sisi, self.sisi, 0, 0, self.sisi, self.sisi]
        z = [0, 0, 0, 0, self.sisi, self.sisi, self.sisi, self.sisi]

        # Tampilkan kubus sebagai mesh 3D dengan warna
        fig = go.Figure()

        # Menambahkan wajah kubus (mesh)
        fig.add_trace(go.Mesh3d(
            x=x,
            y=y,
            z=z,
            opacity=0.5,
            color=self.warna,  # Warna kubus
            flatshading=True
        ))

        # Menambahkan garis tepi kubus (edges)
        edges_x = [x[0], x[1], x[1], x[2], x[2], x[3], x[3], x[0], x[4], x[5], x[5], x[6], x[6], x[7], x[7], x[4], x[0], x[4], x[1], x[5], x[2], x[6], x[3], x[7]]
        edges_y = [y[0], y[1], y[1], y[2], y[2], y[3], y[3], y[0], y[4], y[5], y[5], y[6], y[6], y[7], y[7], y[4], y[0], y[4], y[1], y[5], y[2], y[6], y[3], y[7]]
        edges_z = [z[0], z[1], z[1], z[2], z[2], z[3], z[3], z[0], z[4], z[5], z[5], z[6], z[6], z[7], z[7], z[4], z[0], z[4], z[1], z[5], z[2], z[6], z[3], z[7]]

        # Menambahkan garis pada kubus
        fig.add_trace(go.Scatter3d(
            x=edges_x,
            y=edges_y,
            z=edges_z,
            mode='lines',
            line=dict(color=self.warna_tepi, width=2)  # Garis hitam dengan ketebalan 2
        ))

        # Layout kubus 3D
        fig.update_layout(
            scene=dict(
                xaxis=dict(range=[0, self.sisi]),
                yaxis=dict(range=[0, self.sisi]),
                zaxis=dict(range=[0, self.sisi]),
            ),
            title="Visualisasi Kubus 3D dengan Garis",
            scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
        )

        # Tampilkan kubus 3D di Streamlit
        st.plotly_chart(fig)

# Fungsi untuk validasi input
def validasi_input(sisi):
    if sisi < 5:
        st.warning("Panjang sisi terlalu kecil! Coba sisi yang lebih besar.")
        return False
    elif sisi > 100:
        st.warning("Panjang sisi terlalu besar! Coba sisi yang lebih kecil.")
        return False
    else:
        st.success(f"Sisi {sisi} cm valid, perhitungan volume akan dilakukan.")
        return True

# Fungsi untuk memvalidasi input dengan while loop
def validasi_input_while():
    sisi = st.number_input("Masukkan panjang sisi kubus (cm):", min_value=0.0, step=0.1)
    while sisi < 0:  # Jika sisi kubus tidak valid
        if sisi < 0:
            st.warning("Panjang sisi terlalu kecil! Coba sisi yang lebih besar.")
    return sisi

# Menampilkan judul aplikasi
st.title("Aplikasi Perhitungan Luas dan Volume Kubus")

# Meminta input sisi kubus dengan validasi menggunakan while loop
sisi = validasi_input_while()

# Input pilihan warna kubus
warna = st.color_picker('Pilih warna kubus:', '#00bfae')  # Default color
    
# Input pilihan warna garis tepi kubus
warna_tepi = st.color_picker('Pilih warna garis tepi kubus:', '#000000')  # Default black color

# Membuat objek Kubus
kubus = Kubus(sisi, warna, warna_tepi)

# Menghitung luas permukaan dan volume kubus dan menampilkan hasilnya
lp = kubus.hitung_luas_permukaan()
st.write(f"Luas permukaan kubus dengan sisi {sisi} cm adalah {lp} cm²")
volume = kubus.hitung_volume()
st.write(f"Volume kubus dengan sisi {sisi} cm adalah {volume} cm³")

# Menampilkan visualisasi kubus 3D
if sisi > 0 :
    kubus.tampilkan_kubus_3d()