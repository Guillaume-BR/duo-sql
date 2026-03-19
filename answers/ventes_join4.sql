-- theme: Joins
-- consigne: Afficher le total des ventes par univers et produit
-- tables: ventes, products, univers_categorie

SELECT u.univers_name, p.nom AS produit, SUM(v.montant_total) AS total_ventes
FROM ventes v
JOIN products p
    ON v.produit_id = p.produit_id
JOIN univers_categorie u
    ON p.produit_id = u.categorie_id
GROUP BY u.univers_name, p.nom
ORDER BY u.univers_name, total_ventes DESC;

