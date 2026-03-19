-- theme: Windows Functions
-- consigne: On souhaite avoir la liste des dates pour lesquelles le capteur A ou B ont dépassé les 6000 visiteurs journaliers en moyenne sur les 4 derniers jours similaires.
-- tables: capteurs

SELECT 
    *,
    AVG(visiteurs_count) 
        OVER(PARTITION BY capteur_id, weekday 
            ORDER BY date 
            ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
            ) as avg_day
FROM df
QUALIFY avg_day > 6000