import streamlit as st
import pandas as pd

st.title("ALPFA UTEP - Professional Development Events 📅")

# Cargar eventos
events = pd.read_csv("events.csv")

# Mostrar datos crudos para debug
st.write("Datos cargados:")
st.write(events)

# Filtros
tipo_evento = st.selectbox("Filtrar por tipo de evento", ["Todos"] + list(events["Tipo"].unique()))
empresa = st.selectbox("Filtrar por empresa", ["Todos"] + list(events["Empresa"].unique()))

# Aplicar filtros
filtered_events = events.copy()
if tipo_evento != "Todos":
    filtered_events = filtered_events[filtered_events["Tipo"] == tipo_evento]
if empresa != "Todos":
    filtered_events = filtered_events[filtered_events["Empresa"] == empresa]

# Mostrar eventos
for i, row in filtered_events.iterrows():
    st.markdown(f"### {row['Nombre del Evento']}")
    st.write(f"**Fecha y Hora:** {row['Fecha']} {row['Hora']}")
    st.write(f"**Tipo:** {row['Tipo']}")
    st.write(f"**Empresa:** {row['Empresa']}")
    st.write(f"**Descripción:** {row['Descripción']}")
    st.markdown(f"[Regístrate aquí]({row['Link de Registro']})")
    st.write(f"**RSVP Abierto:** {row['RSVP Abierto']}")
    st.write("---")

