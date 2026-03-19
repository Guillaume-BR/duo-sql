-- theme: Windows Functions
-- consigne: Affiche la moyenne glissante du nombre de visiteurs par capteur et par jour de la semaine
-- tables: capteurs

SELECT 
    capteur_id, 
    weekday,
    AVG(visiteurs_count) OVER (PARTITION BY capteur_id ORDER BY date) AS moyenne_glissante
FROM capteurs
