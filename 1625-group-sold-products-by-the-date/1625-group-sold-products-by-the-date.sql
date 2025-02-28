/* Write your T-SQL query statement below */
SELECT  sell_date   =   T1.sell_date
    ,   num_sold    =   COUNT(DISTINCT T1.product)
    ,   products    =   STRING_AGG(ISNULL(T1.product, ''), ',') WITHIN GROUP(ORDER BY T1.product)
FROM    (
    SELECT  DISTINCT
            TT1.sell_date
        ,   TT1.product
    FROM    Activities TT1
)  T1
GROUP BY
        T1.sell_date
ORDER BY
        T1.sell_date    ASC