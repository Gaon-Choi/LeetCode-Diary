/* Write your T-SQL query statement below */
SELECT  T2.unique_id
    ,   T1.name
FROM    Employees T1
LEFT JOIN   EmployeeUNI T2
    ON  T2.id   = T1.id
