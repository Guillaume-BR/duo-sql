import io
import streamlit as st
import pandas as pd
import duckdb

con = duckdb.connect(database="data/sql_exercices_sql.duckdb", read_only=False)

with st.sidebar:
    option = st.selectbox(
        "Que veux tu réviser  ?",
        ("Joins", "Group By", "Windows Functions"),
        index=None,
        placeholder="Choisis une option",
    )

    st.write("Options sélectionnée :", option)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{option}'").df()
    st.write("Exercice du thème sélectionné :")
    st.dataframe(exercice)

st.write(
    """# Duo SQL App
         Pratiquez le SQL et progresser grâce au système de répétition espacée !
         """
)


sql_query = st.text_area("Entrez du texte là", key="user_input")
if sql_query:
    result = con.execute(sql_query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    exercice_tables = exercice.loc[0, "tables"]
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
   exercice_name = exercice.loc[0, "exercice_name"]
   with open(f"answers/{exercice_name}.sql", "r") as file:
       ANSWER = file.read()
   st.code(ANSWER, language="sql")