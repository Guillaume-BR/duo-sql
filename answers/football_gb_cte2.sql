-- theme: CTE
-- consigne: Afficher le total décroissants du nombre de buts de chaque équipe
-- tables: football

WITH goals_team AS (
    SELECT HomeTeam AS team, GoalsHomeTeam AS goals FROM football
    UNION ALL
    SELECT AwayTeam AS team, GoalsAwayTeam AS goals FROM football
)

SELECT team, SUM(goals) AS total_goals
FROM goals_team
GROUP BY team
ORDER BY total_goals DESC;