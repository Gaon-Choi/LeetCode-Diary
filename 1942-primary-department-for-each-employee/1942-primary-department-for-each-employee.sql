# Write your MySQL query statement below
SELECT  employee_id
    ,   department_id
FROM    (
    SELECT  employee_id
        ,   department_id
        -- ,   primary_flag
        ,   RANK() OVER (PARTITION BY TT1.employee_id ORDER BY TT1.primary_flag ASC) as 'rank'
    FROM    Employee TT1
) T1
WHERE   T1.rank = 1
-- WHERE   RANK() OVER (PARTITION BY T1.employee_idORDER BY T1.primary_flag DESC) = 1