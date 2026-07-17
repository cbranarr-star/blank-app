import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuración de página
st.set_page_config(page_title="Cristian Bran | Portfolio", layout="wide", page_icon="💻")

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
    
    /* Tarjetas con efecto glassmorphism */
    .glass-card { 
        background: var(--panel-glass); backdrop-filter: blur(10px); 
        border: 1px solid rgba(255,255,255,0.1); padding: 30px; 
        border-radius: 16px; margin-bottom: 20px; transition: 0.3s;
    }
    .glass-card:hover { border-color: var(--signal); transform: translateY(-5px); }
    
    /* Tipografía y Botones */
    h1, h2, h3 { color: #ffffff !important; }
    .btn-custom { 
        padding: 10px 20px; border-radius: 8px; border: 1px solid var(--signal);
        background: transparent; color: var(--signal); text-decoration: none;
        font-weight: bold; transition: 0.3s;
    }
    .btn-custom:hover { background: var(--signal); color: var(--ink); }
    
    .eyebrow { color: var(--signal); font-family: monospace; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 1. HERO SECTION
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<p class="eyebrow">Ingeniero & Analista de Datos</p>', unsafe_allow_html=True)
    st.title("Cristian Bran")
    st.write("### Construyendo puentes entre redes, datos e IA.")
    st.write("Transformo infraestructura compleja en decisiones estratégicas mediante Big Data y automatización.")
with col2:
    lottie = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfwnrgu.json")
    if lottie: st_lottie(lottie, height=200)

st.divider()

# 2. PERFIL PROFESIONAL
st.header("Perfil Profesional")
st.markdown("""
<div class="glass-card">
    <p>Profesional versátil en el sector TI, con más de 6 años de experiencia gestionando infraestructura crítica y liderando procesos de Inteligencia de Negocios (BI). 
    Especialista en convertir datos sin procesar en dashboards accionables. Actualmente enfocado en aplicar IA generativa y automatización para optimizar la toma de decisiones corporativas.</p>
</div>
""", unsafe_allow_html=True)

# 3. DASHBOARDS (Power BI / Looker Studio)
st.header("Proyectos & Dashboards")
st.write("Muestras de mi capacidad analítica y visualización de datos.")

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="glass-card">
        <h3>Power BI Dashboard</h3>
        <p>Análisis de métricas de salud y riesgo.</p>
        <a href="URL_DE_TU_POWERBI" target="_blank" class="btn-custom">Ver Proyecto</a>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-card">
        <h3>Looker Studio</h3>
        <p>Automatización de reportes de infraestructura.</p>
        <a href="URL_DE_TU_LOOKER" target="_blank" class="btn-custom">Ver Proyecto</a>
    </div>
    """, unsafe_allow_html=True)

# 4. TRAYECTORIA
st.header("Trayectoria")
# (Aquí puedes mantener tu lista anterior de trayectoria dentro de glass-cards)
st.markdown('<div class="glass-card">Experiencia detallada en infraestructura, BI y soporte técnico.</div>', unsafe_allow_html=True)

# 5. CONTACTO
st.divider()
st.header("Hablemos")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: st.write("📍 Medellín, Colombia")
with col_c2: st.write("📧 ccbran1998@hotmail.com")
with col_c3: st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/cristian-camilo-bran-arriaga-b1074730b)")
