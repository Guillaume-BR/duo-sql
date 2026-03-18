-- Podium des magasins par nombre de transactions
SELECT 
    store_name, 
    SUM(nb_transac) AS total_transac
FROM retail
GROUP BY store_name
ORDER BY total_transac DESC
LIMIT 5;