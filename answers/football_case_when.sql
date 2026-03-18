-- ajouter une colonne avec le nom du vainqueur du match
SELECT 
    *,
    CASE 
        WHEN GoalsHomeTeam > GoalsAwayTeam THEN HomeTeam
        WHEN GoalsHomeTeam < GoalsAwayTeam THEN AwayTeam
        ELSE 'Egalité'
    END AS Vainqueur
FROM football;