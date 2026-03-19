-- theme: Group By
-- consigne: Affiche le nombre de visiteurs par capteurs
-- tables: capteurs

SELECT 
    capteur_id, 
    SUM(visiteurs_count) AS nb_visiteurs
FROM capteurs
GROUP BY capteur_id
