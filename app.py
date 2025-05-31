import streamlit as st
import requests
import pandas as pd

# Config
st.set_page_config(page_title="Recommandations Utilisateur", layout="wide")

st.title("📰 Système de recommandation")

# Input
user_id = st.text_input("Entrez votre identifiant utilisateur :", "")

# Bouton pour lancer la requête
if st.button("Obtenir mes recommandations") and user_id:
    with st.spinner("Récupération des recommandations..."):
        try:
            # Appel à l’API Azure Function
            api_url = f"https://apprecommandes.azurewebsites.net/api/recommand_all?user_id={user_id}"
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            # Affichage des recommandations
            st.subheader("🔎 Recommandations pour l’utilisateur " + str(user_id))
            
            for reco_type in ['ALS', 'Embeddings', 'Similarité']:
                articles = data.get(reco_type, [])
                st.markdown(f"### {reco_type}")
                if articles:
                    df = pd.DataFrame(articles, columns=["Article ID"])
                    st.dataframe(df)
                else:
                    st.info(f"Aucune recommandation disponible pour {reco_type}.")

        except Exception as e:
            st.error(f"Erreur lors de la récupération des recommandations : {e}")

else:
    st.info("Entrez un identifiant utilisateur et cliquez sur le bouton pour obtenir des recommandations.")
