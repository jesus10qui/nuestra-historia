import streamlit as st
from datetime import datetime, date
import random

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Para Pam ❤️ - Nuestra Historia",
    page_icon="💖",
    layout="centered"
)

# Estilos visuales personalizados (colores cálidos y románticos)
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #ff4b4b;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #ff758c;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .timeline-card {
        background-color: #1e1e2f;
        border-left: 4px solid #ff4b4b;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .timeline-date {
        color: #ff758c;
        font-weight: bold;
        font-size: 0.9rem;
    }
    .timeline-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: bold;
        margin: 5px 0;
    }
    .timeline-desc {
        color: #b0b0d0;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------
st.markdown('<h1 class="main-title">Nuestra Historia ❤️</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Un pequeño espacio en la web dedicado solo a nosotros dos</p>', unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# 1. CONTADOR DE TIEMPO DETALLADO
# ---------------------------------------------------------
st.subheader("⏳ El tiempo que llevamos juntos")

# Ajusta aquí la fecha exacta de su aniversario (Año, Mes, Día)
fecha_inicio = datetime(2026, 5, 10, 0, 0, 0) # Ejemplo: 10 de mayo de 2026
ahora = datetime.now()
diferencia = ahora - fecha_inicio

dias = diferencia.days
horas = diferencia.seconds // 3600
minutos = (diferencia.seconds % 3600) // 60

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Días", value=f"{dias} 🗓️")
with col2:
    st.metric(label="Horas", value=f"{horas} ⏰")
with col3:
    st.metric(label="Minutos", value=f"{minutos} ⏱️")

st.caption("...y cada segundo a tu lado vale totalmente la pena.")

st.divider()

# ---------------------------------------------------------
# 2. LÍNEA DE TIEMPO DE NUESTRA HISTORIA (MULTIFOTOS)
# ---------------------------------------------------------
st.subheader("📍 Nuestra Línea de Tiempo")
st.write("Cada gran historia tiene momentos inolvidables. Aquí están los nuestros:")

# En "fotos" ahora usamos corchetes [ ] para poner una lista con los nombres de tus fotos.
hitos =[
    {        
        "fecha": "Mayo 2026",
        "titulo": "✨ El Comienzo de Todo",
        "desc": "El día en que decidimos dar el paso y empezar este bonito camino juntos.",
        "fotos": ["mayo1.jpeg", "mayo2.jpeg"]  # Dos fotos lado a lado
    },
    {
        "fecha": "Junio 2026",
        "titulo": " 💐Las primeras flores que te regale amor💐",
        "desc": "Risas, buenas conversas y darnos cuenta de lo bien que la pasamos juntos.",
        "fotos": ["junio1.jpeg","junio2.jpeg"]  # Una sola foto
    },
    {
        "fecha": "Julio 2026",
        "titulo": "📸 Fotos & Recuerdos",
        "desc": "Empezamos a llenar la galería de recuerdos bonitos.",
        "fotos": ["julio1.jpeg","julio2.jpeg","julio3.jpeg","julio4.jpeg","julio5.jpeg","julio6.jpeg"]  # Dejas los corchetes vacíos si no quieres fotos en este hito
    },
    {
        "fecha": "Agosto 2026",
        "titulo": "❤️ Un Mes Más Juntos",
        "desc": "Seguimos sumando momentos increíbles y fortaleciendo lo nuestro.",
        "fotos": ["agosto1.jpeg", "agosto2.jpeg","agosto3.jpeg"]  # Agrega aquí las fotos de agosto
    },
    {
        "fecha": "Septiembre 2026",
        "titulo": "nuestra primera salida al cine❤️",
        "desc": "Decidí usar lo que sé de programación para crear un espacio único dedicado a ti.",
        "fotos": ["septiembre1.jpeg", "septiembre2.jpeg", "septiembre3.jpeg","septiembre4.jpeg"]  # Tres fotos lado a lado
    },
    {
        "fecha": "El Futuro...",
        "titulo": "🚀 Lo que nos falta por vivir",
        "desc": "Aún nos quedan muchos viajes, cenas, aventuras y metas por cumplir juntos.",
        "fotos": ["fut1.jpg", "fut2.jpg","fut3.jpg"]
    }
]

for hito in hitos:
    # 1. Muestra la tarjeta del hito
    st.markdown(f"""
        <div class="timeline-card">
            <div class="timeline-date">{hito['fecha']}</div>
            <div class="timeline-title">{hito['titulo']}</div>
            <div class="timeline-desc">{hito['desc']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. Lógica para desplegar una o múltiples fotos
    lista_fotos = hito.get("fotos", [])
    
    if lista_fotos:
        # Si es solo 1 foto, ocupa todo el ancho
        if len(lista_fotos) == 1:
            try:
                st.image(lista_fotos[0], use_container_width=True)
            except FileNotFoundError:
                st.info(f"📷 Guarda la imagen '{lista_fotos[0]}' en tu carpeta.")
        # Si hay 2 o más fotos, crea columnas iguales para alinearlas lado a lado
        else:
            columnas = st.columns(len(lista_fotos))
            for i, foto in enumerate(lista_fotos):
                with columnas[i]:
                    try:
                        st.image(foto, use_container_width=True)
                    except FileNotFoundError:
                        st.info(f"📷 Falta '{foto}'")
        st.write("") # Margen inferior entre un hito y otro

st.divider()

# ---------------------------------------------------------
# 3. ÁLBUM DE RECUERDOS (FOTOS Y VIDEOS)
# ---------------------------------------------------------
st.subheader("🎬 Álbum de Recuerdos")

tab1, tab2, tab3 = st.tabs(["Fotos Bonitas", "Momentos Divertidos", "Videos Especiales"])

with tab1:
    st.write("Nuestras mejores fotos juntos. ❤️")
    
    # 1. Pon aquí el nombre de TODAS las fotos que quieras agregar
    fotos_album = ["album1.jpeg", "album2.jpeg", "album3.jpeg", "album4.jpeg","album5.jpeg","album6.jpeg","album7.jpeg","album8.jpeg"]
    
    # 2. Creamos 2 columnas
    cols = st.columns(2)
    
    # 3. Recorremos la lista y repartimos las fotos (una a la izquierda, una a la derecha)
    for i, foto in enumerate(fotos_album):
        with cols[i % 2]: 
            try:
                st.image(foto, use_container_width=True)
            except FileNotFoundError:
                st.info(f"📷 Falta agregar la foto: '{foto}'")

with tab2:
    st.write("Ese video donde no parábamos de reír 😂")
    st.video("gracioso.mp4")

with tab3:
    st.write("Nuestros videos favoritos.")
    st.video("boxeo.mp4")
    st.video("tu.mp4")
    st.video("yo.mp4")
    st.video("primer_mes.mp4")
    
st.divider()

# ---------------------------------------------------------
# 4. GENERADOR DE "RAZONES POR LAS QUE ME ENCANTAS"
# ---------------------------------------------------------
st.subheader("🎲 Un detalle interactivo")
st.write("Haz clic en el botón para descubrir una razón al azar por la que me encantas:")

razones = [
    "Me encanta tu sonrisa y cómo me alegras el día con ella.",
    "Admiro mucho tu forma de ser y lo inteligente que eres.",
    "Me encanta la paz que me da estar a tu lado.",
    "Amo cómo nos complementamos tan bien.",
    "Me encantan nuestros abrazos y nuestras pláticas infinitas.",
    "Simplemente amo cada pequeño detalle que tienes conmigo."
]

if st.button("💖 Haz clic aquí para ver una razón"):
    razon_elegida = random.choice(razones)
    st.balloons()
    st.success(f"✨ **Razón del momento:** {razon_elegida}")

st.divider()

# ---------------------------------------------------------
# 5. MINI QUIZ DE PAREJA
# ---------------------------------------------------------
st.subheader("🧩 ¿Qué tanto recuerdas de nosotros?")
st.write("Un mini test rápido solo para probar memoria 😉")

q1 = st.radio(
    "1. ¿Quién dijo 'te quiero' o tuvo el primer detalle especial?",
    ["Tú", "Yo", "Fue mutuo al mismo tiempo", "Ninguno admite la verdad 😂"]
)

q2 = st.radio(
    "2. ¿Qué es lo que más disfrutamos hacer juntos?",
    ["Comer cosas ricas", "Pasear y conversar", "Ver series / películas", "Todas las anteriores ❤️"]
)

if st.button("Enviar respuestas"):
    st.snow()
    st.annotation = st.balloons()
    st.info("¡Respuesta correcta! La verdad es que cualquier momento juntos siempre es el mejor.")

st.divider()

# ---------------------------------------------------------
# CARTA / MENSAJE FINAL
# ---------------------------------------------------------
with st.expander("💌 Lee esta cartita rápida"):
    st.write("""
    Hola Pam ❤️
    
    Hoy celebramos 5 meses nuestro indicador de tiempo te diria cuantos dias horas y minutos son, es hermoso todo lo que hemos vivido juntos, que bonito como hemos avanzado dia a dia y se que no estamos en el mejor momento cuando estoy escribiendo esto pero si lo llegas a leer es por que lo estamos logrando mi amor.
    
    Gracias por cada día, por cada risa y por acompañarme en este camino.
    
    ¡Te quiero muchísimo! y TE AMO COMO NO TIENES IDEA
    """)