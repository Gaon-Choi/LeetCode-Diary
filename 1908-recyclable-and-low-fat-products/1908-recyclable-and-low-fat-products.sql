# Write your MySQL query statement below
SELECT  product_id
FROM    Products T1
WHERE   T1.low_fats     = 'Y'
    AND T1.recyclable   = 'Y'