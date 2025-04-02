SELECT 
    ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM (
    SELECT 
        customer_id, 
        order_date, 
        customer_pref_delivery_date
    FROM Delivery
    WHERE (customer_id, order_date) IN (
        SELECT customer_id, MIN(order_date) 
        FROM Delivery 
        GROUP BY customer_id
    )
) AS first_orders;