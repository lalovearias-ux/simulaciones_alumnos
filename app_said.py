import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# --- TÍTULO DE AUTORÍA ---
st.title("Simulación de Said Hernandez Sanchez")

# --- CONFIGURACIÓN DE DATOS ---
bebidas = {
    "1": {"nombre": "Agua Destilada (Control)", "brix": 0.0, "color": "blue"},
    "2": {"nombre": "Jugo de Manzana Natural", "brix": 12.0, "color": "orange"},
    "3": {"nombre": "Refresco de Cola", "brix": 10.6, "color": "brown"},
    "4": {"nombre": "Bebida Deportiva (Isotónica)", "brix": 6.0, "color": "cyan"},
    "5": {"nombre": "Jarabe de Maíz (Muy dulce)", "brix": 75.0, "color": "yellow"},
    "6": {"nombre": "Jugo de Uva", "brix": 16.0, "color": "purple"}
}

def graficar_vista_refractometro(valor_brix, nombre_bebida):
    fig, ax = plt.subplots(figsize=(6, 6))
    circulo = plt.Circle((0.5, 0.5), 0.5, color='black', fill=False, linewidth=5)
    ax.add_artist(circulo)

    escala_max = 32 if valor_brix < 32 else 85
    nivel = valor_brix / escala_max

    ax.axhspan(0, nivel, xmin=0, xmax=1, color='cornflowerblue', alpha=0.8, label="Zona Azul")
    ax.axhspan(nivel, 1, xmin=0, xmax=1, color='white', alpha=1.0)
    ax.axhline(y=nivel, color='red', linestyle='--', linewidth=2)

    ax.text(0.5, nivel + 0.02, f"{valor_brix} °Bx", horizontalalignment='center', color='red', fontweight='bold', fontsize=12)
    ax.set_title(f"Lectura del Refractómetro: {nombre_bebida}", fontsize=14)

    ax.set_yticks(np.linspace(0, 1, 11))
    ax.set_yticklabels([f"{int(x)}" for x in np.linspace(0, escala_max, 11)])
    ax.set_xticks([]) 

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('#333333')

    st.pyplot(fig)

# --- INTERFAZ STREAMLIT ---
st.text("🔬 --- SIMULADOR DE REFRACTOMETRÍA --- 🔬\n------------------------------------------\n¿Qué es un refractómetro?\nEs un instrumento que mide cuánto se desvía (refracta) la luz al pasar por un líquido.\nCuantos más sólidos disueltos (azúcar) tenga el líquido, más lento viaja la luz y más se dobla.\n\n¿Qué son los Grados Brix (°Bx)?\nEs la unidad de medida. 1°Bx ≈ 1 gramo de sacarosa en 100g de solución.\n------------------------------------------")

opciones_format = {f"{k}. {v['nombre']}": k for k, v in bebidas.items()}
eleccion_texto = st.selectbox("Selecciona una muestra para analizar:", list(opciones_format.keys()))
opcion = opciones_format[eleccion_texto]

if st.button("Iniciar Procedimiento"):
    bebida = bebidas[opcion]
    espacio_mensajes = st.empty()
    
    with espacio_mensajes.container():
        st.write(f"**🧪 HAS SELECCIONADO: {bebida['nombre']}**")
        st.write("Iniciando procedimiento estándar...")
        time.sleep(1)

        pasos = [
            "1. Levantar la placa de iluminación del prisma.",
            "2. Limpiar el prisma con agua destilada y secar con paño suave (Calibración).",
            f"3. Colocar 2-3 gotas de '{bebida['nombre']}' sobre el prisma principal.",
            "4. Cerrar la placa suavemente para evitar burbujas de aire.",
            "5. Mirar a través del ocular apuntando hacia una fuente de luz..."
        ]

        for paso in pasos:
            st.write(paso)
            time.sleep(1.5)

        st.write("\n**👁️ GENERANDO VISTA DEL OCULAR...**")
        time.sleep(1)
        
    graficar_vista_refractometro(bebida['brix'], bebida['nombre'])

    valor_brix = bebida['brix']
    st.write(f"\n✅ **RESULTADO FINAL:** La muestra tiene {valor_brix} °Brix.")
    if valor_brix > 10:
        st.warning("⚠️ Es una bebida con alto contenido de azúcar.")
    elif valor_brix == 0:
        st.info("💧 No contiene azúcar (o es indetectable).")
    else:
        st.success("👍 Contenido de azúcar moderado.")
