import streamlit as st
import pandas as pd
import requests

# ========== CONFIGURATION ==========
st.set_page_config(page_title="Système de Recommandation", layout="wide")

# ========== CHARGEMENT DES DONNÉES ==========
@st.cache_data
def load_data():
    clicks_df = pd.read_csv("data/clicks_sample.csv")
    articles_df = pd.read_csv("data/articles_metadata.csv")
    return clicks_df, articles_df

clicks_df, articles_df = load_data()

# ========== SIDEBAR ==========
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisir une page :", 
                        ["Exploration des données", 
                         "Recommandations", 
                         "Évaluation des performances"])

# ========== PAGE 1 : EXPLORATION DES DONNÉES ==========
if page == "Exploration des données":
    st.title("📊 Exploration des données")
    st.subheader("Aperçu des interactions utilisateurs")
    st.dataframe(clicks_df.head())
    st.subheader("Aperçu des articles")
    st.dataframe(articles_df.head())
    st.subheader("Statistiques descriptives")
    st.write("Nombre d'utilisateurs :", clicks_df['user_id'].nunique())
    st.write("Nombre d'articles :", articles_df['article_id'].nunique())
    st.write("Nombre d'interactions :", len(clicks_df))

# ========== PAGE 2 : RECOMMANDATIONS ==========
elif page == "Recommandations":
    st.title("🎯 Recommandations personnalisées")

    if 'reco_ready' not in st.session_state:
        st.session_state.reco_ready = False

    user_id = st.text_input("Entrez votre identifiant utilisateur :", "")

    # Remplace par l'URL réelle de ton Azure Function
    base_url = "https://apprecommandes.azurewebsites.net/api/recommand_all?user_id={user_id}"

    if user_id:
        if st.button("Obtenir mes recommandations"):
            st.session_state.reco_ready = True

        if st.session_state.reco_ready:
            st.success("Choisissez votre méthode de recommandation :")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                if st.button("ALS"):
                    api_url = f"{base_url}?user_id={user_id}&type=als"
                    try:
                        response = requests.get(api_url)
                        response.raise_for_status()
                        data = response.json()
                        als_articles = data.get("ALS", [])
                        st.subheader("🔗 Recommandation ALS")
                        if als_articles:
                            st.dataframe(pd.DataFrame(als_articles, columns=["Article ID"]))
                        else:
                            st.warning("Aucune recommandation disponible pour ALS.")
                    except Exception as e:
                        st.error(f"Erreur lors de la récupération des recommandations : {e}")

            with col2:
                if st.button("Embeddings"):
                    api_url = f"{base_url}?user_id={user_id}&type=embeddings"
                    try:
                        response = requests.get(api_url)
                        response.raise_for_status()
                        data = response.json()
                        embed_articles = data.get("Embeddings", [])
                        st.subheader("🔗 Recommandation Embeddings")
                        if embed_articles:
                            st.dataframe(pd.DataFrame(embed_articles, columns=["Article ID"]))
                        else:
                            st.warning("Aucune recommandation disponible pour Embeddings.")
                    except Exception as e:
                        st.error(f"Erreur lors de la récupération des recommandations : {e}")

            with col3:
                if st.button("Similarité d’articles"):
                    api_url = f"{base_url}?user_id={user_id}&type=similarity"
                    try:
                        response = requests.get(api_url)
                        response.raise_for_status()
                        data = response.json()
                        sim_articles = data.get("Similarité", [])
                        st.subheader("🔗 Recommandation Similarité d’article")
                        if sim_articles:
                            st.dataframe(pd.DataFrame(sim_articles, columns=["Article ID"]))
                        else:
                            st.warning("Aucune recommandation disponible pour Similarité d’article.")
                    except Exception as e:
                        st.error(f"Erreur lors de la récupération des recommandations : {e}")

            with col4:
                if st.button("Toutes les recommandations"):
                    try:
                        als_api = f"{base_url}?user_id={user_id}&type=als"
                        embeddings_api = f"{base_url}?user_id={user_id}&type=embeddings"
                        sim_api = f"{base_url}?user_id={user_id}&type=similarity"

                        als_resp = requests.get(als_api)
                        embeddings_resp = requests.get(embeddings_api)
                        sim_resp = requests.get(sim_api)

                        als_articles = als_resp.json().get("ALS", [])
                        embed_articles = embeddings_resp.json().get("Embeddings", [])
                        sim_articles = sim_resp.json().get("Similarité", [])

                        st.subheader("🔗 Recommandation ALS")
                        if als_articles:
                            st.dataframe(pd.DataFrame(als_articles, columns=["Article ID"]))
                        else:
                            st.warning("Aucune recommandation disponible pour ALS.")

                        st.subheader("🔗 Recommandation Embeddings")
                        if embed_articles:
                            st.dataframe(pd.DataFrame(embed_articles, columns=["Article ID"]))
                        else:
                            st.warning("Aucune recommandation disponible pour Embeddings.")

                        st.subheader("🔗 Recommandation Similarité d’article")
                        if sim_articles:
                            st.dataframe(pd.DataFrame(sim_articles, columns=["Article ID"]))
                        else:
                            st.warning("Aucune recommandation disponible pour Similarité d’article.")

                    except Exception as e:
                        st.error(f"Erreur lors de la récupération des recommandations : {e}")
    else:
        st.info("Veuillez entrer votre identifiant utilisateur pour obtenir des recommandations.")

# ========== PAGE 3 : ÉVALUATION DES PERFORMANCES ==========
elif page == "Évaluation des performances":
    st.title("📈 Évaluation des performances")

    results = pd.DataFrame({
        'Modèle': ['ALS', 'Embeddings NumPy', 'Similarité d’article'],
        'Précision@10': [0.02, 0.03, 0.04],
        'Rappel@10': [0.11, 0.21, 0.34],
        'F1-Score': [0.03, 0.06, 0.07]
    })

    st.subheader("Tableau comparatif des modèles")
    st.dataframe(results)

    st.subheader("Visualisation des scores")
    st.bar_chart(results.set_index('Modèle'))
