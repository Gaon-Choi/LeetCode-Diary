/* Write your T-SQL query statement below */
SELECT  Department
    ,   Employee
    ,   Salary
FROM    (
    SELECT  Department  =   (SELECT name FROM Department WHERE id = T1.departmentId)
        ,   Employee    =   T1.name
        ,   Salary      =   T1.salary
        ,   Rank        =   DENSE_RANK() OVER (PARTITION BY T1.departmentId ORDER BY T1.salary DESC)
    FROM    Employee T1
    GROUP BY
            T1.departmentId
        ,   T1.name
        ,   T1.salary
) T
WHERE   T.Rank <= 3