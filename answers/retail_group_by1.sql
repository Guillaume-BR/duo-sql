-- theme: Group By
-- consigne: Affiche le nombre total de transactions par secteur d'activité le samedi (6).
-- tables: retail


-- 
SELECT 
    market_type, 
    SUM(nb_transac) AS total_transactions
FROM retail
WHERE day_of_week = 6
GROUP BY market_type;