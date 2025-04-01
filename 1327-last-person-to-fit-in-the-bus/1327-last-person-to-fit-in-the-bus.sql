# Write your MySQL query statement below
SELECT  T1.person_name
FROM    (
    SELECT  TT1.turn
        ,   TT1.person_id
        ,   TT1.person_name
        ,   TT1.weight
        ,   SUM(TT1.weight)  OVER (ORDER BY TT1.turn ASC) AS total_weight
    FROM    Queue TT1
) T1
WHERE   T1.total_weight <= 1000
ORDER BY
        T1.total_weight DESC
LIMIT   1