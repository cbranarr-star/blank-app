import streamlit as st
import pandas as pd

# Configuración inicial de la página
st.set_page_config(page_title="Portafolio | Cristian Bran", page_icon="📊", layout="wide")

# Estilo personalizado básico (Opcional, para mejorar la estética)
st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-color: #1f77b4; }
    </style>
""", unsafe_allow_html=True)

# Menú de navegación lateral
st.sidebar.title("Navegación")
st.sidebar.markdown("---")
seccion = st.sidebar.radio("Ir a:", [
    "Sobre Mí", 
    "Mi Propuesta de Valor", 
    "Educación", 
    "Experiencia", 
    "Habilidades y Fortalezas", 
    "Portafolio de Dashboards"
])

st.sidebar.markdown("---")
st.sidebar.write("**Contacto:**")
st.sidebar.write("📧 ccbran1998@hotmail.com")
st.sidebar.write("🔗 [Mi perfil de LinkedIn](https://www.linkedin.com/in/cristian-camilo-bran-arriaga-b1074730b)")

# --- SECCIÓN: SOBRE MÍ ---
if seccion == "Sobre Mí":
    st.title("¡Hola! Soy Cristian Camilo Bran Arriaga 👋")
    st.subheader("Profesional en Telecomunicaciones | Especialista en BI y Big Data")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Reemplaza el enlace por una foto tuya real (ej. "mi_foto.jpg" si está en la misma carpeta)
        st.image("https://via.placeholder.com/350x350.png?text=Foto+de+Cristian", caption="Cristian Camilo Bran", use_container_width=True)
    with col2:
        st.write("""
        Bienvenido a mi portafolio interactivo. Soy un profesional híbrido con una base sólida en 
        la infraestructura tecnológica y una profunda especialización en el análisis de datos.
        
        Me apasiona transformar datos complejos en información visual y estratégica que facilite 
        la toma de decisiones (Data-Driven). Entiendo el ciclo de vida del dato desde su 
        transmisión e infraestructura (Telecomunicaciones) hasta su modelado, análisis y 
        visualización (Business Intelligence & Big Data).
        """)
        
        st.info("💡 **Mi objetivo:** Ayudar a las organizaciones a descubrir el valor oculto en sus datos para optimizar procesos, predecir tendencias y aumentar su rentabilidad.")
        
        st.download_button(
            label="📄 Descargar Hoja de Vida (PDF)",
            data="Archivo PDF simulado", # Recuerda cambiar esto por open("tu_cv.pdf", "rb")
            file_name="CV_Cristian_Bran.pdf",
            mime="application/pdf"
        )

# --- SECCIÓN: MI PROPUESTA DE VALOR ---
elif seccion == "Mi Propuesta de Valor":
    st.title("¿Qué le puedo aportar a tu empresa?")
    st.write("Mi perfil combina la visión técnica de las telecomunicaciones con el poder estratégico de los datos. Al incorporarme a tu equipo, obtendrás:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**1. Visión End-to-End del Dato**")
        st.write("Entiendo cómo se generan y transmiten los datos desde la infraestructura, lo que me permite asegurar su integridad antes de llevarlos a entornos de Big Data y BI.")
        
        st.success("**2. Toma de Decisiones Estratégicas**")
        st.write("No solo construyo dashboards; analizo el contexto del negocio para crear métricas (KPIs) que realmente impacten los objetivos de la empresa.")

    with col2:
        st.success("**3. Automatización y Eficiencia**")
        st.write("Transformo procesos de reportes manuales y tediosos en flujos de datos automatizados, ahorrando horas de trabajo operativo al equipo.")
        
        st.success("**4. Puente entre IT y Negocio**")
        st.write("Tengo la capacidad de traducir requerimientos técnicos complejos en un lenguaje claro para los gerentes y directivos (y viceversa).")

# --- SECCIÓN: EDUCACIÓN ---
elif seccion == "Educación":
    st.title("Formación Académica")
    st.write("Mi base de conocimientos se fundamenta en la tecnología y el análisis avanzado:")
    
    # Especialización
    with st.expander("🎓 Especialización en Business Intelligence y Big Data", expanded=True):
        st.write("**Institución:** [Nombre de la Universidad / Institución]")
        st.write("**Año:** [Año de graduación]")
        st.write("""
        * **Enfoque:** Arquitecturas de Big Data, modelado de bases de datos, herramientas de visualización avanzada, minería de datos y analítica predictiva.
        """)
        
    # Pregrado
    with st.expander("🎓 Profesional en Telecomunicaciones", expanded=True):
        st.write("**Institución:** [Nombre de la Universidad / Institución]")
        st.write("**Año:** [Año de graduación]")
        st.write("""
        * **Enfoque:** Redes de datos, infraestructura tecnológica, protocolos de comunicación y gestión de proyectos tecnológicos.
        """)

# --- SECCIÓN: EXPERIENCIA ---
elif seccion == "Experiencia":
    st.title("Experiencia Profesional")
    st.write("A continuación, un resumen de mi trayectoria reciente:")
    
    # Ejemplo de experiencia 1
    st.subheader("📊 Analista BI / Especialista en Datos en [Empresa 1]")
    st.caption("Mes Año – Presente | Ubicación")
    st.write("""
    * **Logro:** Reduje el tiempo de generación de reportes en un X% mediante la automatización con [Herramienta, ej. Power BI/Python].
    * **Responsabilidad:** Desarrollo y mantenimiento de dashboards gerenciales para el seguimiento de KPIs del área de [Ventas/Operaciones].
    * **Responsabilidad:** Extracción, transformación y carga (ETL) de datos desde múltiples fuentes hacia el Data Warehouse.
    """)
    
    st.divider()
    
    # Ejemplo de experiencia 2
    st.subheader("📡 Ingeniero de Telecomunicaciones / Cargo Anterior en [Empresa 2]")
    st.caption("Mes Año – Mes Año | Ubicación")
    st.write("""
    * **Logro:** Implementación de [Proyecto X] que mejoró la conectividad o la eficiencia en un Y%.
    * **Responsabilidad:** Gestión de infraestructura de red y monitoreo de servicios.
    * **Responsabilidad:** Análisis de tráfico de datos para optimización de recursos.
    """)

# --- SECCIÓN: HABILIDADES Y FORTALEZAS ---
elif seccion == "Habilidades y Fortalezas":
    st.title("Conocimientos, Herramientas y Fortalezas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Fortalezas Personales (Soft Skills)")
        st.write("✅ **Pensamiento Analítico:** Capacidad para desglosar problemas complejos y encontrar patrones en los datos.")
        st.write("✅ **Resolución de Problemas:** Enfoque proactivo para encontrar soluciones técnicas a desafíos de negocio.")
        st.write("✅ **Adaptabilidad:** Facilidad para aprender nuevas tecnologías y entornos rápidamente.")
        st.write("✅ **Comunicación Asertiva:** Habilidad para explicar hallazgos de datos técnicos a audiencias no técnicas.")

    with col2:
        st.subheader("Habilidades Técnicas (Hard Skills)")
        # Barras de progreso de habilidades
        st.write("**Análisis de Datos y BI** (Power BI, Tableau, Excel Avanzado)")
        st.progress(90)
        
        st.write("**Bases de Datos** (SQL, PostgreSQL, MySQL)")
        st.progress(85)
        
        st.write("**Programación** (Python, Pandas, Streamlit)")
        st.progress(75)
        
        st.write("**Telecomunicaciones y Redes**")
        st.progress(80)

# --- SECCIÓN: DASHBOARDS ---
elif seccion == "Portafolio de Dashboards":
    st.title("Mis Proyectos y Dashboards")
    st.write("En este espacio interactivo puedes explorar algunos de los dashboards que he construido.")
    
    # Pestañas para diferentes proyectos
    tab1, tab2, tab3 = st.tabs(["Dashboard Comercial", "Análisis de Telecomunicaciones", "Proyecto Local 3"])
    
    with tab1:
        st.subheader("Dashboard Comercial y de Ventas")
        st.write("En este proyecto, integré datos de ventas para mostrar la evolución mensual, productos más vendidos y rendimiento por zona.")
        st.info("👉 Aquí incrustaremos el iframe de tu dashboard de Power BI o el código de tu gráfico en Streamlit.")
        
    with tab2:
        st.subheader("Análisis de Tráfico y Redes (Telecom)")
        st.write("Dashboard diseñado para monitorear el uptime, latencia y consumo de ancho de banda en nodos de red.")
        st.info("👉 Espacio reservado para tu segundo dashboard.")
        
    with tab3:
        st.subheader("Proyecto Personal de Big Data")
        st.write("Análisis descriptivo y predictivo de [Tema del proyecto].")
        st.info("👉 Espacio reservado para tu tercer dashboard.")
