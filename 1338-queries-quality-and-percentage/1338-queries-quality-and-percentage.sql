# Write your MySQL query statement below
SELECT  T1.query_name
    ,   ROUND(SUM(T1.rating * 1.0 / T1.position)  /   COUNT(*), 2)                  AS  'quality'
    ,   ROUND((SUM(CASE WHEN T1.rating < 3 THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) AS  'poor_query_percentage'
FROM    Queries T1
GROUP BY
        T1.query_name