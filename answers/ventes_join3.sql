--Lister toutes les ventes, même si le produit n’existe plus
SELECT v.date, v.produit_id, p.nom, v.quantite_vendue, v.montant_total
FROM ventes v
LEFT JOIN products p
    ON v.produit_id = p.produit_id;