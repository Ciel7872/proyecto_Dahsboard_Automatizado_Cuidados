# Autor: Nahuel Trejo - Data Engineering
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def run_simulador():
    st.header("SIMULADOR DE IMPACTO Y ACCESIBILIDAD")
    
    col_inputs, col_visuals = st.columns([1, 2])
    
    with col_inputs:
        st.subheader("Variables de Simulación")
        st.slider("Infraestructura ($M)", 0, 1000, 100)
        st.slider("Subsidios Directos (%)", 0, 50, 10)
        st.checkbox("Priorizar Zonas Críticas", value=True)
        st.button("Calcular Escenario")

    with col_visuals:
        st.subheader("Densidad de Demanda vs. Accesibilidad")
        df_scat = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50), 's': np.random.rand(50)*100})
        fig = px.scatter(df_scat, x='x', y='y', size='s', color='s',
                         color_continuous_scale=[[0, "#007BFF"], [1, "#E83E8C"]], template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    st.subheader("Proyección de Redistribución del Tiempo")
    fig_w = go.Figure(go.Waterfall(
        x = ["Estado Base", "Inversión Pública", "Subsidios", "Impacto Final"],
        y = [140, 30, -20, 150],
        decreasing = {"marker":{"color":"#E83E8C"}},
        increasing = {"marker":{"color":"#00C853"}},
        totals = {"marker":{"color":"#007BFF"}}
    ))
    fig_w.update_layout(template="plotly_dark", height=350)
    st.plotly_chart(fig_w, use_container_width=True)