# Autor: Nahuel Trejo - Data Engineering
import streamlit as st
from dashboard_diagnostico import run_diagnostico
from dashboard_simulador import run_simulador

# CONFIGURACIÓN GLOBAL
st.set_page_config(page_title="Monitor Estratégico ODS 5.4.1", layout="wide")

# CSS GLOBAL DARK UI
st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; }
    section[data-testid="stSidebar"] { 
        background-color: #161b22 !important; 
        border-right: 1px solid #30363d; 
    }
    html, body, [class*="css"], .stMarkdown, p, span, label, li {
        color: #e0e0e0 !important;
    }
    h1, h2, h3 { color: #ffffff !important; }
    
    /* Botones Sidebar */
    section[data-testid="stSidebar"] .stButton > button {
        background: linear-gradient(135deg, #1f6feb 0%, #007BFF 100%);
        color: white !important; border: none; border-radius: 10px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR PERSISTENTE
with st.sidebar:
    st.title("ODS 5.4.1")
    st.markdown("---")
    nav = st.radio("Navegación Histórica", ["📈 Diagnóstico Estratégico", "🕹️ Simulador de Impacto"])
    st.markdown("---")
    st.subheader("Panel de Exportación")
    st.button("📄 Generar Reporte PDF")
    st.button("📥 Exportar Data (CSV)")
    st.markdown("---")
    st.caption("Datatón 2026 - Análisis de Cuidados")

# NAVEGACIÓN
if nav == "📈 Diagnóstico Estratégico":
    run_diagnostico()
else:
    run_simulador()