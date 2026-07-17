import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuración de página
st.set_page_config(page_title="Cristian Camilo Bran Arriaga | Portfolio", layout="wide", page_icon="💻")

def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=10)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# CSS Estilo Moderno (Framer-like)
st.markdown("""
<style>
    :root { --ink: #0B0F1A; --signal: #4FD9C6; --panel: #121A2B; --panel-glass: rgba(18, 26, 43, 0.7); --paper: #E9EDF5; }
    .stApp { background-color: var(--ink); color: var(--paper); }
    .glass-card { background: var(--panel-glass); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 16px; margin-bottom: 20px; transition: 0.3s; }
    .glass-card:hover { border-color: var(--signal); transform: translateY(-5px); }
    h1, h2, h3 { color: #ffffff !important; }
    .btn-custom { padding: 10px 20px; border-radius: 8px; border: 1px solid var(--signal); background: transparent; color: var(--signal); text-decoration: none; font-weight: bold; transition: 0.3s; }
    .btn-custom:hover { background: var(--signal); color: var(--ink); }
    .eyebrow { color: var(--signal); font-family: monospace; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 1. HEADER
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<p class="eyebrow">Ingeniero & Especialista BI</p>', unsafe_allow_html=True)
    st.title("Cristian Bran")
    st.write("### Construyendo puentes entre redes, datos e IA.")
    st.write("Ingeniero en Telecomunicaciones con +6 años de experiencia en TI, infraestructura y BI.")
with col2:
    lottie = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfwnrgu.json")
    if lottie: st_lottie(lottie, height=200)

# 2. PERFIL PROFESIONAL
st.header("Perfil Profesional")
st.markdown("""
<div class="glass-card">
    <p>Ingeniero en Telecomunicaciones con más de 6 años de experiencia técnica transformando infraestructuras críticas en activos de inteligencia. Mi carrera ha evolucionado desde la gestión de redes y soporte N2 hacia la arquitectura de datos y Business Intelligence. Especialista en convertir flujos complejos de información en tableros estratégicos (Power BI) y soluciones automatizadas (Python, Airflow). Comprometido con la innovación, integro herramientas de Inteligencia Artificial para optimizar procesos operativos y potenciar la toma de decisiones basada en datos.</p>
</div>
""", unsafe_allow_html=True)

# 3. PROYECTOS (Dashboards)
st.header("Proyectos & Dashboards")
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    <div class="glass-card">
        <h3>Power BI</h3>
        <p>Dashboard de gestión de salud y riesgos.</p>
        <a href="#" class="btn-custom">Ver en Power BI</a>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class="glass-card">
        <h3>Looker Studio</h3>
        <p>Automatización de métricas de infraestructura.</p>
        <a href="#" class="btn-custom">Ver en Looker</a>
    </div>
    """, unsafe_allow_html=True)

# 4. TRAYECTORIA COMPLETA
st.header("Trayectoria")
trayectoria = [
    ("Analista de Inteligencia de Negocios", "Savia Salud EPS", "02/2025 – Presente", "Generación de informes estratégicos, queries en MySQL/MariaDB, scripts en Python, tableros en Power BI, gestión de GitHub, Trello y Airflow[cite: 1]."),
    ("Analista de Infraestructura", "Savia Salud EPS", "05/2023 – 02/2025", "Escalamientos, monitoreo de servidores, AD, migración a nube, DRP, VPN Fortigate[cite: 1]."),
    ("Agente Mesa de Servicios", "Savia Salud EPS", "05/2022 – 03/2023", "Soporte técnico, diagnóstico de red HFC/FTT, tableros BI, Google Workspace[cite: 1]."),
    ("Analista Nivel 1", "Supplies", "11/2021 – 02/2022", "Mantenimiento correctivo/preventivo, cableado, instalación de software corporativo, manejo de tickets[cite: 1]."),
    ("Analista Mesa de Servicios", "Comware", "06/2019 – 04/2021", "Soporte a red MPLS (Tigo-Une), monitoreo topologías anillo/bus, manejo de BMC Remedy, iMaster NCE[cite: 1]."),
    ("Agente de Soporte Técnico", "Teleperformance", "06/2018 – 05/2019", "Resolución de problemas de navegación para clientes internacionales Orange y Jazztel[cite: 1].")
]

for rol, org, fecha, desc in trayectoria:
    st.markdown(f"""
    <div class="glass-card">
        <h4>{rol}</h4>
        <p style="color:var(--signal)"><strong>{org}</strong> | {fecha}</p>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# 5. CONTACTO
st.divider()
st.header("Contacto")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: st.write("📍 Medellín, Colombia")
with col_c2: st.write("📧 ccbran1998@hotmail.com")
with col_c3: st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/cristian-camilo-bran-arriaga-b1074730b)")
