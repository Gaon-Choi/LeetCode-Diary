# Write your MySQL query statement below
SELECT  customer_id
    ,   COUNT(T1.visit_id) - COUNT(T2.visit_id)    AS 'count_no_trans'
FROM    Visits T1
LEFT JOIN   Transactions T2
    ON  T2.visit_id = T1.visit_id
GROUP BY
        T1.customer_id
HAVING  COUNT(T1.visit_id) - COUNT(T2.visit_id) > 0