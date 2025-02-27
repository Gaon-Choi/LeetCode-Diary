/* Write your T-SQL query statement below */
SELECT  employee_id = T1.employee_id
FROM    Employees T1
WHERE   T1.salary < 30000
    AND T1.manager_id NOT IN (
        SELECT  employee_id
        FROM    Employees TT1
    )
ORDER BY
        T1.employee_id  ASC