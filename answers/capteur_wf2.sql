--Trouver la moyenne glissante sur les 7 derniers jours des visiteurs selon le capteur
SELECT 
    capteurs.*,
    AVG(visiteurs_count) 
        OVER(
            PARTITION BY capteur_id
            ORDER BY date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) AS moving_avg
FROM capteurs
