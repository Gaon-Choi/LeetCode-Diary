# Write your MySQL query statement below
SELECT  T1.name
    ,   T2.bonus
FROM    Employee T1
LEFT JOIN   Bonus T2
    ON  T2.empId    =   T1.empId
WHERE   T2.bonus IS NULL
    OR  T2.bonus < 1000