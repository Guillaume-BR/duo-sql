import streamlit as st
import pandas as pd
import duckdb

with st.sidebar:
    option = st.selectbox(
    "Que veux tu réviser  ?",
    ("Joins", "Group By", "Windows Functions"),
    index=None,
    placeholder="Select contact method...",
)

    st.write("Options sélectionnée :", option)

st.write("""# Duo SQL App
         Pratiquez le SQL et progresser grâce au système de répétition espacée !
         """)



data = {"a": [1, 2, 3], "b": [4, 5, 6]}

df = pd.DataFrame(data)

st.slider("Select a number", 0, 100, 50)

st.dataframe(df)

sql_query = st.text_area("Entrez du texte ici")
result = duckdb.query(sql_query).df()

st.write(f"Vous avez entré : {sql_query}")

st.dataframe(result)
