-- theme: Group By
-- consigne: Affiche le nombre de transactions par quart d'heure
-- tables: retail

SELECT 
    quarterhour, 
    AVG(nb_transac) AS avg_transac
FROM retail
GROUP BY quarterhour
ORDER BY quarterhour;