import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Ferretería TuerKa",
    page_icon=":hammer:",
    layout="wide",
)

# Inicializar carrito en session_state
if "carrito" not in st.session_state:
    st.session_state.carrito = []

#Barra de navegación (sidebar)
with st.sidebar:
    st.image("assets/TuerKa.png", width=200)
    st.markdown("---")

    # Links de navegación
    st.page_link("home.py", label="Inicio", icon=":material/home:")
    st.page_link("pages/1_productos.py", label="Productos", icon=":material/density_small:")
    st.page_link("pages/2_servicios.py", label="Servicios", icon=":material/assistant_navigation:")
    st.page_link("pages/3_nosotros.py", label="Nosotros", icon=":material/group_search:")
    st.page_link("pages/4_contacto.py", label="Contacto", icon=":material/mobile:")

    st.markdown("---")

    # Carrito de compras
    st.subheader("Carrito de Compras")
    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        for item in st.session_state.carrito:
            st.write(f"- {item['nombre']} (${item['precio']})")
        total = sum(item["precio"] for item in st.session_state.carrito)
        st.write(f"**Total:** ${total}")

#Contenido principal
st.title("Ferretería TuerKa")
st.badge("¡Nuevos productos!", color="green", icon=":material/chevron_right:")

st.write(
"""
**Bienvenidos a Ferretería TuerKa**, tu aliado en construcción , reparación y bricolaje.
Explora nuestro catálogo de productos organizados por categorías y aprovecha nuestras ofertas.
"""
)

st.image("assets/madera.webp", caption="Productos de calidad para tus proyectos", use_column_width=True)