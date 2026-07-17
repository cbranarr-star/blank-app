import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuración de página
st.set_page_config(page_title="Portafolio - Cristian Bran", layout="wide")

# Función segura para cargar animaciones
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=10)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# CSS personalizado para diseño profesional
st.markdown("""
<style>
    :root { --ink: #0B0F1A; --signal: #4FD9C6; --panel: #121A2B; --paper: #E9EDF5; --line: #26314A; }
    .stApp { background-color: var(--ink); color: var(--paper); }
    .card { background: var(--panel); border: 1px solid var(--line); padding: 22px; margin-bottom: 20px; border-radius: 4px; transition: transform 0.3s ease; }
    .card:hover { transform: translateY(-5px); border-color: var(--signal); }
    .btn { padding: 13px 22px; border-radius: 2px; text-decoration: none; font-weight: 600; display: inline-block; cursor: pointer; color: #04201C !important; }
    .btn-primary { background: var(--signal); }
</style>
""", unsafe_allow_html=True)

# Cabecera
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Cristian Bran")
    st.subheader("Construye puentes entre redes, datos e IA.")
    st.write("Ingeniero en Telecomunicaciones y Analista de Inteligencia de Negocios. Transformando infraestructura en decisiones estratégicas[cite: 4].")
    st.markdown('<a href="#trayectoria" class="btn btn-primary">Ver trayectoria</a>', unsafe_allow_html=True)

with col2:
    lottie_data = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfwnrgu.json")
    if lottie_data:
        st_lottie(lottie_data, height=200, key="coding")

st.divider()

# Sección de Trayectoria
st.header("Trayectoria Profesional")
trayectoria = [
    ("Analista de Inteligencia de Negocios", "Savia Salud EPS", "02/2025 – Presente", "Generación de informes estratégicos, queries en MySQL/MariaDB, scripts en Python para cruces de datos y tableros en Power BI[cite: 4]."),
    ("Analista de Infraestructura", "Savia Salud EPS", "05/2023 – 02/2025", "Escalamientos de fallas, monitoreo de recursos, administración de AD, migración a la nube y manejo de VPN Fortigate[cite: 4]."),
    ("Agente Mesa de Servicios", "Savia Salud EPS", "05/2022 – 03/2023", "Soporte técnico, diagnóstico de red, administración de Google Workspace y seguimiento de tickets[cite: 4]."),
    ("Analista Nivel 1", "Supplies", "11/2021 – 02/2022", "Soporte técnico a equipos, mantenimiento preventivo/correctivo, diagnóstico de cableado e instalación de VPN/antivirus[cite: 4]."),
    ("Analista Mesa de Servicios", "Comware", "06/2019 – 04/2021", "Soporte telefónico a técnicos en sitio sobre red MPLS, manejo de BMC Remedy, iMaster NCE y Siebel[cite: 4]."),
    ("Agente de Soporte Técnico", "Teleperformance", "06/2018 – 05/2019", "Atención al cliente internacional para resolución de problemas de navegación en hogares[cite: 4].")
]

for rol, org, fecha, desc in trayectoria:
    st.markdown(f"""
    <div class="card">
        <h3>{rol}</h3>
        <p style="color:var(--signal)"><strong>{org}</strong> | {fecha}</p>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de contacto
st.divider()
st.header("Contacto")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    st.write("📍 **Ubicación:** Medellín, Colombia")
with col_c2:
    st.write("📧 **Correo:** ccbran1998@hotmail.com")
with col_c3:
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/cristian-camilo-bran-arriaga-b1074730b)")

st.write("📱 **Teléfono:** +57 314 613 9747")

# Nota técnica
st.divider()
st.markdown("""
<div class="card" style="border-top: 2px solid var(--signal);">
    <h4>// Nota técnica sobre el sitio</h4>
    <p>Este sitio ha sido desarrollado íntegramente utilizando un stack de <strong>Python y Streamlit</strong>[cite: 1, 2].<br>
    <strong>Stack:</strong> HTML5, CSS3, JS, Streamlit Framework.<br>
    <strong>Última actualización:</strong> Julio 2026.</p>
</div>
""", unsafe_allow_html=True)
