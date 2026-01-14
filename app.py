import io
import streamlit as st
import pandas as pd
import duckdb

con = duckdb.connect(database = 'data/sql_exercices_sql.duckdb', read_only = False)

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


answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""


sql_query = st.text_area("Entrez du texte là", key="user_input")
if sql_query:
    result = con.execute(sql_query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
   exercice_tables = exercice.loc[0,"tables"]
   for table in exercice_tables:
     st.write(f"table: {table}")
     df_table = con.execute(f"SELECT * FROM {table}").df()
     st.dataframe(df_table)

#with tab3:
#    st.write("### Solution") 
#    st.code(answer, language="sql")
#