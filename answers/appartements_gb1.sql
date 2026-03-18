--Classement du prix moyen au m2 par commune
SELECT 
    Commune, 
    AVG(valeur_fonciere / Surface_Carrez_du_1er_lot) AS prix_m2
FROM appartements
GROUP BY Commune
ORDER BY prix_m2 DESC;