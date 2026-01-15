import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/sql_exercices_sql.duckdb", read_only=False)


# -------------------------------------------
# EXERCICES LIST
# -------------------------------------------

data = {
    "theme": ["Joins", "Joins"],
    "exercice_name": ["beverages_and_food","size_and_trademark"],
    "tables": [["beverages", "food_items"], ["size", "trademark"]],
    "last_reviewed": ["2000-01-02", "2000-01-01"],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")


# ----------------------------------------------
# CROSS JOIN EXERCISE TABLES
# ----------------------------------------------

beverages= """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
Cappuccino,1.6
"""

beverages = pd.read_csv(io.StringIO(beverages))
con.execute("CREATE OR REPLACE TABLE beverages AS SELECT * FROM beverages")

food_items = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
croissant,1.6
"""

food_items = pd.read_csv(io.StringIO(food_items))
con.execute("CREATE OR REPLACE TABLE food_items AS SELECT * FROM food_items")


size = '''
size
XS
M
L
XL
'''

trademark = '''
trademark
Nike
Asphalte
Abercrombie
Lewis
'''

size = pd.read_csv(io.StringIO(size))
trademark = pd.read_csv(io.StringIO(trademark))
con.execute("CREATE OR REPLACE TABLE size AS SELECT * FROM size")
con.execute("CREATE OR REPLACE TABLE trademark AS SELECT * FROM trademark")