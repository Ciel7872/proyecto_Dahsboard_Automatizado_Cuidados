import requests
import pandas as pd
import streamlit as st

class CepalMonitor:
    def __init__(self):
        self.base_url = "https://api-cepalstat.cepal.org/cepalstat/api/v1"
        self.arg_id = 32  # Argentina

    @st.cache_data
    def fetch_benchmark(self, _self, indicator_id):
        endpoint = f"{self.base_url}/indicator/{indicator_id}/data"
        params = {"lang": "es", "format": "json", "members": self.arg_id}
        try:
            r = requests.get(endpoint, params=params)
            r.raise_for_status()
            return pd.DataFrame(r.json()['body'])
        except:
            return None

# --- MAPEO REAL ---
KPI_MAP = {
    "Uso del Tiempo (ODS 5.4.1)": 3201,
    "Feminización de la Pobreza": 3330,
    "Participación Laboral (%)": 2470,
    "Fuera del Mercado por Cuidados": 5531, # ¡Esta es clave!
    "Jóvenes NINI (15-24 años)": 3469,
    "Dependencia Demográfica": 4792,
    "Hogares Jefatura Femenina": 2465,
    "Asistencia Escolar (6-11 años)": 4977
}

def main():
    st.set_page_config(page_title="Monitor CEPAL Benchmark", layout="wide")
    st.title("📊 Benchmark Nacional (CEPALSTAT)")
    
    monitor = CepalMonitor()
    
    with st.sidebar:
        st.header("Filtros de API")
        seleccion = st.selectbox("Seleccioná métrica de comparación:", list(KPI_MAP.keys()))
        btn = st.button("Consultar API")

    if btn:
        id_api = KPI_MAP[seleccion]
        df = monitor.fetch_benchmark(monitor, id_api)
        
        if df is not None:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric("Indicador Seleccionado", seleccion)
                st.write(f"ID Técnico: {id_api}")
            with col2:
                st.subheader("Serie Histórica Argentina")
                st.dataframe(df)
                # Si el DF tiene columnas 'años' y 'valor', podés graficar:
                # st.line_chart(df.set_index('años')['valor'])
        else:
            st.error("No hay datos disponibles para Argentina en este indicador.")

if __name__ == "__main__":
    main()