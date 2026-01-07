import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Control de Gastos Quincenales", page_icon="💰")

st.title("💰 Mi Control Quincenal")

# 1. Inicialización del estado de la aplicación
if 'gastos' not in st.session_state:
    st.session_state.gastos = []

# 2. Entrada de Salario
with st.sidebar:
    st.header("Presupuesto")
    salario_inicial = st.number_input("Salario Quincenal:", min_value=0.0, step=100.0, value=1000.0)
    
    st.divider()
    if st.button("Limpiar todos los datos"):
        st.session_state.gastos = []
        st.rerun()

# 3. Formulario para agregar gastos
st.subheader("Registrar Nuevo Gasto")
with st.form("nuevo_gasto"):
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        nombre = st.text_input("Concepto / Descripción")
    with col2:
        monto = st.number_input("Monto", min_value=0.0, step=1.0)
    with col3:
        categoria = st.selectbox("Categoría", ["Vivienda", "Comida", "Transporte", "Ocio", "Servicios", "Otros"])
    
    submit = st.form_submit_button("Agregar Gasto")

    if submit:
        if nombre and monto > 0:
            st.session_state.gastos.append({
                "Concepto": nombre,
                "Monto": monto,
                "Categoría": categoria
            })
            st.success("¡Gasto agregado!")
        else:
            st.error("Por favor, introduce un nombre y un monto válido.")

# 4. Cálculos y Visualización
df_gastos = pd.DataFrame(st.session_state.gastos)

if not df_gastos.empty:
    total_gastado = df_gastos["Monto"].sum()
    saldo_restante = salario_inicial - total_gastado

    # Métricas principales
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Salario Inicial", f"${salario_inicial:,.2f}")
    col_b.metric("Total Gastado", f"${total_gastado:,.2f}", delta=f"-{total_gastado:,.2f}", delta_color="inverse")
    col_c.metric("Saldo Restante", f"${saldo_restante:,.2f}")

    st.divider()

    # Gráficos y Tablas
    col_tabla, col_grafico = st.columns([1.5, 1])

    with col_tabla:
        st.write("### Detalle de Compras")
        st.dataframe(df_gastos, use_container_width=True)

    with col_grafico:
        st.write("### Gastos por Categoría")
        resumen_cat = df_gastos.groupby("Categoría")["Monto"].sum()
        st.bar_chart(resumen_cat)

else:
    st.info("Aún no has registrado gastos. Comienza llenando el formulario de arriba.")
    st.metric("Saldo Disponible", f"${salario_inicial:,.2f}")
