-- Classement des salires des employés seln le sexe par ordre décroissant

SELECT *,
DENSE_RANK() OVER(
    PARTITION BY department 
    ORDER BY wage DESC) AS index
FROM wages