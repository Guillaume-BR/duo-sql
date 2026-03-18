SELECT beverages.beverage, 
       food_items.food_item, 
       (beverages.price + food_items.price) * 0.9 AS total_price_with_discount 
FROM beverages 
CROSS JOIN food_items