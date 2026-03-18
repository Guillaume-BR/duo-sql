-- trouver les ventes qui n'ont pas d'Univers
SELECT * 
FROM ventes
LEFT JOIN categorie_produit USING(produit_id)
LEFT JOIN univers_categorie USING(categorie_id)
WHERE univers_id IS NULL
