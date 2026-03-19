-- theme: Group By
-- consigne: Affiche nombre de visiteurs par capteur et par jour de la semaine
-- tables: capteurs

SELECT 
    capteur_id, 
    weekday,
    SUM(visiteurs_count) AS nb_visiteurs
FROM capteurs
GROUP BY capteur_id, weekday
