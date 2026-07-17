import streamlit as st
import pandas as pd

# Configuración inicial de la página
st.set_page_config(page_title="Mi Portafolio Interactivo", page_icon="💼", layout="wide")

# Menú de navegación lateral
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Ir a:", ["Sobre Mí", "Experiencia", "Habilidades", "Portafolio de Dashboards"])

# --- SECCIÓN: SOBRE MÍ ---
if seccion == "Sobre Mí":
    st.title("¡Hola! Soy [Tu Nombre]")
    st.subheader("Profesional en [Tu Profesión / Especialidad]")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Aquí puedes agregar una foto tuya
        st.image("https://via.placeholder.com/300", caption="[Tu Nombre]")
    with col2:
        st.write("""
        Bienvenido a mi portafolio interactivo. Aquí puedes encontrar un resumen de mi 
        trayectoria profesional, mis habilidades técnicas y los proyectos en los que he trabajado.
        
        Soy una persona apasionada por [tus intereses profesionales], con capacidad para 
        [tu principal propuesta de valor].
        """)
        st.download_button(
            label="📄 Descargar CV en PDF",
            data="Archivo PDF simulado", # Aquí enlazaremos tu PDF real
            file_name="hoja_de_vida.pdf",
            mime="application/pdf"
        )

# --- SECCIÓN: EXPERIENCIA ---
elif seccion == "Experiencia":
    st.title("Experiencia Profesional")
    
    # Ejemplo de experiencia 1
    st.subheader("Rol / Cargo en [Empresa 1]")
    st.caption("Mes Año – Presente | Ubicación")
    st.write("""
    * Logro destacado o responsabilidad clave número 1.
    * Logro destacado o responsabilidad clave número 2.
    """)
    
    st.divider() # Línea divisoria
    
    # Ejemplo de experiencia 2
    st.subheader("Rol / Cargo en [Empresa 2]")
    st.caption("Mes Año – Mes Año | Ubicación")
    st.write("""
    * Logro destacado o responsabilidad clave número 1.
    * Logro destacado o responsabilidad clave número 2.
    """)

# --- SECCIÓN: HABILIDADES ---
elif seccion == "Habilidades":
    st.title("Conocimientos y Herramientas")
    
    st.write("A lo largo de mi carrera, he desarrollado competencias en las siguientes áreas:")
    
    # Tabla interactiva para mostrar habilidades
    datos_habilidades = pd.DataFrame({
        "Categoría": ["Lenguajes", "Visualización", "Bases de Datos", "Soft Skills"],
        "Herramientas": ["Python, SQL", "Power BI, Streamlit", "PostgreSQL, MySQL", "Liderazgo, Comunicación"]
    })
    
    st.table(datos_habilidades)
    
    st.subheader("Nivel de Dominio Técnico")
    st.progress(90, text="Python")
    st.progress(85, text="SQL")
    st.progress(70, text="Power BI")

# --- SECCIÓN: DASHBOARDS ---
elif seccion == "Portafolio de Dashboards":
    st.title("Mis Proyectos y Dashboards")
    st.write("Explora algunos de los dashboards que he construido localmente y adaptado para la web.")
    
    tab1, tab2 = st.tabs(["Dashboard de Ventas", "Análisis de Clientes"])
    
    with tab1:
        st.subheader("Análisis de Ventas 2023")
        st.write("En este proyecto analicé el rendimiento de ventas utilizando X herramientas.")
        # Aquí podemos integrar un gráfico real de Streamlit o una imagen de tu dashboard local
        st.info("Espacio reservado para integrar el código de tu dashboard local o un iframe.")
        
    with tab2:
        st.subheader("Segmentación de Clientes")
        st.write("Aplicación de modelos de agrupación para encontrar nichos de mercado.")
        st.info("Espacio reservado para tu segundo dashboard.")

# Pie de página
st.sidebar.divider()
st.sidebar.write("Contacto: [Tu Correo] | [Tu LinkedIn]")
