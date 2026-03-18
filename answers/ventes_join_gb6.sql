-- Pourcentage de chaque produit dans son univers
WITH total_univers AS (
    SELECT u.univers_name, SUM(v.montant_total) AS total_univers
    FROM ventes v
    JOIN products p
      ON v.produit_id = p.produit_id
    JOIN univers_categorie u
      ON p.produit_id = u.categorie_id
    GROUP BY u.univers_name
)
SELECT p.nom, u.univers_name, SUM(v.montant_total) AS total_produit,
       SUM(v.montant_total) * 100.0 / tu.total_univers AS pct_univers
FROM ventes v
JOIN products p
  ON v.produit_id = p.produit_id
JOIN univers_categorie u
  ON p.produit_id = u.categorie_id
JOIN total_univers tu
  ON u.univers_name = tu.univers_name
GROUP BY p.nom, u.univers_name, tu.total_univers
ORDER BY u.univers_name, pct_univers DESC;