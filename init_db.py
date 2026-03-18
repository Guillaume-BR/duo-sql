import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/sql_exercices.duckdb", read_only=False)


# -------------------------------------------
# EXERCICES LIST
# -------------------------------------------

data = {
    "exercice_name": ["beverages_and_food", "size_and_trademark", "beverages_and_food_sum", "ventes_group_by", "retail_group_by1", "retail_group_by2"],
    "theme": ["Joins", "Joins", "Joins", "Group By", "Group By","Group By"],
    "consigne": [
        "Affiche toutes les combinaisons possibles entre les boissons et les aliments",
        "Affiche toutes les combinaisons possibles entre les tailles et les marques",
        "Affiche les combinaisons possibles entre les boissons et les aliments avec le prix total de chaque combinaison remisé de 10%",
        "Affiche le montant total des ventes par client",
        "Affiche le nombre total de transactions par secteur d'activité le jour 6 de la semaine.",
        "Affiche la moyenne des transactions par jour de semaine dans le magasin de Paris."
    ],
    "tables": [["beverages", "food_items"], ["size", "trademark"], ["beverages", "food_items"], ["ventes"], ["retail"]],
    "last_reviewed": ["2000-01-02", "2000-01-01", "1999-01-02","2000-01-03","2000-01-04"],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")


# ----------------------------------------------
# CROSS JOIN EXERCISE TABLES
# ----------------------------------------------

beverages = """
beverage,price
Orange juice,2.5
Expresso,2
Tea,3
Cappuccino,1.6
"""

food_items = """
food_item,price
Cookie juice,2.5
Chocolatine,2
Muffin,3
Croissant,1.6
"""

beverages = pd.read_csv(io.StringIO(beverages))
food_items = pd.read_csv(io.StringIO(food_items))
con.execute("CREATE OR REPLACE TABLE beverages AS SELECT * FROM beverages")
con.execute("CREATE OR REPLACE TABLE food_items AS SELECT * FROM food_items")


size = """
size
XS
S
M
L
XL
"""

trademark = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""

size = pd.read_csv(io.StringIO(size))
trademark = pd.read_csv(io.StringIO(trademark))
con.execute("CREATE OR REPLACE TABLE size AS SELECT * FROM size")
con.execute("CREATE OR REPLACE TABLE trademark AS SELECT * FROM trademark")


#-----------------------------------------------
# GROUP BY EXERCISE TABLES
#-----------------------------------------------

clients = ["Oussama", "Julie", "Chris", "Tom"]
ventes = [120, 49, 35, 23, 19, 5.99, 20, 18.77, 39, 10, 17, 12]
ventes = pd.DataFrame(ventes)
ventes.columns = ["montant"]
ventes["client"] = clients * 3

con.execute("CREATE OR REPLACE TABLE ventes AS SELECT * FROM ventes")


retail = pd.read_csv('data/retail.csv', sep=',')
con.execute("CREATE OR REPLACE TABLE retail AS SELECT store_name,month,day_of_week,market_type,quarterhour,n_lines AS nb_transac FROM retail")

football = pd.read_csv('data/football.csv',sep=',')
con.execute("CREATE OR REPLACE TABLE football AS SELECT Date,HomeTeam,AwayTeam,FTHG as GoalsHomeTeam,FTAG as GoalsAwayTeam FROM football")

appartements = pd.read_csv('data/appartements.csv',sep=',')
con.execute("CREATE OR REPLACE TABLE appartements AS SELECT * FROM appartements")

ventes = pd.read_csv('data/ventes.csv',sep=',')
con.execute("CREATE OR REPLACE TABLE ventes AS SELECT * FROM ventes")

products = pd.read_csv('data/products.csv',sep=',')
con.execute("CREATE OR REPLACE TABLE products AS SELECT * FROM products")

univers_categorie = pd.read_csv('data/univers_categorie.csv',sep=',')
con.execute("CREATE OR REPLACE TABLE univers_categorie   AS SELECT * FROM univers_categorie")

# Define the furniture data
furniture_data = [
    ("Chairs", "Chair 1", 5.2),
    ("Chairs", "Chair 2", 4.5),
    ("Chairs", "Chair 3", 6.8),
    ("Sofas", "Sofa 1", 25.5),
    ("Sofas", "Sofa 2", 20.3),
    ("Sofas", "Sofa 3", 30.0),
    ("Tables", "Table 1", 15.0),
    ("Tables", "Table 2", 12.5),
    ("Tables", "Table 3", 18.2),
]

# Create a pandas DataFrame from the predefined data
furniture = pd.DataFrame(furniture_data, columns=["category", "item", "weight"])
con.execute("CREATE OR REPLACE TABLE furniture AS SELECT * FROM furniture")

wages = pd.read_csv('data/salaires.csv',sep=',')
con.execute("CREATE OR REPLACE TABLE wages AS SELECT * FROM wages")

#On ferme la connexion à la base de données
con.close()
