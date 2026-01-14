import io
import streamlit as st
import pandas as pd
import duckdb

with st.sidebar:
    option = st.selectbox(
        "Que veux tu réviser  ?",
        ("Joins", "Group By", "Windows Functions"),
        index=None,
        placeholder="Choisis une option",
    )

    st.write("Options sélectionnée :", option)

st.write(
    """# Duo SQL App
         Pratiquez le SQL et progresser grâce au système de répétition espacée !
         """
)

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
Cappuccino,1.6
"""

beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
croissant,1.6
"""

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""


sql_query = st.text_area("Entrez du texte là", key="user_input")
if sql_query:
    result = duckdb.query(sql_query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    st.write("### Beverages Table")
    st.dataframe(beverages)

    st.write("### Food Items Table")
    st.dataframe(food_items)

    st.write("attendus:")
    st.dataframe(duckdb.query(answer).df())

with tab3:
    st.write("### Solution")
    st.code(answer, language="sql")
