import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title('Menghitung volme dan luas permukaan balok')

# Menentukan nilai x,y,z
def plot_balok(p,l,t):
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
        title=f"Visualisasi balok (p={p} cm, l={l} cm, t={t} cm)",
    )
    return fig

#input
p = st.number_input("Masukkan panjang balok (cm):", min_value=0.0, step=0.1)
l = st.number_input("Masukkan lebar balok (cm):", min_value=0.0, step=0.1)
t = st.number_input("Masukkan tinggi balok (cm):", min_value=0.0, step=0.1)
if p > 0 and l > 0 and t > 0:
    fig = plot_balok(p, l, t)
    st.plotly_chart(fig)
    st.write(f"Volume balok: {p * l * t} cm³")
    Luas_permukaan = 2 * (l * l + l * t + l * t)
    st.write(f"Luas Permukaan balok = {Luas_permukaan}")
