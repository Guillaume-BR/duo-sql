import streamlit as st
import pandas as pd
import duckdb

st.write("Hello, streamlit!")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}

df = pd.DataFrame(data)

st.slider("Select a number", 0, 100, 50)

st.dataframe(df)

sql_query = st.text_area("Entrez du texte ici")
result = duckdb.query(sql_query).df()

st.write(f"Vous avez entré : {sql_query}")

st.dataframe(result)
