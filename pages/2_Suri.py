import streamlit as st
import streamlit.components.v1 as components

# --- TÍTULO DE AUTORÍA ---
st.title("Simulación de Suri Espinoza Rangel")

codigo_refractometro = """
<div style="font-family: 'Segoe UI', sans-serif; max-width: 500px; margin: auto; background-color: #f4f4f9; padding: 20px; border-radius: 15px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); text-align: center;">

    <h2 style="color: #333; margin-bottom: 5px;">🔬 Refractómetro Digital</h2>
    <p style="color: #666; font-size: 14px; margin-top: 0;">Mide los gramos de azúcar por cada 100 ml</p>

    <select id="menu_bebidas" style="width: 80%; padding: 10px; font-size: 16px; border-radius: 8px; border: 1px solid #ccc; margin-bottom: 15px; cursor: pointer;">
        <option value="" disabled selected>Selecciona una bebida...</option>
        <option value="0.0">💧 Agua (0g)</option>
        <option value="0.4">🥤 Prime Hydration (0.4g)</option>
        <option value="5.0">🥛 Leche Entera (5g)</option>
        <option value="6.0">⚡ Gatorade (6g)</option>
        <option value="7.0">🧃 Té Helado (7g)</option>
        <option value="9.0">🍋 Sprite (9g)</option>
        <option value="9.0">🍊 Jugo de Naranja Natural (9g)</option>
        <option value="10.0">🍎 Sidral Mundet (10g)</option>
        <option value="10.5">🟠 Fanta (10.5g)</option>
        <option value="10.6">🥤 Coca Cola (10.6g)</option>
        <option value="11.0">🔋 Monster Energy (11g)</option>
        <option value="11.0">🐂 Red Bull (11g)</option>
        <option value="16.0">🍼 Yakult (16g)</option>
    </select>

    <br>

    <button id="boton_medir" style="background-color: #007BFF; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 8px; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 6px rgba(0,123,255,0.3);">
        🔍 Medir Azúcar
    </button>

    <div style="display: flex; justify-content: center; align-items: flex-end; margin-top: 30px; height: 250px;">

        <div style="display: flex; flex-direction: column; justify-content: space-between; height: 100%; margin-right: 10px; font-size: 12px; color: #555; font-weight: bold; text-align: right;">
            <span>20g -</span>
            <span>15g -</span>
            <span>10g -</span>
            <span>5g -</span>
            <span>0g -</span>
        </div>

        <div style="width: 60px; height: 100%; background-color: #e0e0e0; border-radius: 10px; border: 3px solid #ccc; position: relative; overflow: hidden; box-shadow: inset 0 0 10px rgba(0,0,0,0.1);">
            <div id="liquido" style="width: 100%; height: 0%; background: linear-gradient(to top, #4facfe 0%, #00f2fe 100%); position: absolute; bottom: 0; transition: height 1s cubic-bezier(0.25, 0.8, 0.25, 1);"></div>
        </div>
    </div>

    <div id="pantalla_resultado" style="margin-top: 20px; font-size: 24px; font-weight: bold; color: #333; background-color: #fff; padding: 10px; border-radius: 8px; border: 1px solid #ddd;">
        0.0 g / 100ml
    </div>

</div>

<script>
    const boton = document.getElementById('boton_medir');
    const menu = document.getElementById('menu_bebidas');
    const liquido = document.getElementById('liquido');
    const pantalla = document.getElementById('pantalla_resultado');

    boton.addEventListener('click', () => {
        const azucar = parseFloat(menu.value);

        if (isNaN(azucar)) {
            pantalla.innerText = "¡Selecciona una bebida!";
            return;
        }

        const maxAzucarEscala = 20.0;
        let porcentajeAltura = (azucar / maxAzucarEscala) * 100;

        if (porcentajeAltura > 100) porcentajeAltura = 100;

        liquido.style.height = porcentajeAltura + '%';
        pantalla.innerHTML = `<span style="color: #007BFF;">${azucar.toFixed(1)} g</span> de azúcar`;
    });
</script>
"""

# Renderizamos su código web original dentro de Streamlit
components.html(codigo_refractometro, height=550)
