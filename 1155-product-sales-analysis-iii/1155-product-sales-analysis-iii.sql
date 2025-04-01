SELECT  T1.product_id   AS product_id
    ,   T2.first_year   AS first_year
    ,   T1.quantity     AS quantity
    ,   T1.price        AS price
FROM    Sales T1
JOIN   (
    SELECT  TT1.product_id
        ,   MIN(TT1.year)   AS first_year
    FROM    Sales TT1
    GROUP BY
            TT1.product_id
) T2
    ON  T2.product_id   =   T1.product_id
    AND T2.first_year   =   T1.year