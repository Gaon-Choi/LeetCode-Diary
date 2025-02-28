-- Write your MySQL query statement below
DELETE  T1
FROM    Person T1
JOIN    Person T2
    ON  T2.email    = T1.email
    AND T2.id       < T1.id