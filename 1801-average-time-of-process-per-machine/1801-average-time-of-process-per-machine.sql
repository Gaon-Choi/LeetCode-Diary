# Write your MySQL query statement below
SELECT  T1.machine_id           AS  machine_id
    ,   ROUND(AVG(T1.diff), 3)  AS  processing_time
FROM    (
    SELECT  machine_id
        ,   process_id
        ,   MAX(TT1.timestamp) - MIN(TT1.timestamp) AS diff
    FROM    Activity TT1
    GROUP BY
            TT1.machine_id
        ,   TT1.process_id
) T1
GROUP BY
        T1.machine_id