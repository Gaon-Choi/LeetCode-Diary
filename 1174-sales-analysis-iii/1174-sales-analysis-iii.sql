/* Write your T-SQL query statement below */
SELECT  product_id
    ,   product_name
FROM    (
    SELECT  T1.product_id
        ,   T1.product_name
        ,   cnt1    =   COUNT(CASE WHEN T2.sale_date BETWEEN '2019-01-01' AND '2019-03-31' THEN 1 END)
        ,   cnt2    =   COUNT(*)
    FROM    Product T1
    JOIN    Sales T2
        ON  T2.product_id   =   T1.product_id
    GROUP BY
            T1.product_id
        ,   T1.product_name
) T
WHERE   cnt1 = cnt2