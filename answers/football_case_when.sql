-- theme: Case When
-- consigne: Ajouter une colonne avec le nom du vainqueur du match
-- tables: football

SELECT 
    *,
    CASE 
        WHEN GoalsHomeTeam > GoalsAwayTeam THEN HomeTeam
        WHEN GoalsHomeTeam < GoalsAwayTeam THEN AwayTeam
        ELSE 'Egalité'
    END AS Vainqueur
FROM football;