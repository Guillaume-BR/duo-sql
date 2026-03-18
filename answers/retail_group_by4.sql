-- Activité par tranche horaire
SELECT 
    quarterhour, 
    AVG(nb_transac) AS avg_transac
FROM retail
GROUP BY quarterhour
ORDER BY quarterhour;