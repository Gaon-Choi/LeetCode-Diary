/* Write your T-SQL query statement below */
SELECT  name    =   T1.name
FROM    Employee T1
WHERE   T1.id IN    (
    SELECT  TT1.managerId
        -- ,   COUNT(*)
    FROM    Employee TT1
    WHERE   TT1.managerId IS NOT NULL
    GROUP BY
            TT1.managerId
    HAVING  COUNT(*)    >=  5
)