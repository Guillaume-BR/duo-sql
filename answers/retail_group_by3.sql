-- theme: Group By
-- consigne: Affiche le nombre de transactions par magasin et par mois
-- tables: retail

SELECT 
    store_name, 
    month, 
    SUM(nb_transac) AS total_transac
FROM retail
GROUP BY store_name, month;