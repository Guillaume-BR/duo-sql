import duckdb

con = duckdb.connect(database = 'data/sql_exercices_sql.duckdb', read_only = False)
test_result = con.execute("SELECT * FROM memory_state").df()
print(test_result)