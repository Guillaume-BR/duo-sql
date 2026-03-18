--Trouver le pourcentage de changement du nombre de visiteurs d'une semaine sur l'autre 
--pour le même jour et le même capteur 
SELECT 
    *,
    LAG(visiteurs_count) 
        OVER(PARTITION BY capteurs_id, weekday
             ORDER BY date) AS lag_visiteurs_count,
     visiteurs_count - lag_visiteurs_count AS diff_visiteurs_count,
    ROUND(diff_visiteurs_count / lag_visiteurs_count * 100, 2) AS pct_change
FROM capteurs

