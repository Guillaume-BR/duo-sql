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


def verify_sql_results(sql_query: str) -> None:
    """
    Verify the results of a SQL query against the expected solution.

    :param sql_query: The SQL query to be executed and verified.
    :type sql_query: str
    """
    result = con.execute(sql_query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Certaines colonnes sont manquantes")

    n_lines_diff = result.shape[0] - solution_df.shape[0]
    if n_lines_diff != 0:
        st.write(
            f"Le nombre de lignes est différent de la solution par {n_lines_diff} lignes."
        )


con = duckdb.connect(database="data/sql_exercices_sql.duckdb", read_only=False)

st.markdown(
    """# Duo SQL App
       ## Pratiquez le SQL et progressez grâce au système de répétition espacée !
         """
)

with st.sidebar:
    available_themes = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    option = st.selectbox(
        "Que veux tu réviser  ?",
        available_themes["theme"].unique(),
        index=None,
        placeholder="Choisis une option",
    )

    if option:
        st.write("Options sélectionnée :", option)
        select_exercise_query = f"SELECT * FROM memory_state WHERE theme = '{option}'"
    else:
        select_exercise_query = "SELECT * FROM memory_state"

    exercice = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )

    st.write("Exercice du thème sélectionné :")
    st.dataframe(exercice)

    exercice_name = exercice.loc[0, "exercice_name"]
    with open(f"answers/{exercice_name}.sql", "r") as file:
        ANSWER = file.read()

    solution_df = con.execute(ANSWER).df()

st.header("Tapez votre code SQL ci-dessous")
query_user = st.text_area("Entrez du texte là", key="user_input")

col1, col2, col3, col4 = st.columns(4)

for col, days in zip([col1, col2, col3],[2,7,21]):
    if col.button(f'Revoir dans {days} jours'):
        next_review = datetime.now() + timedelta(days=days)
        con.execute(f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercice_name = '{exercice_name}'")
        st.rerun()

#bouton reset dans la col4
if col4.button('Reset'):
    con.execute(f"UPDATE memory_state SET last_reviewed = '2000-01-01' WHERE exercice_name = '{exercice_name}'")
    st.rerun()


if query_user:
    verify_sql_results(query_user)

tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    exercice_tables = exercice.loc[0, "tables"]
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    st.code(ANSWER, language="sql")
