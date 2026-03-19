-- theme: Group By
-- consigne: Affiche le classement décroissant du nombre de transactions selon le nombre de pièces
-- tables: appartements

SELECT 
    Nombre_pieces_principales, 
    COUNT(*) AS nb_transactions
FROM appartements
GROUP BY Nombre_pieces_principales
ORDER BY nb_transactions DESC;