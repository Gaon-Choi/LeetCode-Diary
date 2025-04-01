# Write your MySQL query statement below
SELECT  T1.employee_id
    ,   T1.name
    ,   COUNT(*)                AS reports_count
    ,   ROUND(AVG(T2.age), 0)   AS average_age
FROM    Employees T1
JOIN    Employees T2
    ON  T2.reports_to   =   T1.employee_id
GROUP BY
        T1.employee_id
ORDER BY
        T1.employee_id