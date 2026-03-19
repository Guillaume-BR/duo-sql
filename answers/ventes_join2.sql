-- theme: Joins
-- consigne: Lister toutes les ventes avec le nom du produit
-- tables: ventes, products

SELECT v.date, v.produit_id, p.nom, v.quantite_vendue, v.montant_total
FROM ventes v
JOIN products p
    ON v.produit_id = p.produit_id;