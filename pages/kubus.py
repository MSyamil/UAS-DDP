import streamlit as st
import plotly.graph_objects as go

# Definisikan kelas Kubus
class Kubus:
    def __init__(self, sisi, warna, warna_tepi):
        self.sisi = sisi  # Variabel sisi kubus
        self.warna = warna  # Variabel warna kubus
        self.warna_tepi = warna_tepi  # warna garis tepi

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
    sisi = st.number_input("Masukkan panjang sisi kubus (cm):", min_value=5.0, step=0.0)
    while sisi < 5 or sisi > 100:  # Jika sisi kubus tidak valid
        if sisi < 5:
            st.warning("Panjang sisi terlalu kecil! Coba sisi yang lebih besar.")
        elif sisi > 100:
            st.warning("Panjang sisi terlalu besar! Coba sisi yang lebih kecil.")
        sisi = st.number_input("Masukkan panjang sisi kubus (cm):", min_value=5.0, step=0.1)
    return sisi
 
st.title("Aplikasi Perhitungan Volume Kubus")

# Meminta input sisi kubus dengan validasi menggunakan while loop
sisi = validasi_input_while()

# Input pilihan warna kubus
warna = st.color_picker('Pilih warna kubus:', '#00bfae')  # Default color
    
# Input pilihan warna garis tepi kubus
warna_tepi = st.color_picker('Pilih warna garis tepi kubus:', '#000000')  # Default black color

# Membuat objek Kubus
kubus = Kubus(sisi, warna, warna_tepi)

# Menghitung volume kubus dan menampilkan hasilnya
volume = kubus.hitung_volume()
st.write(f"Volume kubus dengan sisi {sisi} cm adalah {volume} cm³")

# Menampilkan visualisasi kubus 3D
kubus.tampilkan_kubus_3d()
