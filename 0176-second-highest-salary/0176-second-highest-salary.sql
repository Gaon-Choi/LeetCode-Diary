# Write your MySQL query statement below
SELECT  MAX(T.salary)  AS 'SecondHighestSalary'
FROM    (
    SELECT  salary
        ,   DENSE_RANK()  OVER (ORDER BY T1.salary DESC)  AS 'rank'
    FROM    Employee T1
) T
WHERE   T.rank = 2