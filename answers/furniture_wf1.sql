--affiche le poids cumulé de chaque meuble
SELECT *,
SUM(weight) OVER(ORDER BY item) AS poids_total,
FROM df