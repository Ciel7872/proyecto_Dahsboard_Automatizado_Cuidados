import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Monitor ODS 5.4.1 - UTN", layout="wide")

# CSS PARA ARREGLAR VISIBILIDAD Y DIMENSIONES
st.markdown("""
    <style>
    /* Fondo general */
    .stApp { background-color: #f8f9fb; }
    
    /* Títulos principales en negro puro */
    h1, h2, h3, span, label, p {
        color: #1a1a1a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Tarjetas KPI */
    div[data-testid="stMetric"] {
        background-color: white !important;
        padding: 15px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        border-left: 6px solid #1f77b4 !important;
    }
    
    /* Forzar visibilidad de métricas */
    [data-testid="stMetricLabel"] p { color: #444 !important; font-size: 1rem !important; }
    [data-testid="stMetricValue"] div { color: #000 !important; font-size: 2rem !important; font-weight: 800 !important; }

    /* Estilo de los Tabs (Insights) */
    .stTabs [data-baseweb="tab"] {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA (2016-2026)
anios = np.arange(2016, 2027)
hombres = [4000, 4100, 4250, 4400, 5100, 5200, 5400, 5600, 5900, 6200, 6400]
mujeres = [2100, 2200, 2350, 2500, 2800, 2950, 3100, 3300, 3500, 3600, 3800]
df_hist = pd.DataFrame({'Año': anios, 'Hombres': hombres, 'Mujeres': mujeres})

# 3. HEADER
st.title("Monitor de Igualdad ODS 5.4.1")
st.markdown("**MÉTRICAS CLAVE - INGENIERÍA DE DATOS**")

# 4. KPI ROW (Ajustadas)
k1, k2, k3, k4 = st.columns(4)
k1.metric("Brecha TNR", "54.8%", "↑ 1.2%")
k2.metric("Índice Igualdad", "0.84", "↑ 0.02")
k3.metric("Carga Trabajo", "2000h", "↑ 5%")
k4.metric("Carga Trabajo (%)", "32.1%", "↓ 0.5%")

st.write("") # Espaciador

# 5. MIDDLE ROW: DIMENSIONES CORREGIDAS
# Usamos alturas fijas para que el mapa y los gráficos coincidan
CHART_HEIGHT = 400

c1, c2, c3 = st.columns([2, 1, 1.2])

with c1:
    st.markdown("### Comparativa Temporal")
    fig_area = go.Figure()
    fig_area.add_trace(go.Scatter(x=df_hist['Año'], y=df_hist['Hombres'], name='Hombres', fill='tozeroy', line_color='#1f77b4', fillcolor='rgba(31, 119, 180, 0.4)'))
    fig_area.add_trace(go.Scatter(x=df_hist['Año'], y=df_hist['Mujeres'], name='Mujeres', fill='tonexty', line_color='#e7298a', fillcolor='rgba(231, 41, 138, 0.4)'))
    fig_area.update_layout(
        height=CHART_HEIGHT, 
        template="plotly_white", # Fondo blanco para que no se vea "oscuro"
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_area, use_container_width=True)

with c2:
    st.markdown("### Por Categoría")
    df_bar = pd.DataFrame({'Cat': ['Hombres', 'Mujeres'], 'Horas': [600, 450]})
    fig_bar = px.bar(df_bar, x='Cat', y='Horas', color='Cat', 
                     color_discrete_map={'Hombres':'#1f77b4', 'Mujeres':'#e7298a'},
                     template="plotly_white")
    fig_bar.update_layout(height=CHART_HEIGHT, showlegend=False, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_bar, use_container_width=True)

with c3:
    st.markdown("### Vista Regional")
    # Mapa con altura controlada para emparejar
    map_data = pd.DataFrame({'lat': [-31.442, -31.416, -31.430], 'lon': [-64.193, -64.183, -64.190]})
    st.map(map_data, zoom=11, use_container_width=True)

# 6. FILA 3: INSIGHTS (CON TEXTO VISIBLE)
st.write("")
b_left, b_right = st.columns([2, 1])

with b_left:
    st.markdown("### Insights Clave")
    tabs = st.tabs(["📈 Tendencias", "📍 Regional", "💡 Recomendaciones"])
    with tabs[0]:
        st.markdown("""
        - **Reducción de Brecha:** Se detectó una convergencia del 0.8% anual en la zona metropolitana.
        - **Feminización:** Persistencia crítica en tareas domésticas no remuneradas.
        """)
    with tabs[1]:
        st.write("Fuerte concentración de demanda en la zona centro de Córdoba Capital.")

with b_right:
    st.markdown("### Acciones de Reporte")
    st.button("📥 Exportar Datos (CSV)")
    st.button("📄 Generar Reporte PDF")

# FOOTER
st.markdown("---")
st.caption("Dataton 2026")