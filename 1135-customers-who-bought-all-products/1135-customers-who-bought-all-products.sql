# Write your MySQL query statement below
WITH UNIQUE_CUSTOMER_TBL AS (
    SELECT  DISTINCT
            customer_id
        ,   product_key
    FROM    Customer
)

SELECT  customer_id
FROM    (
    SELECT  customer_id
        ,   COUNT(TT1.product_key)  AS total_count
    FROM    UNIQUE_CUSTOMER_TBL TT1
    GROUP BY
            TT1.customer_id
) T1
WHERE   T1.total_count = (SELECT COUNT(*) FROM Product)