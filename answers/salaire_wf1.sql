-- theme: Windows Functions
-- consigne: Affiche le classement des salaires des employés selon le sexe par ordre décroissant
-- tables: wages

SELECT *,
DENSE_RANK() OVER(
    PARTITION BY department 
    ORDER BY wage DESC) AS index
FROM wages