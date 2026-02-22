import streamlit as st
import matplotlib.pyplot as plt

# --- TÍTULO DE AUTORÍA ---
st.title("Simulación de Santiago Caballero Aguilar")

# Diccionario optimizado de Grados Brix (°Bx)
bebidas_datos = {
    "Agua Destilada": 0.0, "Té Verde": 0.2, "Agua de Coco": 4.5,
    "Cerveza Lager": 4.0, "Bebida Deportiva": 6.0, "Leche Entera": 11.5,
    "Jugo de Tomate": 5.0, "Limonada": 8.5, "Jugo de Naranja": 10.5,
    "Refresco de Cola": 10.8, "Jugo de Manzana": 13.5, "Jugo de Uva": 16.0,
    "Kétchup": 25.0, "Salsa BBQ": 40.0, "Jarabe de Fruta": 45.0,
    "Leche Condensada": 54.0, "Mermelada": 68.0, "Miel de Abeja": 82.0
}

def dibujar_visor_pro(brix):
    plt.rcParams['figure.facecolor'] = '#f0f0f0'
    fig, ax = plt.subplots(figsize=(8, 8))

    circulo_exterior = plt.Circle((0.5, 0.5), 0.48, color='#2c3e50', zorder=1)
    circulo_interior = plt.Circle((0.5, 0.5), 0.45, color='white', zorder=2)
    ax.add_artist(circulo_exterior)
    ax.add_artist(circulo_interior)

    nivel = 0.05 + (0.9 * (brix / 100))
    rect_azul = plt.Rectangle((0, 0), 1, nivel, color='#2980b9', alpha=0.85, zorder=3)
    ax.add_artist(rect_azul)

    for i in range(0, 101, 5):
        y_pos = 0.05 + (0.9 * (i / 100))
        color_linea = 'white' if i <= brix else '#2c3e50'
        if i % 10 == 0:
            ax.plot([0.42, 0.58], [y_pos, y_pos], color=color_linea, lw=1.5, zorder=4)
            ax.text(0.40, y_pos, f"{i}", ha='right', va='center',
                    color=color_linea, fontsize=10, fontweight='bold', zorder=5)
        else:
            ax.plot([0.47, 0.53], [y_pos, y_pos], color=color_linea, lw=0.5, zorder=4)

    ax.axhline(nivel, color='#e74c3c', lw=2, linestyle='--', zorder=6)
    ax.text(0.65, nivel, f" LECTURA: {brix}°Bx", color='#e74c3c',
            fontweight='bold', fontsize=12, zorder=6)

    from matplotlib.patches import Circle
    patch = Circle((0.5, 0.5), 0.45, transform=ax.transData)
    rect_azul.set_clip_path(patch)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.title("SISTEMA DE MEDICIÓN BRIX ANALÓGICO", fontsize=16,
              color='#2c3e50', fontweight='bold', pad=20)
    
    st.pyplot(fig)

# --- INTERFAZ STREAMLIT ---
seleccion = st.selectbox('🧪 SELECCIONAR MUESTRA:', sorted(bebidas_datos.keys()))
valor = bebidas_datos[seleccion]

# Panel informativo con Markdown HTML de Santiago
st.markdown(f"""
<div style="background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #2980b9; margin-bottom: 10px;">
    <h3 style="margin: 0; color: #2c3e50;">Muestra: {seleccion}</h3>
    <p style="margin: 5px 0; color: #7f8c8d;">Concentración detectada: <b>{valor} °Bx</b></p>
</div>
""", unsafe_allow_html=True)

dibujar_visor_pro(valor)
