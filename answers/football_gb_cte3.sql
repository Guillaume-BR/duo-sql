-- theme: Mix
-- consigne: Afficher le classement du championnat de football et le nombre de points (victoire = 3, match nul = 1, défaite = 0)
-- tables: football


-- 
WITH points AS (
    SELECT
        HomeTeam AS Team,
        CASE 
            WHEN GoalsHomeTeam > GoalsAwayTeam THEN 3
            WHEN GoalsHomeTeam = GoalsAwayTeam THEN 1
            ELSE 0
        END AS Points
    FROM football

    UNION ALL

    SELECT
        AwayTeam AS Team,
        CASE 
            WHEN GoalsAwayTeam > GoalsHomeTeam THEN 3
            WHEN GoalsHomeTeam = GoalsAwayTeam THEN 1
            ELSE 0
        END AS Points
    FROM football
)

SELECT
    Team,
    SUM(Points) AS Total_Points
FROM points
GROUP BY Team
ORDER BY Total_Points DESC;