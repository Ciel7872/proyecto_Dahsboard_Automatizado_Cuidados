# Autor: Nahuel Trejo - Data Engineering
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def run_diagnostico():
    st.header("DATOS PROCESADOS: DIAGNÓSTICO ESTRATÉGICO")
    
    # CSS Específico para Metrics
    st.markdown("""
        <style>
        div[data-testid="stMetric"] {
            background: rgba(30, 33, 48, 0.7) !important;
            border-radius: 15px; padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-bottom: 4px solid #007BFF !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # KPIs - Fila 1
    c1, c2, c3 = st.columns(3)
    c1.metric("Brecha TNR", "14.4h", "↑ Promedio")
    c2.metric("Carga Cuidado", "37.4h", "Semanal")
    c3.metric("Índice Igualdad", "2.25", "Ratio M/H")

    st.write("---")

    # Fila 2: El mapa ocupa el 60% para que se vea bien Córdoba
    col_map, col_bar = st.columns([1.8, 1.2])
    
    with col_map:
        st.subheader("📍 Análisis Regional (Córdoba)")
        # Mapa con más altura
        st.map(pd.DataFrame({'lat': [-31.417], 'lon': [-64.183]}), zoom=11)

    with col_bar:
        st.subheader("📊 Cuidado Promedio")
        df_dummy = pd.DataFrame({'Sexo': ['Mujer', 'Hombre'], 'Valor': [28, 12]})
        fig = px.bar(df_dummy, x='Sexo', y='Valor', color='Sexo', 
                     color_discrete_map={"Hombre": "#007BFF", "Mujer": "#E83E8C"}, template="plotly_dark")
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")

    # Fila 3: El gráfico de torta e Insights comparten el fondo
    col_pie, col_ins = st.columns([1.2, 1.8])

    with col_pie:
        st.subheader("🥧 Reparto Semanal")
        fig2 = px.pie(df_dummy, values='Valor', names='Sexo', hole=0.5,
                      color_discrete_map={"Hombre": "#007BFF", "Mujer": "#E83E8C"}, template="plotly_dark")
        fig2.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig2, use_container_width=True)

    with col_ins:
        st.subheader("💡 Insights Clave")
        st.markdown("""
        * **Brecha de Género:** La disparidad en el tiempo de cuidado no remunerado sigue siendo el principal obstáculo para la paridad económica.
        * **Distribución:** Se observa una concentración crítica de tareas en el género femenino en áreas periféricas.
        * **Proyección:** Sin intervención estratégica, la convergencia total se estima para después de 2050.
        """)