import streamlit as st

# Datos de ejemplo de productos
productos = {
    "Madera": [
        {"nombre": "Tablero de pino 2x4", "precio": 12990, "imagen": "assets/madera.webp"},
        {"nombre": "Piso flotante roble", "precio": 8990, "imagen": "assets/madera.webp"},
    ],
    "Agua": [
        {"nombre": "Bomba de agua 1/2 HP", "precio": 45990, "imagen": "assets/bomba0.5hp.webp"},
        {"nombre": "Estanque 1000L", "precio": 78990, "imagen": "assets/tanquemixto.jpg"},
    ],
    "Eléctrico": [
        {"nombre": "Cable NYY 4mm", "precio": 3490, "imagen": "assets/cable4mm.webp"},
        {"nombre": "Interruptor Hembra", "precio": 5990, "imagen": "assets/interruptorhembra.webp"},
    ],
    "Tubos PVC": [
        {"nombre": "Tubo Sanitario PVC 110mm", "precio": 2990, "imagen": "assets/tubopvc110.webp"},
        {"nombre": "Codo Sanitario PVC 110mm 90° ", "precio": 1490, "imagen": "assets/codo90x110.webp"},
    ],
    "Herramientas": [
        {"nombre": "variedad de extintores", "precio": 39990, "imagen": "assets/extintores.webp"},
        {"nombre": "martillos", "precio": 18990, "imagen": "assets/martillo.jpg"},
    ],
    "Interiores": [
        {"nombre": "Pintura latex 20L", "precio": 24990, "imagen": "assets/pintura20l.jpg"},
        {"nombre": "Aire acondicionado", "precio": 49990, "imagen": "assets/aire9.webp"},
    ],
    "Tornillos/Clavos": [
        {"nombre": "Caja tornillos 3\"", "precio": 2990, "imagen": "assets/tornillos.jpg"},
        {"nombre": "Clavos galvanizados 2\"", "precio": 1990, "imagen": "assets/clavos.jpg"},
    ],
}

# Función para agregar al carrito
def agregar_al_carrito(nombre, precio):
    st.session_state.carrito.append({"nombre": nombre, "precio": precio})
    st.success(f"Agregado: {nombre} (${precio})")

# --------------------- Contenido --------------------------#
st.title("Nuestros Productos")

# Seleccionar categoría
categoria = st.selectbox("Selecciona una categoría:", list(productos.keys()))

# Mostrar productos en columnas
cols = st.columns(2)
for i, producto in enumerate(productos[categoria]):
    with cols[i % 2]:
        st.image(producto["imagen"], width=200)
        st.subheader(producto["nombre"])
        st.write(f"${producto['precio']}")
        st.button(
            "Agregar al carrito",
            on_click=agregar_al_carrito,
            args=(producto["nombre"], producto["precio"]),
            key=f"btn_{categoria}_{i}"
        )