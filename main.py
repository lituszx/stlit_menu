import streamlit as st

# 1. Definición de los platos y sus ingredientes
MENU_DATA = {
    "Lentejas clásicas": ["Lentejas", "Patata", "Zanahoria", "Cebolla"],
    "Amanida de Pasta": ["Pasta integral", "Tomates cherry", "Pechuga de pollo", "Yogur natural", "Mostaza", "Limón"],
    "Arroz con Pollo": ["Arroz integral", "Pechuga de pollo", "Judía verde", "Salsa de soja"],
    "Ensaladilla Ligera": ["Patata", "Zanahoria", "Atún al natural", "Huevos", "Yogur natural"],
    "Garbanzos Popeye": ["Garbanzos (bote)", "Espinacas congeladas", "Ajo", "Pimentón", "Huevos"],
    "Arroz con Merluza": ["Arroz integral", "Merluza", "Limón"],
    "Pollo con Calabacín": ["Pechuga de pollo", "Calabacín"],
    "Pad Thai": ["Fideos de arroz", "Pollo", "Zanahoria", "Cebolla", "Brotes de soja"]
}

st.set_page_config(page_title="Planificador de Batch Cooking", page_icon="🍱")

st.title("🍱 Planificador Semanal & Lista de la Compra")
st.write("Selecciona los platos para tu semana de Batch Cooking:")

# 2. Organización de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
elecciones = {}

col1, col2 = st.columns(2)

with col1:
    for dia in dias[:3]:
        elecciones[dia] = st.selectbox(f"Comida {dia}", list(MENU_DATA.keys()), key=dia)

with col2:
    for dia in dias[3:]:
        elecciones[dia] = st.selectbox(f"Comida {dia}", list(MENU_DATA.keys()), key=dia)

# 3. Lógica para la lista de la compra
if st.button("Generar Lista de la Compra 🛒"):
    st.subheader("Tu lista de la compra para el Domingo:")
    
    lista_compra = []
    for plato in elecciones.values():
        lista_compra.extend(MENU_DATA[plato])
    
    # Eliminamos duplicados y ordenamos
    lista_final = sorted(list(set(lista_compra)))
    
    # Mostrar la lista con checkboxes para cuando estés en el súper
    for item in lista_final:
        st.checkbox(item, key=f"buy_{item}")
        
    st.success("¡Consejo! Recuerda revisar lo que ya tienes en la despensa (especias, aceite, sal) antes de salir.")

# 4. Resumen del Batch Cooking (Opcional)
with st.expander("Ver resumen de preparaciones"):
    st.info("""
    - **Hervir:** Arroz, Pasta, Huevos, Judía verde, Patata, Zanahoria.
    - **Horno:** Pollo y Calabacín.
    - **Olla:** Lentejas.
    """)