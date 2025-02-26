# Write your MySQL query statement below
SELECT  product_name
    ,   year
    ,   price
FROM    Product T1
JOIN    Sales   T2
    ON  T2.product_id = T1.product_id
