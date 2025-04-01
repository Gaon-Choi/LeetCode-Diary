# Write your MySQL query statement below
SELECT  ROUND(AVG(
        CASE    WHEN T1.order_date = T1.customer_pref_delivery_date THEN 1
                ELSE 0
        END
        ) * 100.0, 2) AS immediate_percentage
FROM    (
    SELECT  customer_id
        ,   order_date
        ,   customer_pref_delivery_date
        ,   ROW_NUMBER() OVER (PARTITION BY TT1.customer_id ORDER BY TT1.order_date ASC) AS rn
    FROM    Delivery TT1
) T1
WHERE   rn  =   1