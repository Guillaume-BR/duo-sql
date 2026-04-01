# 🗄️ DuoSQL

> **Pratiquez le SQL et progressez grâce à la répétition espacée.**

DuoSQL est une application Streamlit qui vous aide à maîtriser le SQL en vous soumettant des exercices selon l'algorithme de répétition espacée — les requêtes que vous maîtrisez moins bien reviennent plus souvent, celles que vous connaissez bien s'espacent automatiquement.

---

## ✨ Fonctionnalités

- **Exercices SQL interactifs** — écrivez vos requêtes directement dans l'interface et obtenez un feedback immédiat
- **Répétition espacée** — planifiez votre prochaine révision dans 2, 7 ou 21 jours selon votre niveau de maîtrise
- **Filtrage par thème** — concentrez-vous sur un sujet précis (JOIN, GROUP BY, sous-requêtes, etc.)
- **Comparaison avec la solution** — l'app détecte les différences ligne par ligne entre votre résultat et la solution attendue
- **Visualisation des tables** — consultez les données disponibles directement dans l'interface

---

## 🚀 Installation

### Prérequis

- Python 3.9+
- [uv](https://docs.astral.sh/uv/) — gestionnaire de dépendances

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/duosql.git
cd duosql

# 2. Installer les dépendances via uv
uv sync

# 3. Initialiser la base de données
uv run python init_db.py

# 4. Lancer l'application
uv run streamlit run app.py
```

L'application est accessible sur `http://localhost:8501`.

---

## 📁 Structure du projet

```
duosql/
├── app.py              # Application principale Streamlit
├── init_db.py          # Script d'initialisation de la base
├── requirements.txt    # Dépendances Python
├── data/               # contient les csv 
├── answers/            # Fichiers .sql contenant les solutions
│   ├── exercice_1.sql
│   └── ...
└── bdd/                # Base de données DuckDB (générée automatiquement)
    └── sql_exercices.duckdb
```

---

## 🗃️ Structure de la base de données

La base DuckDB contient une table `memory_state` avec les colonnes suivantes :

| Colonne | Type | Description |
|---|---|---|
| `exercice_name` | VARCHAR | Identifiant de l'exercice |
| `consigne` | VARCHAR | Énoncé affiché à l'utilisateur |
| `theme` | VARCHAR | Thème SQL de l'exercice |
| `tables` | LIST | Tables nécessaires à l'exercice |
| `last_reviewed` | TIMESTAMP | Date de dernière révision |

---

## 🧠 Algorithme de répétition espacée

Après chaque exercice, vous choisissez quand le revoir :

| Bouton | Intervalle | Quand l'utiliser |
|---|---|---|
| ⚡ 2 jours | Court terme | Notion fragile ou erreur commise |
| 📅 7 jours | Moyen terme | Bonne réponse avec hésitation |
| 🗓️ 21 jours | Long terme | Maîtrise complète et fluide |
| ↺ Reset | Immédiat | Remettre l'exercice en tête de file |

L'exercice affiché est toujours celui dont la date de révision (`last_reviewed`) est la plus ancienne.

---

## 📦 Dépendances principales

Gérées via **uv** :

```
streamlit
duckdb
pandas
```

Pour ajouter une dépendance : `uv add nom-du-package`

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour ajouter des exercices :

1. Créez un fichier `answers/nom_exercice.sql` contenant la requête solution
2. Ajoutez une entrée dans la table `memory_state` via `init_db.py`
3. Soumettez une pull request

---

## 📄 Licence

MIT
