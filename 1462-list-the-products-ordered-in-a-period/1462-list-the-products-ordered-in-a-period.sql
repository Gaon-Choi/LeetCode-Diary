/* Write your T-SQL query statement below */
SELECT  product_name    =   T1.product_name
    ,   unit            =   SUM(ISNULL(T2.unit, 0))
FROM    Products T1
JOIN    Orders T2
    ON  T2.product_id   =   T1.product_id
WHERE   YEAR(T2.order_date)     =   2020
    AND MONTH(T2.order_date)    =   2
GROUP BY
        T1.product_name
HAVING  SUM(ISNULL(T2.unit, 0)) >=  100