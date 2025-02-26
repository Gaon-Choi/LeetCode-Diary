# Write your MySQL query statement below
SELECT  T1.name    AS 'Employee'
FROM    Employee T1
JOIN    Employee T2
    ON  T2.id = T1.managerId
WHERE   T2.salary < T1.salary