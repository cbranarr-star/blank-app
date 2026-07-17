import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuración de página
st.set_page_config(page_title="Portafolio - Cristian Bran", layout="wide")

# Función para cargar animación Lottie
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

# CSS personalizado para efectos de movimiento y diseño
st.markdown("""
<style>
    :root { --ink: #0B0F1A; --signal: #4FD9C6; --panel: #121A2B; --paper: #E9EDF5; --line: #26314A; }
    .stApp { background-color: var(--ink); color: var(--paper); }
    
    .card {
        background: var(--panel); border: 1px solid var(--line); 
        padding: 22px; transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 20px; border-radius: 4px;
    }
    .card:hover { transform: translateY(-10px) scale(1.02); border-color: var(--signal); }
    
    .btn {
        padding: 13px 22px; border-radius: 2px; text-decoration: none; 
        transition: transform .2s, background .2s; display: inline-block;
        font-family: 'monospace'; font-weight: 600; cursor: pointer;
    }
    .btn-primary { background: var(--signal); color: #04201C; }
    
    .reveal { opacity: 0; transform: translateY(20px); transition: all 0.6s ease-out; }
    .in { opacity: 1; transform: translateY(0); }
</style>
""", unsafe_allow_html=True)

# Cabecera con Animación Lottie
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Cristian Bran")
    st.subheader("Construye puentes entre redes, datos e IA.")
    st.write("Ingeniero en Telecomunicaciones y Analista de Inteligencia de Negocios. Transformando infraestructura en decisiones estratégicas[cite: 4].")
    st.markdown('<a href="#trayectoria" class="btn btn-primary">Ver trayectoria</a>', unsafe_allow_html=True)

with col2:
    lottie_data = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfwnrgu.json")
    st_lottie(lottie_data, height=200)

st.divider()

# Sección de Trayectoria
st.header("Trayectoria Profesional")
experiencias = [
    ("Analista de Inteligencia de Negocios", "Savia Salud EPS", "Generación de informes estratégicos y automatización con Python y Power BI."),
    ("Analista de Infraestructura", "Savia Salud EPS", "Gestión de servidores, redes MPLS y administración de VPN Fortigate[cite: 4]."),
    ("Agente Mesa de Servicios", "Comware", "Soporte especializado a redes MPLS y monitoreo en plataformas BMC Remedy[cite: 4].")
]

for titulo, org, desc in experiencias:
    st.markdown(f"""
    <div class="card reveal">
        <h3>{titulo}</h3>
        <p style="color:var(--signal)">{org}</p>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de Nota Técnica
st.divider()
st.markdown("""
<div class="card reveal" style="border-top: 2px solid var(--signal);">
    <h4>// Nota técnica sobre el sitio</h4>
    <p>Este sitio ha sido desarrollado íntegramente por mí utilizando un stack de <strong>Python y Streamlit</strong>[cite: 1, 2].<br>
    <strong>Stack:</strong> HTML5, CSS3, JS, Streamlit Framework.<br>
    <strong>Última actualización:</strong> Julio 2026.</p>
</div>
""", unsafe_allow_html=True)

# Script de animación al hacer scroll
st.markdown("""
<script>
    const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('in'); });
    });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
</script>
""", unsafe_allow_html=True)
