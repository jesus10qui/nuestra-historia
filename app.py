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

# Fecha exacta de aniversario
fecha_inicio = datetime(2026, 5, 10, 0, 0, 0) 
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

hitos =[
    {        
        "fecha": "Mayo 2026",
        "titulo": "✨ El Comienzo de Todo",
        "desc": "El día en que decidimos dar el paso y empezar este bonito camino juntos.",
        "fotos": ["mayo1.jpeg", "mayo2.jpeg"]  
    },
    {
        "fecha": "Junio 2026",
        "titulo": " 💐Las primeras flores que te regale amor💐",
        "desc": "Risas, buenas conversas y darnos cuenta de lo bien que la pasamos juntos.",
        "fotos": ["junio1.jpeg","junio2.jpeg"]  
    },
    {
        "fecha": "Julio 2026",
        "titulo": "📸 Fotos & Recuerdos",
        "desc": "Empezamos a llenar la galería de recuerdos bonitos.",
        "fotos": ["julio1.jpeg","julio2.jpeg","julio3.jpeg","julio4.jpeg","julio5.jpeg","julio6.jpeg"]  
    },
    {
        "fecha": "Agosto 2026",
        "titulo": "❤️ Un Mes Más Juntos",
        "desc": "Seguimos sumando momentos increíbles y fortaleciendo lo nuestro.",
        "fotos": ["agosto1.jpeg", "agosto2.jpeg","agosto3.jpeg"]  
    },
    {
        "fecha": "Septiembre 2026",
        "titulo": "nuestra primera salida al cine❤️",
        "desc": "Decidí usar lo que sé de programación para crear un espacio único dedicado a ti.",
        "fotos": ["septiembre1.jpeg", "septiembre2.jpeg", "septiembre3.jpeg","septiembre4.jpeg"]  
    },
    {
        "fecha": "El Futuro...",
        "titulo": "🚀 Lo que nos falta por vivir",
        "desc": "Aún nos quedan muchos viajes, cenas, aventuras y metas por cumplir juntos.",
        "fotos": ["fut1.jpg", "fut2.jpg","fut3.jpg"]
    }
]

for hito in hitos:
    st.markdown(f"""
        <div class="timeline-card">
            <div class="timeline-date">{hito['fecha']}</div>
            <div class="timeline-title">{hito['titulo']}</div>
            <div class="timeline-desc">{hito['desc']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    lista_fotos = hito.get("fotos", [])
    
    if lista_fotos:
        if len(lista_fotos) == 1:
            try:
                st.image(lista_fotos[0], use_container_width=True)
            except FileNotFoundError:
                st.info(f"📷 Guarda la imagen '{lista_fotos[0]}' en tu carpeta.")
        else:
            columnas = st.columns(len(lista_fotos))
            for i, foto in enumerate(lista_fotos):
                with columnas[i]:
                    try:
                        st.image(foto, use_container_width=True)
                    except FileNotFoundError:
                        st.info(f"📷 Falta '{foto}'")
        st.write("") 

st.divider()

# ---------------------------------------------------------
# 3. ÁLBUM DE RECUERDOS (FOTOS Y VIDEOS)
# ---------------------------------------------------------
st.subheader("🎬 Álbum de Recuerdos")

tab1, tab2, tab3 = st.tabs(["Fotos Bonitas", "Momentos Divertidos", "Videos Especiales"])

with tab1:
    st.write("Nuestras mejores fotos juntos. ❤️")
    
    fotos_album = ["album1.jpeg", "album2.jpeg", "album3.jpeg", "album4.jpeg","album5.jpeg","album6.jpeg","album7.jpeg","album8.jpeg"]
    cols = st.columns(2)
    
    for i, foto in enumerate(fotos_album):
        with cols[i % 2]: 
            try:
                st.image(foto, use_container_width=True)
            except FileNotFoundError:
                st.info(f"📷 Falta agregar la foto: '{foto}'")

with tab2:
    st.write("Ese video donde no parábamos de reír 😂")
    try:
        st.video("gracioso.mp4")
    except:
        st.info("Falta el video 'gracioso.mp4'")

with tab3:
    st.write("Nuestros videos favoritos.")
    videos = ["boxeo.mp4", "tu.mp4", "yo.mp4", "primer_mes.mp4"]
    for vid in videos:
        try:
            st.video(vid)
        except:
            st.info(f"Falta el video '{vid}'")
            
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
    st.balloons()
    st.info("¡Respuesta correcta! La verdad es que cualquier momento juntos siempre es el mejor.")

st.divider()

# ---------------------------------------------------------
# 6. NUESTRA CANCIÓN ESPECIAL (SPOTIFY)
# ---------------------------------------------------------
st.subheader("🎵 Nuestra Canción")
st.write("Dale play mientras sigues bajando...")

# Código HTML para incrustar el reproductor de Spotify
spotify_iframe = """
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/2DnJjbjNTV9Nd5NOa1KGba?si=4578ed72f2924eab" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
"""
st.markdown(spotify_iframe, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# 7. REGALO SORPRESA (BLOQUEADO HASTA EL 10 DE OCTUBRE)
# ---------------------------------------------------------
st.subheader("🎁 Sorpresa de 5 Meses")

fecha_aniversario = date(2026, 10, 10)
hoy = date.today()

if hoy >= fecha_aniversario:
    st.success("🎉 ¡FELIZ 5 MESES MI AMOR! ❤️")
    st.write("¡Por fin llegó el día! Gracias por estos meses maravillosos. Aquí tienes tu sorpresa...")
    
    # --- AQUÍ PONES LA FOTO O VIDEO SORPRESA ---
    try:
        st.image("sorpresa.jpg", caption="Te amo muchísimo ❤️", use_container_width=True)
    except FileNotFoundError:
        st.info("📷 Guarda tu foto sorpresa como 'sorpresa_5_meses.jpeg'")
        
else:
    dias_faltantes = (fecha_aniversario - hoy).days
    st.warning(f"🔒 **Bloqueado:** Esta sorpresa especial se abrirá automáticamente en {dias_faltantes} días (el 10 de octubre). ¡Paciencia! 😉")

st.divider()

# ---------------------------------------------------------
# CARTA / MENSAJE FINAL
# ---------------------------------------------------------
with st.expander("💌 Lee esta cartita rápida"):
    st.write("""
    Hola Pam ❤️
    
    Hoy celebramos 5 meses, nuestro indicador de tiempo te diría cuántos días, horas y minutos son. Es hermoso todo lo que hemos vivido juntos, qué bonito cómo hemos avanzado día a día, y sé que no estamos en el mejor momento cuando estoy escribiendo esto, pero si lo llegas a leer es porque lo estamos logrando, mi amor.
    
    Gracias por cada día, por cada risa y por acompañarme en este camino.
    
    ¡Te quiero muchísimo! y TE AMO COMO NO TIENES IDEA
    """)