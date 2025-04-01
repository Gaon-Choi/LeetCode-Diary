# Write your MySQL query statement below
SELECT  T1.Department   AS Department
    ,   T1.EmpName      AS Employee
    ,   T1.salary       AS Salary
FROM    (
    SELECT  TT2.name    AS Department
        ,   TT1.name    AS EmpName
        ,   TT1.salary
        ,   RANK() OVER (PARTITION BY TT1.departmentId ORDER BY TT1.salary DESC) AS rn
    FROM    Employee TT1
    JOIN    Department TT2
        ON  TT2.id   =   TT1.departmentId
) T1
WHERE   T1.rn  =   1