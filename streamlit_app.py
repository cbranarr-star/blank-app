import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuración de página
st.set_page_config(page_title="Portafolio - Cristian Camilo Bran Arriaga", layout="wide")

# Función para cargar animación Lottie
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

# CSS personalizado para efectos de movimiento (Hover)
st.markdown("""
<style>
    .card {
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        padding: 20px;
        border-radius: 15px;
        background: #fdfdfd;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }
    .card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 25px rgba(0,0,0,0.1);
    }
    .btn-linkedin {
        background-color: #0077b5; 
        color: white; 
        padding: 10px 20px; 
        border-radius: 5px; 
        text-decoration: none; 
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Carga de animación
lottie_data = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")

# Cabecera
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Cristian Camilo Bran Arriaga")
    st.subheader("Ingeniero en Telecomunicaciones | Especialista en Big Data e Inteligencia de Negocios")
    st.write("Profesional enfocado en infraestructura tecnológica, mesa de servicios y análisis estratégico de datos.")
with col2:
    if lottie_data:
        st_lottie(lottie_data, height=200)

st.divider()

# Sección de Experiencia
st.header("Experiencia Profesional")
experiencias = [
    ("Savia Salud EPS", "Practicante de infraestructura y Agente mesa de servicios. Soporte nivel 1/2, gestión de tickets, monitoreo de red y optimización de plataformas de salud[cite: 4]."),
    ("Comware", "Analista de mesa de fibra óptica. Soporte a red MPLS, monitoreo y gestión en plataformas como BMC Remedy e iMaster NCE[cite: 4]."),
    ("Supplies", "Analista nivel 1. Soporte técnico, mantenimiento de hardware, inventarios y gestión de VPN/Antivirus[cite: 4]."),
    ("Teleperformance", "Agente soporte técnico nivel 1. Solución de problemas de navegación para clientes internacionales[cite: 4].")
]

for titulo, desc in experiencias:
    st.markdown(f'<div class="card"><h4>{titulo}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

# Sección de Formación
st.divider()
st.header("Formación Académica")
st.markdown("""
- **Especialista en Big Data e Inteligencia de Negocios** - Universidad Católica Luis Amigó (2026)[cite: 2, 6].
- **Ingeniero en Telecomunicaciones** - Politécnico Grancolombiano[cite: 3].
- **Tecnólogo en Gestión de Redes de Datos** - SENA[cite: 4].
- **Técnico en Sistemas** - SENA[cite: 4].
""")

# Sección de contacto
st.divider()
st.subheader("Contacto")
col_c1, col_c2, col_c3 = st.columns(3)

with col_c1:
    st.write("📍 Medellín, Colombia")
with col_c2:
    st.write("📧 ccbran1998@hotmail.com")
with col_c3:
    st.markdown("""
    <a href="https://www.linkedin.com/in/cristian-camilo-bran-arriaga-b1074730b" target="_blank" class="btn-linkedin">
        LinkedIn
    </a>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Desarrollado para transformar datos en valor estratégico.")
