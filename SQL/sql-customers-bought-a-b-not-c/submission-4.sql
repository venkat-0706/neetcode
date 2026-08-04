WITH cte AS (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(CASE WHEN product_name = 'A' THEN 1 END) > 0
       AND COUNT(CASE WHEN product_name = 'B' THEN 1 END) > 0
       AND COUNT(CASE WHEN product_name = 'C' THEN 1 END) = 0
)
SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM cte
)
ORDER BY customer_name