# Write your MySQL query statement below
SELECT  DISTINCT
        T1.num  AS ConsecutiveNums
FROM    Logs T1
JOIN    Logs T2
    ON  T2.id   =   T1.id - 1
    AND T2.num  =   T1.num
JOIN    Logs T3
    ON  T3.id   =   T2.id - 1
    AND T3.num  =   T2.num