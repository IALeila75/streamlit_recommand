Système de Recommandation d'Articles
====================================

Cette application est un système de recommandation d’articles, développé en Python et déployé en mode serverless sur Azure Functions. L’interface utilisateur est réalisée avec Streamlit.

------------------------------------
Fonctionnalités
------------------------------------
- Exploration des données (visualisation des clics utilisateurs et des métadonnées des articles)
- Trois méthodes de recommandation intégrées :
  * ALS (filtrage collaboratif)
  * Embeddings (similarité sémantique)
  * Similarité d’articles (proximité de contenu)
- Évaluation des performances via des métriques comparatives (Précision@10, Rappel@10, F1-score)
- API Azure Function pour générer les recommandations
- Interface interactive Streamlit pour tester les recommandations

------------------------------------
Structure du projet
------------------------------------
streamlit_recommand/
│
├── app.py                  -> Application Streamlit principale
├── requirements.txt        -> Dépendances Python
├── data/                   -> Dossier de données (CSV, Pickle, etc.)
│
├── README.txt              -> Ce fichier
└── .gitignore              -> Fichiers et dossiers à ignorer par Git

------------------------------------
Installation
------------------------------------
1. Clonez ce dépôt GitHub :
   git clone https://github.com/IALeila75/streamlit_recommand.git
   cd streamlit_recommand

2. Créez un environnement virtuel et activez-le :
   python -m venv venv
   # Sur Linux/Mac :
   source venv/bin/activate
   # Sur Windows :
   venv\Scripts\activate

3. Installez les dépendances :
   pip install -r requirements.txt

------------------------------------
Lancer l'application Streamlit
------------------------------------
streamlit run app.py

L'application sera accessible dans votre navigateur à l'adresse :
http://localhost:8501

------------------------------------
Déploiement de l'API Azure Function
------------------------------------
L’API de recommandation est déployée sur Azure Functions pour répondre aux requêtes de l’application Streamlit.

- Endpoint : https://<nom_function_app>.azurewebsites.net/api/recommendations
- Paramètres : user_id et type (als, embeddings, similarity)

------------------------------------
Résultats des performances
------------------------------------
Les modèles de recommandation sont évalués sur trois métriques :
- Précision@10
- Rappel@10
- F1-score

Ces résultats sont visibles dans la page "Évaluation des performances" de l’application Streamlit.

------------------------------------
Contribution
------------------------------------
1. Forkez ce projet.
2. Créez une branche (git checkout -b ma-feature).
3. Commitez vos changements (git commit -m 'Ajouter une nouvelle fonctionnalité').
4. Poussez la branche (git push origin ma-feature).
5. Créez une Pull Request.

------------------------------------
Licence
------------------------------------
Ce projet est sous licence MIT.

------------------------------------
Remerciements
------------------------------------
Merci à toute l'équipe et aux contributeurs pour leur soutien et leurs retours.
N'hésitez pas à ouvrir une issue ou à contribuer au projet !
