-- Convertir 1 à 7 en lundi à dimanche
SELECT 
    *,
    CASE 
        WHEN day_of_week = 1 THEN 'Lundi'
        WHEN day_of_week = 2 THEN 'Mardi'
        WHEN day_of_week = 3 THEN 'Mercredi'
        WHEN day_of_week = 4 THEN 'Jeudi'
        WHEN day_of_week = 5 THEN 'Vendredi'
        WHEN day_of_week = 6 THEN 'Samedi'
        WHEN day_of_week = 7 THEN 'Dimanche'
    END AS day_name
FROM retail