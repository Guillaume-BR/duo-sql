-- Pourcentage de victoires à domicile, à l'extérieur et de matchs nuls
WITH total_matches AS (
    SELECT COUNT(*) AS total
    FROM football
),
results AS (
    SELECT
        CASE 
            WHEN GoalsHomeTeam > GoalsAwayTeam THEN "Victoire à domicile"
            WHEN GoalsHomeTeam < GoalsAwayTeam THEN "Victoire à l'extérieur"
            ELSE "Match nul"
        END AS Resultat
    FROM football
)

SELECT
    Resultat,
    COUNT(*) * 100.0 / total_matches.total AS Pourcentage
FROM results
CROSS JOIN total_matches
GROUP BY Resultat, total_matches.total;