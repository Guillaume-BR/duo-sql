-- theme: Group By
-- consigne: Affiche le podium des magasins par nombre de transactions
-- tables: retail

SELECT 
    store_name, 
    SUM(nb_transac) AS total_transac
FROM retail
GROUP BY store_name
ORDER BY total_transac DESC
LIMIT 3;