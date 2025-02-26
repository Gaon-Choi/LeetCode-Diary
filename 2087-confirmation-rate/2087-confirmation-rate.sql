# Write your MySQL query statement below
SELECT  T1.user_id
    ,   ROUND(AVG(IF(T2.action = 'confirmed', 1.0, 0.0)), 2)  AS 'confirmation_rate'
FROM    Signups T1
LEFT JOIN   Confirmations T2
    ON  T2.user_id  = T1.user_id
GROUP BY
        T1.user_id