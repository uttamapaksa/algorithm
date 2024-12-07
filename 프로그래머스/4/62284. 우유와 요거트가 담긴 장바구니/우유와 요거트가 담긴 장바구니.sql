SELECT CART_ID
FROM (
    SELECT DISTINCT CART_ID, NAME
    FROM CART_PRODUCTS
    WHERE NAME IN ('Yogurt', 'Milk')
) AS A
GROUP BY CART_ID
HAVING COUNT(*) > 1
ORDER BY CART_ID