# Write your MySQL query statement below
SELECT  T1.employee_id
FROM    Employees T1
LEFT JOIN   Salaries T2
    ON  T2.employee_id  = T1.employee_id
WHERE   T2.salary IS NULL

UNION

SELECT  T2.employee_id
FROM    Employees T1
RIGHT JOIN   Salaries T2
    ON  T2.employee_id  = T1.employee_id
WHERE   T1.name IS NULL

ORDER BY
        employee_id ASC