-- theme: Mix
-- consigne: Affiche le nombre de transactions à Madrid la semaine et le WE
-- tables: retail

SELECT 
    CASE 
        WHEN day_of_week >= 6 THEN 'Weekend'
        ELSE 'Weekday'
    END AS type_day,
    AVG(nb_transac) AS avg_transac
FROM retail
WHERE store_name = 'Madrid'
GROUP BY type_day;