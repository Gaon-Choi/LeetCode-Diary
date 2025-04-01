# Write your MySQL query statement below
SELECT  T1.product_id               AS product_id
    ,   IFNULL(T2.new_price, 10)    AS price
FROM    (
    SELECT  DISTINCT
            product_id
    FROM    Products TT1
) T1
LEFT JOIN   (
    SELECT  product_id
        ,   new_price
        ,   RANK() OVER (PARTITION BY TT1.product_id ORDER BY TT1.change_date DESC) AS rn
    FROM    Products TT1
    WHERE   TT1.change_date <= '2019-08-16'
) T2
    ON  T2.product_id   =   T1.product_id
    AND T2.rn           =   1
ORDER BY
        NULLIF(T2.new_price, 10)    DESC