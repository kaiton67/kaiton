import streamlit as st

st.title("Contáctanos")

with st.form("formulario_contacto"):
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Email")
    telefono = st.text_input("Teléfono")
    mensaje = st.text_area("Mensaje")

    submitted = st.form_submit_button("Enviar")
    if submitted:
        st.success(f"Gracias, {nombre}. Tu mensaje ha sido enviado. Nos contactaremos pronto.")
        # Aquí podrías agregar lógica para enviar el mensaje a un email o base de datos.
