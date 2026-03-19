-- theme: Windows Functions
-- consigne: Affiche le nombre de visiteurs et le classement des capteurs par semaine
-- tables: capteurs

WITH total_per_week AS (
SELECT 
    capteur_id,
    WEEK(TRY_CAST(date AS DATE)) AS week,
    SUM(visiteurs_count) AS total_visiteurs
FROM df
GROUP BY week, capteur_id
)

SELECT
    *,
    DENSE_RANK() OVER(PARTITION BY week ORDER BY total_visiteurs DESC) as index
FROM total_per_week
ORDER BY week, index