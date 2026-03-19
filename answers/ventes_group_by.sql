-- theme: Group By
-- consigne: Affiche le montant des ventes par clients
-- tables: ventes

SELECT 
    client, 
    SUM(montant)
FROM ventes
GROUP BY client