import io
import os
import pandas as pd
import duckdb

con = duckdb.connect(database="bdd/sql_exercices.duckdb", read_only=False)


#Création 
REQUIRED_METADATA = {"theme", "consigne", "tables"}

def parse_sql_file(filepath):
    """
    Fonction pour parser les fichiers sql présents dans le dossier data et récupérer si possible les métadonnées
    """
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    metadata = {}
    for line in lines:
        if line.startswith("--"):
            key, _, value = line[3:].strip().partition(":")
            metadata[key.strip()] = value.strip()
    
    missing = REQUIRED_METADATA - metadata.keys()
    if missing:
        raise ValueError(f"Métadonnées manquantes dans {filepath} : {missing}")
    
    metadata["exercice_name"] = os.path.basename(filepath)[:-4]
    metadata["tables"] = metadata.get("tables", "").split(", ")
    metadata["last_reviewed"] = "2000-01-01"
    return metadata

rows = []
for f in sorted(os.listdir("answers")):
    if f.endswith(".sql"):
        try:
            rows.append(parse_sql_file(f"answers/{f}"))
        except ValueError as e:
            logging.warning(f"Fichier ignoré : {e}")

memory_state_df = pd.DataFrame(rows)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")


for files in os.listdir("data"):
    if files.endswith(".csv"):
        name = files[:-4]
        df = pd.read_csv(f"data/{files}")
        con.execute(f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM df")

#On ferme la connexion à la base de données
con.close()
