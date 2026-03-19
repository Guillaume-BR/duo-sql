-- theme: Group By
-- consigne: Affiche le montant des achats par clients
-- tables: ventes

SELECT 
    client, 
    SUM(montant)
FROM achats
GROUP BY client