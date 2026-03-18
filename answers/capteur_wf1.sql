--Trouver la moyenne moyenne de visiteurs sur les dates qui se met à jour progressivement 
--en fonction des résultats de la journée
SELECT 
    capteur_id, 
    weekday,
    AVG(visiteurs_count) OVER (PARTITION BY capteur_id ORDER BY date) AS moyenne_glissante
FROM capteur
