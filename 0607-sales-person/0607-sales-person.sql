/* Write your T-SQL query statement below */
SELECT  T1.name
FROM    SalesPerson T1
LEFT JOIN   Orders T2
    ON  T2.sales_id =   T1.sales_id
LEFT JOIN   Company T3
    ON  T3.com_id   =   T2.com_id
GROUP BY
        T1.sales_id
    ,   T1.name
HAVING  SUM(CASE WHEN T3.name = 'RED' THEN 1 ELSE 0 END) = 0