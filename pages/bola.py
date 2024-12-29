import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Visualisasi Lingkaran",
    page_icon="🌐",
    layout="wide"
)
def plot_bola(r):
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)

    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    fig = go.Figure()

    for i in range(len(u)):
        fig.add_trace(go.Scatter3d(
            x=x[i, :],
            y=y[i, :],
            z=z[i, :],
            mode='lines',
            line=dict(color='blue', width=2)
        ))

    for i in range(len(v)):
        fig.add_trace(go.Scatter3d(
            x=x[:, i],
            y=y[:, i],
            z=z[:, i],
            mode='lines',
            line=dict(color='blue', width=2)
        ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        title=f"Visualisasi Rangka Bola (r={r} cm)",
    )
    return fig

st.title("Visualisasi Lingkaran")

# r = st.slider("Masukkan Jari-jari Lingkaran (cm)", 1, 100, 10)
r = st.number_input("Masukkan Jari-jari Lingkaran (cm)", min_value=0)

if r <= 0:
    st.error("Jari-jari Lingkaran harus lebih besar dari 0 cm.")
else:
    fig = plot_bola(r)
    st.plotly_chart(fig)
    st.write(f"Luas Permukaan Bola = {4 * np.pi * r**2} cm^2")
    st.write(f"Volume Bola = {4/3 * np.pi * r**3} cm^3")
