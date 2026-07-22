import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

# ────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cristian Camilo Bran Arriaga | Portfolio",
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
# ESTILOS — paleta clara y profesional (blanco / azul acero / oro mate)
# ────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
    :root {
        --ink: #F8FAFC;
        --panel: #FFFFFF;
        --panel-glass: rgba(255, 255, 255, 0.9);
        --signal: #2E5AAC;
        --signal-2: #1F4685;
        --amber: #9C6B23;
        --paper: #172033;
        --muted: #5C6B85;
        --line: #E2E8F0;
    }

    .stApp {
        background: linear-gradient(180deg, #FFFFFF 0%, #F4F7FB 100%);
        color: var(--paper);
    }
    h1, h2, h3, h4 { color: var(--paper) !important; letter-spacing: -0.01em; }

    .glass-card {
        background: var(--panel-glass); backdrop-filter: blur(10px);
        border: 1px solid var(--line); padding: 26px 28px;
        border-radius: 14px; margin-bottom: 18px;
        box-shadow: 0 2px 14px rgba(23,32,51,0.05);
        transition: transform .28s ease, border-color .28s ease, box-shadow .28s ease;
    }
    .glass-card:hover {
        border-color: var(--signal); transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(46,90,172,0.14);
    }
    .glass-card ul { margin: 10px 0 0; padding-left: 20px; }
    .glass-card li { margin-bottom: 6px; color: #3A4A63; font-size: 0.95rem; }
    .glass-card p { color: #3A4A63; }

    .eyebrow {
        color: var(--signal); font-family: monospace; text-transform: uppercase;
        letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 8px;
    }
    .tag {
        display:inline-block; font-family: monospace; font-size: 0.72rem;
        color: #FFFFFF; background: var(--signal); padding: 3px 10px;
        border-radius: 20px; margin-bottom: 10px; font-weight:700;
    }
    .tag.amber { background: var(--amber); }
    .org { color: var(--signal); font-weight: 700; }
    .muted { color: var(--muted); font-size: 0.85rem; }

    /* ── botones de navegación con movimiento ── */
    .stButton>button {
        border-radius: 10px; padding: 10px 18px; font-weight: 600; width: 100%;
        transition: transform .22s cubic-bezier(.34,1.56,.64,1), box-shadow .22s ease, background .22s ease, border-color .22s ease;
        border: 1px solid var(--line);
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.035);
        box-shadow: 0 10px 22px rgba(46,90,172,0.22);
    }
    .stButton>button:active { transform: translateY(-1px) scale(0.98); }

    button[kind="secondary"] {
        background: #FFFFFF !important; color: var(--signal) !important;
        border-color: rgba(46,90,172,0.35) !important;
    }
    button[kind="secondary"]:hover {
        background: rgba(46,90,172,0.08) !important; border-color: var(--signal) !important;
    }
    button[kind="primary"] {
        background: linear-gradient(135deg, var(--signal) 0%, var(--signal-2) 100%) !important;
        color: #FFFFFF !important; border-color: var(--signal) !important;
        box-shadow: 0 0 0 3px rgba(46,90,172,0.15);
    }
    button[kind="primary"]:hover {
        box-shadow: 0 10px 24px rgba(46,90,172,0.35);
    }

    .stat-box {
        background: var(--panel-glass); border-left: 3px solid var(--signal);
        padding: 14px 18px; border-radius: 6px;
        box-shadow: 0 2px 14px rgba(23,32,51,0.05);
        transition: transform .22s ease, border-color .22s ease;
    }
    .stat-box:hover { transform: translateY(-3px); border-color: var(--amber); }
    .stat-box .num { font-family: monospace; font-size: 1.6rem; font-weight: 700; color: var(--paper); }
    .stat-box .lbl { color: var(--muted); font-size: 0.8rem; text-transform: uppercase; }

    .dash-slot {
        border: 1px dashed rgba(23,32,51,0.22); border-radius: 12px;
        padding: 18px; background: var(--panel-glass);
    }

    .upload-note {
        border: 1px dashed var(--amber); border-radius: 10px; padding: 14px 16px;
        background: rgba(156,107,35,0.06); font-size: 0.85rem; color: var(--muted);
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
            {
                "rol": "Analista de Inteligencia de Negocios",
                "org": "Savia Salud EPS",
                "fecha": "02/2025 – Presente",
                "funciones": [
                    "Genero informes estandarizados y personalizados sobre datos de la organización: cuentas médicas, autorizaciones, MIPRES, riesgo en salud, PQRS y tutelas.",
                    "Brindo soporte a los informes creados y ejecuto modificaciones según necesidades del negocio.",
                    "Escribo queries en MySQL y MariaDB para la entrega de información a distintas áreas.",
                    "Desarrollo scripts en Python para cruces y limpieza de datos entre distintas fuentes.",
                    "Apoyo la extracción de información solicitada por entes de control.",
                    "Diseño y mantengo tableros estratégicos y operativos en Power BI.",
                    "Gestiono versionamiento y flujos de trabajo con GitHub, Trello y Airflow.",
                ],
            },
        ],
    },
    "Infraestructura": {
        "icono": "🖥️",
        "periodo": "2022 – 2025",
        "items": [
            {
                "rol": "Analista de Infraestructura",
                "org": "Savia Salud EPS",
                "fecha": "05/2023 – 02/2025",
                "funciones": [
                    "Gestioné escalamientos sobre fallas en servidores directamente con el proveedor Tigo.",
                    "Realicé monitoreo continuo de servidores y solicitudes de ampliación de recursos.",
                    "Atendí solicitudes de recuperación de archivos y administré el Directorio Activo (AD).",
                    "Supervisé el backup de servidores y lideré la migración de servidores a la nube.",
                    "Construí tableros en Power BI para seguimiento de disponibilidad de infraestructura.",
                    "Participé en capacitación del proceso N2 y en la ejecución del DRP (plan de recuperación ante desastres).",
                    "Elaboré informes mensuales de disponibilidad del centro de datos (DC).",
                    "Administré la plataforma VPN Fortigate y mantuve actualizado el inventario de servidores.",
                    "Lideré la implementación de nuevos servidores en producción.",
                ],
            },
            {
                "rol": "Agente Mesa de Servicios",
                "org": "Savia Salud EPS",
                "fecha": "05/2022 – 03/2023",
                "funciones": [
                    "Recibí y gestioné solicitudes vía chat, correo y canal telefónico, generando tickets de atención.",
                    "Brindé soporte técnico sobre equipos, periféricos e impresoras.",
                    "Realicé diagnóstico de red HFC/FTT y escalamientos a nivel N2.",
                    "Diseñé tableros de seguimiento en Power BI.",
                    "Administré cuentas y recursos en Google Workspace.",
                    "Apoyé la coordinación de análisis de datos, haciendo seguimiento de tickets y entrega de informes.",
                ],
            },
        ],
    },
    "Soporte & Redes": {
        "icono": "🌐",
        "periodo": "2018 – 2022",
        "items": [
            {
                "rol": "Analista Nivel 1",
                "org": "Supplies",
                "fecha": "11/2021 – 02/2022",
                "funciones": [
                    "Brindé soporte técnico a computadores portátiles y de escritorio.",
                    "Ejecuté mantenimiento correctivo y preventivo, y gestioné inventario de equipos.",
                    "Realicé validación de puntos de red y diagnóstico de cableado interno.",
                    "Instalé sistema operativo Windows 10 y realicé cambios/actualizaciones de equipos.",
                    "Configuré programas internos de VPN y antivirus corporativo.",
                    "Gestioné tickets a través de la plataforma Seus.",
                ],
            },
            {
                "rol": "Analista Mesa de Servicios",
                "org": "Comware",
                "fecha": "06/2019 – 04/2021",
                "funciones": [
                    "Brindé soporte telefónico a técnicos en sitio sobre aperturas en la red MPLS del operador Tigo-Une.",
                    "Di soporte en topologías de red en anillo y en bus.",
                    "Gestioné instalación y retiro de servicios, con monitoreo continuo de la red MPLS.",
                    "Creé y realicé seguimiento de tickets a través de BMC Remedy.",
                    "Utilicé Fénix ATC Clientes, Service Desk, iMaster NCE y Siebel como plataformas de soporte.",
                ],
            },
            {
                "rol": "Agente de Soporte Técnico",
                "org": "Teleperformance",
                "fecha": "06/2018 – 05/2019",
                "funciones": [
                    "Atendí clientes vía telefónica para resolver casuísticas de navegación de internet en hogares.",
                    "Di soporte a operadoras móviles en líneas internacionales Orange y Jazztel.",
                ],
            },
        ],
    },
}

FORMACION_ACADEMICA = [
    {
        "titulo": "Especialista en Big Data e BI",
        "periodo": "02/2025 – 01/2026",
        "detalle": "Especialización orientada a arquitectura de datos, modelado y visualización estratégica para la toma de decisiones.",
        "uploader": False,
    },
    {
        "titulo": "Ingeniero en Telecomunicaciones",
        "periodo": "02/2021 – 07/2023",
        "detalle": "Formación profesional en redes, infraestructura de telecomunicaciones y sistemas de comunicación.",
        "uploader": True,
    },
    {
        "titulo": "Tecnólogo en Gestión de Redes de Datos",
        "periodo": "01/2016 – 04/2018",
        "detalle": "Formación técnica en administración, monitoreo y soporte de redes de datos.",
        "uploader": False,
    },
    {
        "titulo": "Técnico en Sistemas",
        "periodo": "01/2014 – 12/2015",
        "detalle": "Base técnica en soporte de sistemas, hardware y software.",
        "uploader": False,
    },
]

CERTIFICACIONES_2026 = [
    ("Crear valor con IA, automatización y bots", "02/07/2026", "2 h · 2 módulos", "Automatización"),
    ("Gen AI Intermedio — AWS Entrena Colombia / TIDWIT", "30/06/2026", "4 h 09 min", "IA generativa"),
    ("Publicidad digital: datos, IA y legalidad", "25/05/2026", "8 h · 2 módulos", "IA & Legalidad"),
    ("Introducción a la Ciencia de Datos", "07/01/2026", "6 h · 2 módulos", "Ciencia de datos"),
    ("Domina la IA con Gemini", "05/01/2026", "2 h · 2 módulos", "IA generativa"),
]

# ────────────────────────────────────────────────────────────
# NAVEGACIÓN POR BOTONES (con estado activo resaltado)
# ────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Inicio"

PAGE_ICONS = {
    "Inicio": "🏠",
    "Experiencia": "💼",
    "Formación & Cursos": "🎓",
    "Dashboards": "📈",
    "Contacto": "✉️",
}
PAGES = list(PAGE_ICONS.keys())

nav_cols = st.columns(len(PAGES))
for col, page_name in zip(nav_cols, PAGES):
    with col:
        is_active = st.session_state.page == page_name
        if st.button(
            f"{PAGE_ICONS[page_name]}  {page_name}",
            use_container_width=True,
            key=f"nav_{page_name}",
            type="primary" if is_active else "secondary",
        ):
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
        que ha construido su carrera subiendo capas de forma deliberada: primero aprendí a sostener la
        infraestructura que hace posible que los sistemas funcionen —redes, servidores, mesas de servicio—,
        después pasé a interpretar los datos que esos mismos sistemas generan, y desde 2026 sumé inteligencia
        artificial aplicada a ese stack, entendiendo que el dato sin contexto ni automatización tiene un
        techo bajo.</p>
        <p>Mi camino empezó en soporte técnico y redes MPLS —en Teleperformance resolviendo casos de
        conectividad para líneas internacionales, y en Comware dando soporte en sitio sobre la red del
        operador Tigo-Une—. De ahí pasé a mantenimiento de equipos e infraestructura crítica en Supplies
        y en Savia Salud EPS, donde escalé fallas de servidores, administré Directorio Activo, ejecuté
        migraciones a la nube y sostuve planes de recuperación ante desastres (DRP). Esa base de
        infraestructura es, hoy, lo que me permite entender de extremo a extremo de dónde viene cada dato
        que analizo.</p>
        <p>Actualmente soy <strong>Analista de Inteligencia de Negocios en Savia Salud EPS</strong>, donde
        genero informes estratégicos sobre cuentas médicas, autorizaciones, riesgo en salud y PQRS para una
        aseguradora de salud. Trabajo con SQL sobre MySQL y MariaDB, escribo scripts en Python para cruces
        de datos entre fuentes, y diseño tableros estratégicos y operativos en Power BI que sirven de
        insumo real para la toma de decisiones y la respuesta a entes de control.</p>
        <p>En paralelo, completé una <strong>especialización en Big Data e BI</strong> (2025–2026) y cinco
        certificaciones aplicadas de inteligencia artificial durante 2026 —desde IA generativa con Gemini,
        pasando por fundamentos de ciencia de datos y automatización con bots, hasta el marco legal de la
        IA en publicidad digital—. No lo veo como una colección de diplomas, sino como una actualización
        deliberada de mi caja de herramientas para seguir siendo útil a medida que el trabajo con datos
        cambia. Me caracteriza la facilidad para el trabajo en equipo, la capacidad de simultanear varias
        tareas y adaptarme a entornos distintos, y un entusiasmo genuino por seguir aprendiendo.</p>
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
# PÁGINA: EXPERIENCIA (segmentada por etapa, funciones expandidas)
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Experiencia":
    st.markdown('<p class="eyebrow">Trayectoria profesional</p>', unsafe_allow_html=True)
    st.title("Experiencia, por etapa")
    st.write("Seis roles agrupados en tres etapas de especialización creciente. Selecciona una pestaña para ver el detalle de funciones de cada cargo.")

    tabs = st.tabs([f"{v['icono']} {k}  ·  {v['periodo']}" for k, v in EXPERIENCIA.items()])
    for tab, (etapa, data) in zip(tabs, EXPERIENCIA.items()):
        with tab:
            for item in data["items"]:
                funciones_html = "".join(f"<li>{f}</li>" for f in item["funciones"])
                st.markdown(
                    f"""
                <div class="glass-card">
                    <span class="tag">{item['fecha']}</span>
                    <h4>{item['rol']}</h4>
                    <p class="org">{item['org']}</p>
                    <ul>{funciones_html}</ul>
                </div>
                """,
                    unsafe_allow_html=True,
                )

# ────────────────────────────────────────────────────────────
# PÁGINA: FORMACIÓN & CURSOS (segmentada, con anexos)
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Formación & Cursos":
    st.markdown('<p class="eyebrow">Formación continua</p>', unsafe_allow_html=True)
    st.title("Formación académica y certificaciones")
    st.write("Dos bloques: la base académica formal, y las certificaciones de IA/datos completadas en 2026.")

    tab_edu, tab_cert = st.tabs(["🎓 Formación académica", "🤖 Certificaciones IA · 2026"])

    with tab_edu:
        for edu in FORMACION_ACADEMICA:
            with st.expander(f"{edu['titulo']}  ·  {edu['periodo']}", expanded=edu["uploader"]):
                st.markdown(
                    f"""
                <div class="glass-card" style="margin-bottom:10px;">
                    <span class="tag amber">{edu['periodo']}</span>
                    <p>{edu['detalle']}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )
                if edu["uploader"]:
                    st.markdown(
                        '<div class="upload-note">📎 Espacio para anexar soportes de este título '
                        '(diploma, acta de grado, certificado). Los archivos se muestran solo durante '
                        'esta sesión; para que queden disponibles de forma permanente en el sitio, '
                        'súbelos también al repositorio del proyecto en Streamlit Cloud.</div>',
                        unsafe_allow_html=True,
                    )
                    archivos = st.file_uploader(
                        "Anexar documentos — Ingeniero en Telecomunicaciones",
                        type=["pdf", "png", "jpg", "jpeg"],
                        accept_multiple_files=True,
                        key="anexos_telecom",
                    )
                    if archivos:
                        st.success(f"{len(archivos)} archivo(s) cargado(s) en esta sesión:")
                        for a in archivos:
                            st.write(f"📄 {a.name}")

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
