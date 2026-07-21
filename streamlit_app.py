import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

# ────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cristian Camilo Bran Arriaga | Portafolio",
    layout="wide",
    page_icon="💻",
)


def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=10)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


# ────────────────────────────────────────────────────────────
# ESTILOS
# ────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
    :root {
        --ink: #0B0F1A; --signal: #4FD9C6; --amber: #F0A857;
        --panel: #121A2B; --panel-glass: rgba(18, 26, 43, 0.7);
        --paper: #E9EDF5; --muted: #8892A6;
    }
    .stApp { background-color: var(--ink); color: var(--paper); }
    h1, h2, h3, h4 { color: #ffffff !important; }

    .glass-card {
        background: var(--panel-glass); backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1); padding: 26px 28px;
        border-radius: 14px; margin-bottom: 18px; transition: 0.25s;
    }
    .glass-card:hover { border-color: var(--signal); transform: translateY(-3px); }

    .eyebrow {
        color: var(--signal); font-family: monospace; text-transform: uppercase;
        letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 8px;
    }
    .tag {
        display:inline-block; font-family: monospace; font-size: 0.72rem;
        color: var(--ink); background: var(--signal); padding: 3px 10px;
        border-radius: 20px; margin-bottom: 10px; font-weight:700;
    }
    .tag.amber { background: var(--amber); }
    .org { color: var(--signal); font-weight: 700; }
    .muted { color: var(--muted); font-size: 0.85rem; }

    .stButton>button {
        background: transparent; border: 1px solid var(--signal); color: var(--signal);
        border-radius: 8px; padding: 8px 20px; font-weight: 600; width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover { background: var(--signal); color: var(--ink); border-color: var(--signal); }
    .stButton>button:focus { box-shadow: 0 0 0 2px rgba(79,217,198,0.4); }

    .stat-box {
        background: var(--panel-glass); border-left: 3px solid var(--signal);
        padding: 14px 18px; border-radius: 6px;
    }
    .stat-box .num { font-family: monospace; font-size: 1.6rem; font-weight: 700; color: #fff; }
    .stat-box .lbl { color: var(--muted); font-size: 0.8rem; text-transform: uppercase; }

    .dash-slot {
        border: 1px dashed rgba(255,255,255,0.25); border-radius: 12px;
        padding: 18px; background: var(--panel-glass);
    }
</style>
""",
    unsafe_allow_html=True,
)

# ────────────────────────────────────────────────────────────
# DATOS (edítalos aquí una sola vez)
# ────────────────────────────────────────────────────────────
EXPERIENCIA = {
    "Inteligencia de Negocios": {
        "icono": "📊",
        "periodo": "2025 – hoy",
        "items": [
            (
                "Analista de Inteligencia de Negocios",
                "Savia Salud EPS",
                "02/2025 – Presente",
                "Genero informes estandarizados y personalizados sobre datos de la organización "
                "(cuentas médicas, autorizaciones, MIPRES, riesgo en salud, PQRS, tutelas). Creo "
                "queries para MySQL y MariaDB, scripts en Python para cruces de datos, y tableros "
                "estratégicos y operativos en Power BI. Apoyo la extracción de información para "
                "entes de control y manejo GitHub, Trello y Airflow.",
            ),
        ],
    },
    "Infraestructura": {
        "icono": "🖥️",
        "periodo": "2022 – 2025",
        "items": [
            (
                "Analista de Infraestructura",
                "Savia Salud EPS",
                "05/2023 – 02/2025",
                "Escalamientos de fallas de servidores con el proveedor Tigo, monitoreo y ampliación "
                "de recursos, administración de AD, migración de servidores a la nube, tableros en "
                "Power BI, DRP, informes mensuales de disponibilidad y manejo de VPN Fortigate.",
            ),
            (
                "Agente Mesa de Servicios",
                "Savia Salud EPS",
                "05/2022 – 03/2023",
                "Recepción de solicitudes vía chat, correo y teléfono, soporte técnico y diagnóstico "
                "de red HFC/FTT, escalamientos N2, creación de tableros en Power BI, administración "
                "de Google Workspace y seguimiento de tickets.",
            ),
        ],
    },
    "Soporte & Redes": {
        "icono": "🌐",
        "periodo": "2018 – 2022",
        "items": [
            (
                "Analista Nivel 1",
                "Supplies",
                "11/2021 – 02/2022",
                "Soporte técnico a equipos portátiles y de escritorio, mantenimiento correctivo y "
                "preventivo, diagnóstico de cableado interno, instalación de sistema operativo y "
                "de VPN/antivirus.",
            ),
            (
                "Analista Mesa de Servicios",
                "Comware",
                "06/2019 – 04/2021",
                "Soporte telefónico a técnicos en sitio sobre aperturas en la red MPLS de Tigo-Une "
                "(topologías en anillo y bus), instalación y retiro de servicios, y manejo de BMC "
                "Remedy, Fénix ATC, Service Desk, iMaster NCE y Siebel.",
            ),
            (
                "Agente de Soporte Técnico",
                "Teleperformance",
                "06/2018 – 05/2019",
                "Atención al cliente para resolver casos de navegación de internet en hogares y "
                "líneas móviles internacionales Orange y Jazztel.",
            ),
        ],
    },
}

FORMACION_ACADEMICA = [
    ("Especialista en Big Data e BI", "02/2025 – 01/2026"),
    ("Ingeniero en Telecomunicaciones", "02/2021 – 07/2023"),
    ("Tecnólogo en Gestión de Redes de Datos", "01/2016 – 04/2018"),
    ("Técnico en Sistemas", "01/2014 – 12/2015"),
]

CERTIFICACIONES_2026 = [
    ("Crear valor con IA, automatización y bots", "02/07/2026", "2 h · 2 módulos", "Automatización"),
    ("Gen AI Intermedio — AWS Entrena Colombia / TIDWIT", "30/06/2026", "4 h 09 min", "IA generativa"),
    ("Publicidad digital: datos, IA y legalidad", "25/05/2026", "8 h · 2 módulos", "IA & Legalidad"),
    ("Introducción a la Ciencia de Datos", "07/01/2026", "6 h · 2 módulos", "Ciencia de datos"),
    ("Domina la IA con Gemini", "05/01/2026", "2 h · 2 módulos", "IA generativa"),
]

# ────────────────────────────────────────────────────────────
# NAVEGACIÓN POR BOTONES
# ────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Inicio"

PAGES = ["Inicio", "Experiencia", "Formación & Cursos", "Dashboards", "Contacto"]

nav_cols = st.columns(len(PAGES))
for col, page_name in zip(nav_cols, PAGES):
    with col:
        if st.button(page_name, use_container_width=True, key=f"nav_{page_name}"):
            st.session_state.page = page_name

st.markdown("<br>", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────
# PÁGINA: INICIO
# ────────────────────────────────────────────────────────────
if st.session_state.page == "Inicio":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<p class="eyebrow">Ingeniero en Telecomunicaciones & Especialista BI</p>', unsafe_allow_html=True)
        st.title("Cristian Camilo Bran Arriaga")
        st.write("### Construyendo puentes entre redes, datos e inteligencia artificial.")
    with col2:
        lottie = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfwnrgu.json")
        if lottie:
            st_lottie(lottie, height=180)

    st.markdown("#### Resumen profesional")
    st.markdown(
        """
    <div class="glass-card">
        <p>Soy un profesional versátil, con más de <strong>6 años de experiencia continua en tecnología</strong>,
        que ha construido su carrera subiendo capas: primero sostuve la infraestructura que hace posible que
        los sistemas funcionen (redes, servidores, mesas de servicio), luego pasé a interpretar los datos que
        esos sistemas generan, y desde 2026 sumé inteligencia artificial aplicada a ese mismo stack.</p>
        <p>Empecé en soporte técnico y redes MPLS (Comware, Teleperformance), pasé por mantenimiento de
        equipos e infraestructura (Supplies, Savia Salud EPS) y hoy trabajo como <strong>Analista de
        Inteligencia de Negocios en Savia Salud EPS</strong>, generando informes estratégicos sobre cuentas
        médicas, autorizaciones, riesgo en salud y PQRS. Uso SQL (MySQL/MariaDB), Python para cruces de
        datos, y construyo tableros estratégicos y operativos en Power BI.</p>
        <p>En paralelo completé una <strong>especialización en Big Data e BI</strong> (2025–2026) y cinco
        certificaciones aplicadas de IA en 2026 — desde IA generativa con Gemini hasta ciencia de datos,
        automatización con bots y el marco legal de la IA en publicidad digital. Me caracteriza la facilidad
        para el trabajo en equipo y el entusiasmo por seguir aprendiendo y aportar lo mejor de mí en cada
        entorno.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("#### En números")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown('<div class="stat-box"><div class="num">6+</div><div class="lbl">Años en TI</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="stat-box"><div class="num">6</div><div class="lbl">Roles ocupados</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="stat-box"><div class="num">5</div><div class="lbl">Certificaciones IA 2026</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="stat-box"><div class="num">SAVIA</div><div class="lbl">Rol actual: Analista BI</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Usa los botones de arriba para explorar mi **experiencia segmentada**, mi **formación y cursos**, y algunos **tableros** que he construido.")

# ────────────────────────────────────────────────────────────
# PÁGINA: EXPERIENCIA (segmentada por etapa)
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Experiencia":
    st.markdown('<p class="eyebrow">Trayectoria profesional</p>', unsafe_allow_html=True)
    st.title("Experiencia, por etapa")
    st.write("Seis roles agrupados en tres etapas de especialización creciente. Selecciona una pestaña para explorar cada una.")

    tabs = st.tabs([f"{v['icono']} {k}  ·  {v['periodo']}" for k, v in EXPERIENCIA.items()])
    for tab, (etapa, data) in zip(tabs, EXPERIENCIA.items()):
        with tab:
            for rol, org, fecha, desc in data["items"]:
                st.markdown(
                    f"""
                <div class="glass-card">
                    <span class="tag">{fecha}</span>
                    <h4>{rol}</h4>
                    <p class="org">{org}</p>
                    <p>{desc}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

# ────────────────────────────────────────────────────────────
# PÁGINA: FORMACIÓN & CURSOS (segmentada)
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Formación & Cursos":
    st.markdown('<p class="eyebrow">Formación continua</p>', unsafe_allow_html=True)
    st.title("Formación académica y certificaciones")
    st.write("Dos bloques: la base académica formal, y las certificaciones de IA/datos completadas en 2026.")

    tab_edu, tab_cert = st.tabs(["🎓 Formación académica", "🤖 Certificaciones IA · 2026"])

    with tab_edu:
        for titulo, periodo in FORMACION_ACADEMICA:
            st.markdown(
                f"""
            <div class="glass-card">
                <span class="tag amber">{periodo}</span>
                <h4>{titulo}</h4>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with tab_cert:
        c1, c2 = st.columns(2)
        for i, (titulo, fecha, duracion, categoria) in enumerate(CERTIFICACIONES_2026):
            target = c1 if i % 2 == 0 else c2
            with target:
                st.markdown(
                    f"""
                <div class="glass-card">
                    <span class="tag">{categoria}</span>
                    <h4>{titulo}</h4>
                    <p class="muted">📅 {fecha} &nbsp;·&nbsp; ⏱️ {duracion}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

# ────────────────────────────────────────────────────────────
# PÁGINA: DASHBOARDS (espacios para Power BI y Looker Studio)
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Dashboards":
    st.markdown('<p class="eyebrow">Proyectos aplicados</p>', unsafe_allow_html=True)
    st.title("Tableros y visualizaciones")
    st.write(
        "Espacios listos para incrustar tus tableros públicos de Power BI y Looker Studio. "
        "Reemplaza el `src` de cada iframe por el enlace **'Publicar en la web'** de tu tablero."
    )

    col_pbi, col_looker = st.columns(2)

    with col_pbi:
        st.markdown("#### 📊 Power BI")
        st.markdown('<div class="dash-slot">', unsafe_allow_html=True)
        # Reemplaza la URL de abajo por el enlace de publicación de tu informe de Power BI
        components.iframe(
            src="https://app.powerbi.com/view?r=REEMPLAZA_CON_TU_ENLACE_DE_PUBLICACION",
            height=400,
        )
        st.caption("Ejemplo: dashboard de gestión de cuentas médicas y riesgo en salud.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_looker:
        st.markdown("#### 📈 Looker Studio (Data Studio)")
        st.markdown('<div class="dash-slot">', unsafe_allow_html=True)
        # Reemplaza la URL de abajo por el enlace "insertar informe" de tu Looker Studio
        components.iframe(
            src="https://lookerstudio.google.com/embed/reporting/REEMPLAZA_CON_TU_ID/page/1",
            height=400,
        )
        st.caption("Ejemplo: automatización de métricas de infraestructura y disponibilidad.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.warning(
        "💡 Si el iframe aparece en blanco, revisa que el informe esté publicado como **público** "
        "(Power BI → *Publicar en la web*; Looker Studio → *Compartir → Insertar informe*)."
    )

# ────────────────────────────────────────────────────────────
# PÁGINA: CONTACTO
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Contacto":
    st.markdown('<p class="eyebrow">Contacto</p>', unsafe_allow_html=True)
    st.title("Hablemos")
    st.write("Abierto a conversar sobre roles en BI, datos, infraestructura o proyectos donde la IA aplicada sume valor.")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="glass-card">📍 <strong>Ubicación</strong><br>Medellín, Colombia</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="glass-card">📧 <strong>Correo</strong><br><a href="mailto:ccbran1998@hotmail.com" style="color:var(--signal);">ccbran1998@hotmail.com</a></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="glass-card">🔗 <strong>LinkedIn</strong><br><a href="https://www.linkedin.com/in/cristian-camilo-bran-arriaga-b1074730b" style="color:var(--signal);" target="_blank">Ver perfil</a></div>',
            unsafe_allow_html=True,
        )

st.markdown("<br><hr style='opacity:0.15'><center class='muted'>Cristian Camilo Bran Arriaga — Medellín, Colombia</center>", unsafe_allow_html=True)
