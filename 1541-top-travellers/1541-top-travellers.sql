# Write your MySQL query statement below
SELECT  T1.name
    ,   SUM(IFNULL(T2.distance, 0))    AS 'travelled_distance'
FROM    Users T1
LEFT JOIN   Rides T2
    ON  T2.user_id = T1.id
GROUP BY
        T1.id
ORDER BY
        travelled_distance  DESC
    ,   T1.name             ASC