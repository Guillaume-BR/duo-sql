-- theme: Joins
-- consigne: Affiche les combinaisons possibles entre les boissons et les aliments avec le prix total de chaque combinaison remisé de 10%
-- tables: beverages, food_items

SELECT 
       beverages.beverage, 
       food_items.food_item, 
       (beverages.price + food_items.price) * 0.9 AS total_price_with_discount 
FROM beverages 
CROSS JOIN food_items