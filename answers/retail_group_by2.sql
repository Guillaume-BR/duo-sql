-- theme: Group By
-- consigne: Affiche la moyenne des transactions par jour de semaine dans le magasin de Paris.
-- tables: retail

SELECT 
    day_of_week, 
    AVG(nb_transac) AS avg_transac
FROM retail
WHERE store_name = 'Paris'
GROUP BY day_of_week;