-- Transactions par magasin et mois
SELECT 
    store_name, 
    month, 
    SUM(nb_transac) AS total_transac
FROM retail
GROUP BY store_name, month;