import streamlit as st

st.set_page_config(page_title="Tablero BI", layout="wide")

# ---- TABS ----
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📁 Datos", "📝 Conclusiones"])

# ---- TAB 1 ----
with tab1:
    st.title("📊 Dashboard")
    st.write("Visualizaciones principales del proyecto.")
    st.metric("Ingresos", "$120,000")
    st.metric("Ocupación", "87%")
    st.metric("Cancelaciones", "12%")

# ---- TAB 2 ----
with tab2:
    st.title("📁 Datos")
    st.write("Exploración simple de datos.")
    st.write("Carga un archivo CSV para visualizarlo.")
    
    uploaded = st.file_uploader("Subir archivo CSV", type="csv")
    if uploaded is not None:
        import pandas as pd
        df = pd.read_csv(uploaded)
        st.dataframe(df)

# ---- TAB 3 ----
with tab3:
    st.title("📝 Conclusiones")
    st.write("""
    - La pestaña 1 muestra métricas clave.
    - La pestaña 2 permite carga y visualización de datos.
    - Este tablero sirve como plantilla base para BI.
    """)
