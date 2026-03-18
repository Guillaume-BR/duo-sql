--Trouver le nombre de visiteurs par capteurs
SELECT 
    capteur_id, 
    SUM(visiteurs_count) AS nb_visiteurs
FROM capteur
GROUP BY capteur_id
