-- Transactions par nombre de pièces principales

SELECT 
    Nombre_pieces_principales, 
    COUNT(*) AS nb_transactions
FROM appartements
GROUP BY Nombre_pieces_principales
ORDER BY Nombre_pieces_principales;