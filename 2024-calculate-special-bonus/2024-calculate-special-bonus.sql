/* Write your T-SQL query statement below */
SELECT  employee_id =   T1.employee_id
    ,   bonus       =   CASE    WHEN T1.employee_id & 1 = 1 AND T1.name NOT LIKE 'M%' THEN T1.salary
                                ELSE 0
                        END
FROM    Employees T1
ORDER BY
        T1.employee_id  ASC