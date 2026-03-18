--Trouver l’équipe avec le meilleur goal average
WITH goals_team AS (
    SELECT HomeTeam AS team, GoalsHomeTeam AS goals_for, GoalsAwayTeam AS goals_against FROM football
    UNION ALL
    SELECT AwayTeam AS team, GoalsAwayTeam AS goals_for, GoalsHomeTeam AS goals_against FROM football
),

goal_for_against AS (
    SELECT 
        team, 
        SUM(goals_for) AS total_goals_for, 
        SUM(goals_against) AS total_goals_against,
    FROM goals_team
    GROUP BY team
)

SELECT 
    team, 
    total_goals_for - total_goals_against AS goal_average
FROM goal_for_against
ORDER BY goal_average DESC
LIMIT 1;