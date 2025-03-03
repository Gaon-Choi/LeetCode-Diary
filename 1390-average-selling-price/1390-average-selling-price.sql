# Write your MySQL query statement below
SELECT  T1.product_id   AS product_id
    ,   IFNULL(ROUND(SUM(1.0 * T2.units * T1.price) / SUM(T2.units), 2), 0)    AS average_price
FROM    Prices T1
LEFT JOIN    UnitsSold T2
    ON  T1.product_id       =   T2.product_id
    AND T2.purchase_date    >=  T1.start_date
    AND T2.purchase_date    <=  T1.end_date
GROUP BY
        T1.product_id