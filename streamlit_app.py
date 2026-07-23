import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

# ────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cristian Camilo Bran Arriaga | Portfolio Web & AI",
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
# ESTILOS AVANZADOS Y EFECTO DE PARTÍCULAS / CURSOR (Dribbble Style)
# ────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
    :root {
        --ink: #0A0F1D;
        --panel: rgba(18, 25, 43, 0.75);
        --panel-glass: rgba(18, 25, 43, 0.65);
        --signal: #4FD9C6;
        --signal-2: #2E8B7A;
        --amber: #F6AD55;
        --paper: #F8FAFC;
        --muted: #94A3B8;
        --line: rgba(79, 217, 198, 0.2);
    }

    .stApp {
        background: radial-gradient(circle at 50% 0%, #111B33 0%, #0A0F1D 100%);
        color: var(--paper);
        overflow-x: hidden;
    }

    /* Canvas de partículas de fondo interactivo con el cursor */
    #cursor-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 99999;
    }

    h1, h2, h3, h4 { color: #FFFFFF !important; letter-spacing: -0.02em; }

    .glass-card {
        background: var(--panel-glass);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--line);
        padding: 30px;
        border-radius: 18px;
        margin-bottom: 22px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform .3s cubic-bezier(0.175, 0.885, 0.32, 1.275), border-color .3s ease, box-shadow .3s ease;
    }
    .glass-card:hover {
        border-color: var(--signal);
        transform: translateY(-6px);
        box-shadow: 0 16px 40px rgba(79, 217, 198, 0.15);
    }
    .glass-card ul { margin: 12px 0 0; padding-left: 20px; }
    .glass-card li { margin-bottom: 8px; color: var(--muted); font-size: 0.95rem; }
    .glass-card p { color: var(--muted); line-height: 1.6; }

    .eyebrow {
        color: var(--signal); font-family: monospace; text-transform: uppercase;
        letter-spacing: 3px; font-size: 0.85rem; margin-bottom: 10px; font-weight: 700;
    }
    .tag {
        display: inline-block; font-family: monospace; font-size: 0.75rem;
        color: #0A0F1D; background: var(--signal); padding: 4px 12px;
        border-radius: 20px; margin-bottom: 12px; font-weight: 700;
        box-shadow: 0 0 15px rgba(79,217,198,0.4);
    }
    .tag.amber { background: var(--amber); color: #0A0F1D; box-shadow: 0 0 15px rgba(246,173,85,0.4); }
    .org { color: var(--signal); font-weight: 700; font-size: 1.05rem; }
    .muted { color: var(--muted); font-size: 0.9rem; }

    /* Botones Interactivos con Animación */
    .stButton>button {
        border-radius: 12px; padding: 12px 20px; font-weight: 600; width: 100%;
        transition: all 0.3s cubic-bezier(.34,1.56,.64,1);
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.05);
        color: var(--paper);
    }
    .stButton>button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 12px 30px rgba(79, 217, 198, 0.25);
        border-color: var(--signal);
    }

    button[kind="primary"] {
        background: linear-gradient(135deg, var(--signal) 0%, var(--signal-2) 100%) !important;
        color: #0A0F1D !important; border-color: var(--signal) !important;
        font-weight: 700;
        box-shadow: 0 4px 20px rgba(79, 217, 198, 0.3);
    }
    button[kind="primary"]:hover {
        box-shadow: 0 8px 30px rgba(79, 217, 198, 0.5);
    }
    button[kind="secondary"] {
        background: rgba(18, 25, 43, 0.8) !important;
        color: var(--paper) !important;
    }

    .stat-box {
        background: var(--panel); border: 1px solid var(--line);
        border-left: 4px solid var(--signal);
        padding: 18px 22px; border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        transition: transform .3s ease, border-color .3s ease;
    }
    .stat-box:hover { transform: translateY(-4px); border-color: var(--amber); }
    .stat-box .num { font-family: monospace; font-size: 1.8rem; font-weight: 700; color: #FFFFFF; }
    .stat-box .lbl { color: var(--muted); font-size: 0.82rem; text-transform: uppercase; letter-spacing: 1px; }

    .dash-slot {
        border: 1px dashed var(--line); border-radius: 16px;
        padding: 22px; background: var(--panel-glass);
    }

    .upload-note {
        border: 1px dashed var(--amber); border-radius: 12px; padding: 16px;
        background: rgba(246, 173, 85, 0.08); font-size: 0.9rem; color: var(--muted);
    }
</style>

<!-- Script para el efecto interactivo de partículas en el cursor (Framer / Dribbble style) -->
<canvas id="cursor-canvas"></canvas>
<script>
const canvas = document.getElementById('cursor-canvas');
const ctx = canvas.getContext('2d');

let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
});

const mouse = { x: null, y: null, radius: 120 };

window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
});

window.addEventListener('mouseout', () => {
    mouse.x = null;
    mouse.y = null;
});

class Particle {
    constructor() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.size = Math.random() * 2 + 1;
        this.baseX = this.x;
        this.baseY = this.y;
        this.density = (Math.random() * 20) + 5;
        this.vx = (Math.random() - 0.5) * 0.8;
        this.vy = (Math.random() - 0.5) * 0.8;
    }
    update() {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0 || this.x > width) this.vx = -this.vx;
        if (this.y < 0 || this.y > height) this.vy = -this.vy;

        if (mouse.x != null && mouse.y != null) {
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            if (distance < mouse.radius) {
                let force = (mouse.radius - distance) / mouse.radius;
                let angle = Math.atan2(dy, dx);
                this.x -= Math.cos(angle) * force * 5;
                this.y -= Math.sin(angle) * force * 5;
            }
        }
    }
    draw() {
        ctx.fillStyle = 'rgba(79, 217, 198, 0.6)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.closePath();
        ctx.fill();
    }
}

let particlesArray = [];
function initParticles() {
    particlesArray = [];
    let numberOfParticles = (width * height) / 12000;
    for (let i = 0; i < numberOfParticles; i++) {
        particlesArray.push(new Particle());
    }
}
initParticles();

function animate() {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < particlesArray.length; i++) {
        particlesArray[i].update();
        particlesArray[i].draw();

        // Conectar líneas cercanas
        for (let j = i; j < particlesArray.length; j++) {
            let dx = particlesArray[i].x - particlesArray[j].x;
            let dy = particlesArray[i].y - particlesArray[j].y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            if (distance < 90) {
                ctx.strokeStyle = `rgba(79, 217, 198, ${0.15 * (1 - distance/90)})`;
                ctx.lineWidth = 0.5;
                ctx.beginPath();
                ctx.moveTo(particlesArray[i].x, particlesArray[i].y);
                ctx.lineTo(particlesArray[j].x, particlesArray[j].y);
                ctx.stroke();
            }
        }

        // Conectar con el cursor
        if (mouse.x != null && mouse.y != null) {
            let dx = particlesArray[i].x - mouse.x;
            let dy = particlesArray[i].y - mouse.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            if (distance < 130) {
                ctx.strokeStyle = `rgba(246, 173, 85, ${0.3 * (1 - distance/130)})`;
                ctx.lineWidth = 0.8;
                ctx.beginPath();
                ctx.moveTo(particlesArray[i].x, particlesArray[i].y);
                ctx.lineTo(mouse.x, mouse.y);
                ctx.stroke();
            }
        }
    }
    requestAnimationFrame(animate);
}
animate();
</script>
""",
    unsafe_allow_html=True,
)

# ────────────────────────────────────────────────────────────
# DATOS (Experiencia, Formación y Certificaciones)
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
                    "Genero informes estandarizados y personalizados sobre datos de la organización: cuentas médicas, autorizaciones, MIPRES, riesgo en salud, PQRS y tutelas[cite: 1].",
                    "Brindo soporte a los informes creados y ejecuto modificaciones según necesidades del negocio[cite: 1].",
                    "Escribo queries en MySQL y MariaDB para la entrega de información a distintas áreas[cite: 1].",
                    "Desarrollo scripts en Python para cruces y limpieza de datos entre distintas fuentes[cite: 1].",
                    "Apoyo la extracción de información solicitada por entes de control[cite: 1].",
                    "Diseño y mantengo tableros estratégicos y operativos en Power BI[cite: 1].",
                    "Gestiono versionamiento y flujos de trabajo con GitHub, Trello y Airflow[cite: 1].",
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
                    "Gestioné escalamientos sobre fallas en servidores directamente con el proveedor Tigo[cite: 1].",
                    "Realicé monitoreo continuo de servidores y solicitudes de ampliación de recursos[cite: 1].",
                    "Atendí solicitudes de recuperación de archivos y administré el Directorio Activo (AD)[cite: 1].",
                    "Supervisé el backup de servidores y lideré la migración de servidores a la nube[cite: 1].",
                    "Construí tableros en Power BI para seguimiento de disponibilidad de infraestructura[cite: 1].",
                    "Participé en capacitación del proceso N2 y en la ejecución del DRP (plan de recuperación ante desastres)[cite: 1].",
                    "Elaboré informes mensuales de disponibilidad del centro de datos (DC)[cite: 1].",
                    "Administré la plataforma VPN Fortigate y mantuve actualizado el inventario de servidores[cite: 1].",
                    "Lideré la implementación de nuevos servidores en producción[cite: 1].",
                ],
            },
            {
                "rol": "Agente Mesa de Servicios",
                "org": "Savia Salud EPS",
                "fecha": "05/2022 – 03/2023",
                "funciones": [
                    "Recibí y gestioné solicitudes vía chat, correo y canal telefónico, generando tickets de atención[cite: 1].",
                    "Brindé soporte técnico sobre equipos, periféricos e impresoras[cite: 1].",
                    "Realicé diagnóstico de red HFC/FTT y escalamientos a nivel N2[cite: 1].",
                    "Diseñé tableros de seguimiento en Power BI[cite: 1].",
                    "Administré cuentas y recursos en Google Workspace[cite: 1].",
                    "Apoyé la coordinación de análisis de datos, haciendo seguimiento de tickets y entrega de informes[cite: 1].",
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
                    "Brindé soporte técnico a computadores portátiles y de escritorio[cite: 1].",
                    "Ejecuté mantenimiento correctivo y preventivo, y gestioné inventario de equipos[cite: 1].",
                    "Realicé validación de puntos de red y diagnóstico de cableado interno[cite: 1].",
                    "Instalé sistema operativo Windows 10 y realicé cambios/actualizaciones de equipos[cite: 1].",
                    "Configuré programas internos de VPN y antivirus corporativo[cite: 1].",
                    "Gestioné tickets a través de la plataforma Seus[cite: 1].",
                ],
            },
            {
                "rol": "Analista Mesa de Servicios",
                "org": "Comware",
                "fecha": "06/2019 – 04/2021",
                "funciones": [
                    "Brindé soporte telefónico a técnicos en sitio sobre aperturas en la red MPLS del operador Tigo-Une[cite: 1].",
                    "Di soporte en topologías de red en anillo y en bus[cite: 1].",
                    "Gestioné instalación y retiro de servicios, con monitoreo continuo de la red MPLS[cite: 1].",
                    "Creé y realicé seguimiento de tickets a través de BMC Remedy[cite: 1].",
                    "Utilicé Fénix ATC Clientes, Service Desk, iMaster NCE y Siebel como plataformas de soporte[cite: 1].",
                ],
            },
            {
                "rol": "Agente de Soporte Técnico",
                "org": "Teleperformance",
                "fecha": "06/2018 – 05/2019",
                "funciones": [
                    "Atendí clientes vía telefónica para resolver casuísticas de navegación de internet en hogares[cite: 1].",
                    "Di soporte a operadoras móviles en líneas internacionales Orange y Jazztel[cite: 1].",
                ],
            },
        ],
    },
}

FORMACION_ACADEMICA = [
    {
        "titulo": "Especialista en Big Data e BI",
        "periodo": "02/2025 – 01/2026",
        "detalle": "Especialización orientada a arquitectura de datos, modelado y visualización estratégica para la toma de decisiones[cite: 1].",
        "uploader": False,
    },
    {
        "titulo": "Ingeniero en Telecomunicaciones",
        "periodo": "02/2021 – 07/2023",
        "detalle": "Formación profesional en redes, infraestructura de telecomunicaciones y sistemas de comunicación[cite: 1].",
        "uploader": True,
    },
    {
        "titulo": "Tecnólogo en Gestión de Redes de Datos",
        "periodo": "01/2016 – 04/2018",
        "detalle": "Formación técnica en administración, monitoreo y soporte de redes de datos[cite: 1].",
        "uploader": False,
    },
    {
        "titulo": "Técnico en Sistemas",
        "periodo": "01/2014 – 12/2015",
        "detalle": "Base técnica en soporte de sistemas, hardware y software[cite: 1].",
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
# NAVEGACIÓN POR BOTONES
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
        techo bajo[cite: 1].</p>
        <p>Mi camino empezó en soporte técnico y redes MPLS —en Teleperformance resolviendo casos de
        conectividad para líneas internacionales, y en Comware dando soporte en sitio sobre la red del
        operador Tigo-Une[cite: 1]—. De ahí pasé a mantenimiento de equipos e infraestructura crítica en Supplies
        y en Savia Salud EPS, donde escalé fallas de servidores, administré Directorio Activo, ejecuté
        migraciones a la nube y sostuve planes de recuperación ante desastres (DRP)[cite: 1]. Esa base de
        infraestructura es, hoy, lo que me permite entender de extremo a extremo de dónde viene cada dato
        que analizo.</p>
        <p>Actualmente soy <strong>Analista de Inteligencia de Negocios en Savia Salud EPS</strong>, donde
        genero informes estratégicos sobre cuentas médicas, autorizaciones, riesgo en salud y PQRS para una
        aseguradora de salud[cite: 1]. Trabajo con SQL sobre MySQL y MariaDB, escribo scripts en Python para cruces
        de datos entre fuentes, y diseño tableros estratégicos y operativos en Power BI que sirven de
        insumo real para la toma de decisiones y la respuesta a entes de control[cite: 1].</p>
        <p>En paralelo, completé una <strong>especialización en Big Data e BI</strong> (2025–2026) y cinco
        certificaciones aplicadas de inteligencia artificial durante 2026 —desde IA generativa con Gemini,
        pasando por fundamentos de ciencia de datos y automatización con bots, hasta el marco legal de la
        IA en publicidad digital[cite: 1]—. No lo veo como una colección de diplomas, sino como una actualización
        deliberada de mi caja de herramientas para seguir siendo útil a medida que el trabajo con datos
        cambia. Me caracteriza la facilidad para el trabajo en equipo, la capacidad de simultanear varias
        tareas y adaptarme a entornos distintos, y un entusiasmo genuino por seguir aprendiendo[cite: 1].</p>
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
    st.info("💡 Mueve el cursor por la pantalla para interactuar con el fondo dinámico de partículas. Usa los botones superiores para explorar las secciones.")

# ────────────────────────────────────────────────────────────
# PÁGINA: EXPERIENCIA
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Experiencia":
    st.markdown('<p class="eyebrow">Trayectoria profesional</p>', unsafe_allow_html=True)
    st.title("Experiencia, por etapa")
    st.write("Seis roles agrupados en tres etapas de especialización creciente. Selecciona una pestaña para ver el detalle de funciones.")

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
# PÁGINA: FORMACIÓN & CURSOS
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Formación & Cursos":
    st.markdown('<p class="eyebrow">Formación continua</p>', unsafe_allow_html=True)
    st.title("Formación académica y certificaciones")
    st.write("Bloques de formación académica formal y certificaciones tecnológicas avanzadas.")

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
                        'esta sesión; para que queden disponibles de forma permanente, '
                        'súbelos al repositorio del proyecto en Streamlit Cloud.</div>',
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
# PÁGINA: DASHBOARDS
# ────────────────────────────────────────────────────────────
elif st.session_state.page == "Dashboards":
    st.markdown('<p class="eyebrow">Proyectos aplicados</p>', unsafe_allow_html=True)
    st.title("Tableros y visualizaciones")
    st.write(
        "Espacios interactivos para incrustar tus tableros públicos de Power BI y Looker Studio. "
        "Reemplaza el `src` de cada iframe por tu enlace de publicación."
    )

    col_pbi, col_looker = st.columns(2)

    with col_pbi:
        st.markdown("#### 📊 Power BI")
        st.markdown('<div class="dash-slot">', unsafe_allow_html=True)
        components.iframe(
            src="https://app.powerbi.com/view?r=REEMPLAZA_CON_TU_ENLACE_DE_PUBLICACION",
            height=400,
        )
        st.caption("Ejemplo: dashboard de gestión de cuentas médicas y riesgo en salud.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_looker:
        st.markdown("#### 📈 Looker Studio")
        st.markdown('<div class="dash-slot">', unsafe_allow_html=True)
        components.iframe(
            src="https://lookerstudio.google.com/embed/reporting/REEMPLAZA_CON_TU_ID/page/1",
            height=400,
        )
        st.caption("Ejemplo: automatización de métricas de infraestructura y disponibilidad.")
        st.markdown("</div>", unsafe_allow_html=True)

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
