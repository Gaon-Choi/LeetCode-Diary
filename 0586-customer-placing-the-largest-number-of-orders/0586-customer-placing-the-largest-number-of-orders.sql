# Write your MySQL query statement below
SELECT  customer_number
FROM    (
    SELECT  customer_number
        ,   COUNT(*)    AS number_of_orders
    FROM    Orders TT1
    GROUP BY
            TT1.customer_number
) T1
ORDER BY
        T1.number_of_orders DESC
LIMIT   1