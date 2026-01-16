import logging
import os
import streamlit as st
import pandas as pd
import duckdb
from datetime import datetime, timedelta

# Set up logging
if "data" not in os.listdir():
    logging.error("os.listdir()")
    logging.error("Creating data/ folder")
    os.mkdir("data")

if "sql_exercices_sql.duckdb" not in os.listdir("data"):
    logging.error("os.listdir('data/')")
    logging.error("Creating data/sql_exercices_sql.duckdb database")
    exec(open("init_db.py").read())
    # subprocess.run(["python", "init_db.py"])

con = duckdb.connect(database="data/sql_exercices_sql.duckdb", read_only=False)

st.markdown(
    """# Duo SQL App
       ## Pratiquez le SQL et progressez grâce au système de répétition espacée !
         """
)

with st.sidebar:
    option = st.selectbox(
        "Que veux tu réviser  ?",
        ["Joins", "Group By", "Windows Functions"],
        index=None,
        placeholder="Choisis une option",
    )

    st.write("Options sélectionnée :", option)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{option}'").df().sort_values("last_reviewed").reset_index(drop=True)
    st.write("Exercice du thème sélectionné :")
    st.dataframe(exercice)
    
    exercice_name = exercice.loc[0, "exercice_name"]
    with open(f"answers/{exercice_name}.sql", "r") as file:
        ANSWER = file.read()
    
    solution_df = con.execute(ANSWER).df()

st.header("Tapez votre code SQL ci-dessous")
sql_query = st.text_area("Entrez du texte là", key="user_input")
if sql_query:
    result = con.execute(sql_query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Certaines colonnes sont manquantes")
 
tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    exercice_tables = exercice.loc[0, "tables"]
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    st.code(ANSWER, language="sql")
