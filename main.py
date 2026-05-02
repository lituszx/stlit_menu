import streamlit as st
import pandas as pd

PLATOS = {
    "Comidas": {
        "Llenties clàssiques": ["Llenties", "Patata", "Pastanaga", "Ceba"],
        "Amanida de pasta": ["Pasta integral", "Tomàquets cherry", "Pit de pollastre", "Iogurt natural", "Mostassa", "Llimona", "Cranc", "Pinya"],
        "Arròs amb pollastre": ["Arròs integral", "Pit de pollastre", "Mongeta verda", "Salsa de soja"],
        "Ensaladilla": ["Patata", "Pastanaga", "Tonyina al natural", "Ous", "Iogurt natural"],
        "Cigrons i espinacs": ["Cigrons (pot)", "Espinacs congelats", "All", "Pebre vermell", "Ous"],
        "Arròs amb lluç": ["Arròs integral", "Lluç", "Llimona"],
        "Pollastre amb carbassó": ["Pit de pollastre", "Carbassó"],
        "Pad Thai": ["Fideus d'arròs", "Pollastre", "Pastanaga", "Ceba", "Brots de soja"],
        "Família Berta": [],
        "Família Carles": [],
        "Indefinit": [],
    }
}

st.set_page_config(page_title="Health Strategy Planner", layout="wide")

st.title("🗓️ Week Planner")

dias = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]
opciones_comida = list(PLATOS["Comidas"].keys())
opciones_cena = list(PLATOS["Comidas"].keys())

try:
    idx_no_definido = opciones_comida.index("Indefinit")
    idx_berta = opciones_cena.index("Família Berta")
    idx_carles = opciones_cena.index("Família Carles")
except ValueError:
    idx_no_definido = 0
    idx_berta = 0
    idx_carles = 0

elecciones = {}

cols = st.columns(len(dias))

for i, dia in enumerate(dias):
    with cols[i]:
        st.markdown(f"**{dia}**")
        
        comida = st.selectbox(
            "Dinar", 
            opciones_comida, 
            index=idx_no_definido, 
            key=f"c_{dia}"
        )

        if dia == "Dimarts":
            default_cena = idx_berta
        elif dia == "Dijous":
            default_cena = idx_carles
        else:
            default_cena = idx_no_definido
            
        cena = st.selectbox(
            "Sopar", 
            opciones_cena, 
            index=default_cena, 
            key=f"n_{dia}"
        )
        
        elecciones[dia] = {"Dinar": comida, "Sopar": cena}

# 3. Generación de Lista de la Compra y Exportación
if st.button("🚀 Generar llista"):
    st.divider()
    col_resumen, col_compra = st.columns([1, 1])
    
    with col_resumen:
        st.subheader("📋 Resum")
        df_semana = pd.DataFrame(elecciones).T
        st.table(df_semana)

    with col_compra:
        st.subheader("🛒 Llista de la Compra")
        ingredientes_totales = []
        for v in elecciones.values():
            ingredientes_totales.extend(PLATOS["Comidas"][v["Dinar"]])
            ingredientes_totales.extend(PLATOS["Comidas"][v["Sopar"]])
        
        lista_final = sorted(list(set(ingredientes_totales)))
        
        texto_exportar = "🍎 Llista de la Compra\n" + "="*25 + "\n"
        
        for ing in lista_final:
            st.write(f"- [ ] {ing}")
            texto_exportar += f"- [ ] {ing}\n"
        
        st.write("")
        
        st.download_button(
            label="📩 Descargar LLista",
            data=texto_exportar,
            file_name="lista_compra_semanal.txt",
            mime="text/plain"
        )

    st.success("¡Plan Fet!")