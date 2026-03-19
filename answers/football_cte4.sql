-- theme: CTE
-- consigne: Trouver l’équipe la plus défensive
-- tables: football

WITH goals_team AS (
    SELECT HomeTeam AS team, GoalsAwayTeam AS goals FROM football
    UNION ALL
    SELECT AwayTeam AS team, GoalsHomeTeam AS goals FROM football
)

SELECT 
    team, 
    SUM(goals) AS total_goals
FROM goals_team
GROUP BY team
ORDER BY total_goals ASC
LIMIT 1;