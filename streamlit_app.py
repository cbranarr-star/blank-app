import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Cristian Bran — Portafolio", layout="wide")

# CSS personalizado que replica tu diseño original
st.markdown("""
<style>
    :root { --ink: #0B0F1A; --signal: #4FD9C6; --panel: #121A2B; --paper: #E9EDF5; --line: #26314A; }
    .stApp { background-color: var(--ink); color: var(--paper); }
    
    /* Animación de botones */
    .btn {
        padding: 13px 22px; border-radius: 2px; text-decoration: none; 
        transition: transform .2s, background .2s; display: inline-block;
        font-family: 'IBM Plex Mono', monospace; font-weight: 600;
    }
    .btn-primary { background: var(--signal); color: #04201C; }
    .btn:hover { transform: translateY(-5px); cursor: pointer; }
    
    /* Tarjetas con movimiento */
    .card {
        background: var(--panel); border: 1px solid var(--line); 
        padding: 22px; transition: transform 0.3s ease;
    }
    .card:hover { transform: translateY(-10px); border-color: var(--signal); }
    
    /* Animación de entrada */
    .reveal { opacity: 0; transform: translateY(20px); transition: all 0.6s ease-out; }
    .in { opacity: 1; transform: translateY(0); }
</style>
""", unsafe_allow_html=True)

# Contenido del Portafolio
st.title("Cristian Bran")
st.subheader("Construye puentes entre redes, datos e IA.")

st.markdown("""
<div class="reveal">
    <p>Ingeniero en Telecomunicaciones y Analista de Inteligencia de Negocios en Savia Salud EPS.</p>
</div>
""", unsafe_allow_html=True)

# Botones con estilo
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown('<a href="#trayectoria" class="btn btn-primary">Trayectoria</a>', unsafe_allow_html=True)

st.divider()

# Sección de Trayectoria con efecto
st.header("Trayectoria Profesional")
experiencia = [
    ("Analista de Inteligencia de Negocios", "Savia Salud EPS", "02/2025 - Presente"),
    ("Analista de Infraestructura", "Savia Salud EPS", "05/2023 - 02/2025"),
    ("Agente Mesa de Servicios", "Savia Salud EPS", "05/2022 - 03/2023")
]

for rol, org, fecha in experiencia:
    st.markdown(f"""
    <div class="card reveal">
        <h3>{rol}</h3>
        <p style="color:var(--signal)">{org}</p>
        <small>{fecha}</small>
    </div>
    <br>
    """, unsafe_allow_html=True)

# Script para animar la aparición de elementos al hacer scroll
st.markdown("""
<script>
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('in');
        });
    });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
</script>
""", unsafe_allow_html=True)
