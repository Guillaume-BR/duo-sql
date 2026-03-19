-- theme: Windows Functions
-- consigne: Ajoute une colonne affichant le poids cumulé croissant selon l'ordre alphabétique des meubles
-- tables: furniture

SELECT *,
SUM(weight) OVER(ORDER BY item) AS poids_total,
FROM furniture