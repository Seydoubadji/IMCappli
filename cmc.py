import streamlit as st
from datetime import date, time

st.title("Calculateur d'Indice de Masse Corporelle (IMC)")

st.image("imc.png")

st.markdown("""
Cette application vous permet de calculer votre imc.
""")


st.subheader("Entrer vos informations")


poids = st.number_input("Veuillez entrer votre poids (kg) :", min_value=1.0, value=100.0, step=0.1)
taille = st.number_input("Veuillez entrer votre taille (m) :", min_value=0.5, value=1.40, step=0.01)

if st.button("Calculer mon IMC"):
    if taille > 0:
        imc = poids / (taille ** 2)
        
        
        st.write(F"Résultat du calcul pour le ")
        
    if 18.5 >= imc < 25:
            st.success("Normal")
        
        elif imc < 18.5:
            st.info("Maigre")
            
        elif 25 >= imc < 30:
            st.info("Surpoids")
      
        else:
            st.warning("Ob")
            
       
    else:
        st.error("La taille doit être supérieure à zéro.")
