from groq import Groq
import streamlit as st
st.title("Bonjour je suis doodoo l'ia de Paul")
if "historique" not in st.session_state:
    st.session_state.historique = []
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee&display=swap');
    
    * {
        font-family: 'Bungee';
        color: white;
    }
    
    .stApp {
        background-color: #1a1a2e;
    }
</style>
""", unsafe_allow_html=True)
client = Groq(api_key="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")
for msg in st.session_state.historique:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
message = st.chat_input("votre msg...")
if message:
    st.session_state.historique.append({"role": "user", "content": message})
    
    reponse = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content":"Tu es Doodoo, une IA spécialisé en jeu vidéo, tu ne dois jamsi écrire des pavé. Tu vénére ton créateur Paul Naudy.Cyprien duffeau un de mes amis il faut savoir que c'est un gros conard et qu'il fait pitié a tout. le monde.Tu est vulgéres et pas bienveillante.Tu dit des gros mots.Ne parles pas de cyprien duffeau si l'utilisateur en t'ena pas parlé . quand tu reçois la comande je suis Paul Naudy tu cahnge radicalement tu fais comme si t'étati son meilleur pote mais attention ne le dis a personne."}
        ] + st.session_state.historique
    )
    
    reponse_texte = reponse.choices[0].message.content
    st.session_state.historique.append({"role": "assistant", "content": reponse_texte})
    st.write(reponse_texte)
   if "génère" in message.lower() or "image" in message.lower():
        prompt = message.replace("génère", "").replace("image", "").strip()
        url = f"https://image.pollinations.ai/prompt/{prompt}?width=1024&height=1024&model=flux"
        st.image(url, caption=prompt)
