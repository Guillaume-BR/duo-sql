import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/sql_exercices_sql.duckdb", read_only=False)


# -------------------------------------------
# EXERCICES LIST
# -------------------------------------------

data = {
    "theme": ["Joins", "Windows Functions"],
    "exercice_name": ["beverages_and_food", "simple_windows"],
    "tables": [["beverages", "food_items"], ["simple_windows_table"]],
    "last_reviewed": ["2000-01-01", "2000-01-01"],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# ----------------------------------------------
# CROSS JOIN EXERCISE TABLES
# ----------------------------------------------

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
Cappuccino,1.6
"""

beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
croissant,1.6
"""

food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")
