-- Write your MySQL query statement below
SELECT  Id  = T1.id
FROM    Weather T1
WHERE   T1.temperature > (
    SELECT  TOP 1
            TT1.temperature
    FROM    Weather TT1
    WHERE   TT1.recordDate = DATEADD(DAY, -1, T1.recordDate)
)