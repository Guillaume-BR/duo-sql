--Classement des univers par montant total des ventes
WITH total_par_univers AS (
    SELECT u.univers_name, SUM(v.montant_total) AS total_ventes
    FROM ventes v
    JOIN products p
        ON v.produit_id = p.produit_id
    JOIN univers_categorie u
        ON p.produit_id = u.categorie_id
    GROUP BY u.univers_name
)
SELECT *, DENSE_RANK() OVER (ORDER BY total_ventes DESC) AS rank_univers
FROM total_par_univers;