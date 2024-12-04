import streamlit as st

st.header("Marias App")

# Erstelle ein Texteingabefeld
benutzer_text = st.text_input('Gib deinen Text hier ein:', key="input1")

# Zeige den eingegebenen Text an
st.write('Du hast eingegeben:', benutzer_text)

# Erstelle zwei Eingabefelder für Zahlen
zahl1 = st.number_input('Gib die erste Zahl ein:', value=0, step=1, key="input2")
zahl2 = st.number_input('Gib die zweite Zahl ein:', value=0, step=1, key="input3")

# Addiere die beiden Zahlen
summe = zahl1 + zahl2

# Zeige das Ergebnis an
st.write('Die Summe der beiden Zahlen ist:', summe)

# Starte mit einer Liste von GIF URLs
gif_urls = [
'https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif',
'https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif',
'https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif',
'https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
'https://media.giphy.com/media/lJNoBCvQYp7nq/giphy.gif',
'https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif',
'https://media.giphy.com/media/l1J9EdzfOSgfyueLm/giphy.gif',
'https://media.giphy.com/media/mCRJDo24UvJMA/giphy.gif',
'https://media.giphy.com/media/QyJ0We4GHpjBa/giphy.gif',
'https://media.giphy.com/media/Lq0h93752f6J9tijrh/giphy.gif',   
]

# Initialisiere den Session State für die GIF-Auswahl
if 'gif_index' not in st.session_state:
    st.session_state['gif_index'] = 0

# Funktion, um das GIF zu ändern
def change_gif():
    st.session_state['gif_index'] = (st.session_state['gif_index'] + 1) % len(gif_urls)

# Button, um das GIF zu ändern
st.button('Ändere das GIF', on_click=change_gif)

# Zeige das aktuelle GIF an
current_gif_url = gif_urls[st.session_state['gif_index']]
st.image(current_gif_url, caption='Aktuelles GIF', use_container_width=True)



st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.tapetenfieber.com/media/image/product/41712/lg/ftvl-0028_vlies-fototapete-no-28-a-million-stars-sternenhimmel-tapete-sternenhimmel-stars-sterne-leuchtsterne-nachthimmel-blau.jpg'); /* Beispiel-GIF URL */
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
