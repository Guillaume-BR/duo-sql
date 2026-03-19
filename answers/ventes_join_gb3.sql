-- theme: Joins
-- consigne: Affiche le total décroissant des ventes par produit
-- tables: ventes, products

SELECT p.nom, SUM(v.montant_total) AS total_ventes
FROM ventes v
JOIN products p
    ON v.produit_id = p.produit_id
GROUP BY p.nom
ORDER BY total_ventes DESC;