-- theme: Windows Functions
-- consigne: Ajouter la différence et le pourcentage de différence de visiteurs entre deux mêmes jours de la semaine consécutifs pour chaque capteur
-- tables: capteurs

SELECT 
    *,
    LAG(visiteurs_count) 
        OVER(PARTITION BY capteurs_id, weekday
             ORDER BY date) AS lag_visiteurs_count,
     visiteurs_count - lag_visiteurs_count AS diff_visiteurs_count,
    ROUND(diff_visiteurs_count / lag_visiteurs_count * 100, 2) AS pct_change
FROM capteurs

