SELECT 
    client, 
    SUM(montant)
FROM ventes
GROUP BY client