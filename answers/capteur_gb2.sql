--Trouver le nombre de visiteurs par capteurs et par jour
SELECT 
    capteur_id, 
    weekday,
    SUM(visiteurs_count) AS nb_visiteurs
FROM capteur
GROUP BY capteur_id, weekday
