import streamlit as st


st.set_page_config(page_title="Calculateur IMC", page_icon="calculatrice de l'imc")


st.title("Calculatrice d'IMC")

st.write("Cette application permet de calculer votre **Indice de Masse Corporelle (IMC)**.")


st.markdown("---")


col1, col2 = st.columns(2)

with col1:
   
    poids = st.number_input("Donner votre poids (kg)", min_value=0.0, step=0.1, format="%.2f")

with col2:
    
    taille = st.number_input("Donner votre taille (m)", min_value=0.0, step=0.01, format="%.2f")


if st.button("Calculer mon IMC"):
    if taille > 0:
        
        imc = poids / (taille ** 2)
        
        
        st.subheader(f"Votre IMC=: {imc:.2f}")
        
       
        if imc < 18.5:
            st.info("Insuffisance pondérale (Maigreur)")
        elif 18.5 <= imc < 25:
            st.success("Poids normal")
        elif 25 <= imc < 30:
            st.warning("Surpoids")
        else:
            st.error("Obésité") 
            
    else:
        
        st.warning("« Veuillez remplir les informations »")


with st.sidebar:
    st.image("imc.png")
    st.header("À propos")
    st.markdown("""
    L'IMC est un indicateur standardisé utilisé par l'OMS :
    - **< 18.5** : Maigreur
    - **18.5 - 25** : Normal
    - **25 - 30** : Surpoids
    - **> 30** : Obésité
    """)
