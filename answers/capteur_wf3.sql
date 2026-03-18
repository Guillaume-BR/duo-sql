--Trouver la moyenne mobile sur les 7 derniers même jour de la semaine du nombre de visiteurs selon le capteur
--et créer un seuil à 80 % de cette moyenne mobile
SELECT 
    capteurs.*,
    AVG(visiteurs_count) 
        OVER(
            PARTITION BY capteur_id, weekday
            ORDER BY date 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) AS moving_avg,
    0.8 * moving_avg AS seuil
FROM capteurs
