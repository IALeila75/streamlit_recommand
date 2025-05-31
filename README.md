
# RecoStreamlitApp – MVP de recommandation d’articles

Ce projet est un MVP fonctionnel de système de recommandation d’articles, développé dans le cadre de la construction d’un produit par une start-up fondée par Leïla (CTO) et Samia (CEO).

---

##  Fonctionnalité principale

> "En tant qu’utilisateur de l’application, je vais recevoir une sélection de cinq articles."

L’utilisateur choisit un `user_id` et une méthode de recommandation. Il reçoit ensuite les 5 articles les plus pertinents selon :

-  Collaborative filtering
-  Embedding vectoriel
-  Similarité d’articles

---

## Architecture retenue

-  Système de recommandation exposé via **Azure Functions** (serverless)
-  Interface utilisateur simple via **Streamlit Cloud**
-  Données pré-chargées : fichiers `.csv` + `.pickle`
-  Requêtes HTTP entre front et backend

---

##  Structure du dépôt

```
.
├── streamlit_app.py           # Application Streamlit (frontend)
├── requirements.txt           # Dépendances (streamlit, requests)
└── .gitignore                 # Fichiers ignorés
```

---

## ️ Lancer l'application en local

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

##  Déploiement cloud

- **Backend Azure Function** : [https://apprecommand25.azurewebsites.net/api/reco_all](https://apprecommand25.azurewebsites.net/api/reco_all)
- **Frontend Streamlit Cloud** : *(à compléter après déploiement)*

---

##  Exemple d'appel API

```bash
GET /api/reco_all?user_id=18&method=embed
```

Réponse :
 
```json
{
  "user_id": 18,
  "embedding": [{"article_id": 1001, "category_id": 1}, ...],
  "similar": [{"article_id": 1003, "category_id": 2}, ...],
  "collaborative": []
}
```

---

##  Perspectives d'évolution

- Intégration de feedback utilisateur (like/dislike)
- Ajout de nouveaux articles et utilisateurs dynamiquement
- Pipeline de mise à jour des recommandations
