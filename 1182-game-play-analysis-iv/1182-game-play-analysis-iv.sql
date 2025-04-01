# Write your MySQL query statement below
SELECT  ROUND(AVG(CASE WHEN T2.player_id IS NULL THEN 0 ELSE 1 END), 2) AS fraction
FROM    (
    SELECT  TT1.player_id
        ,   TT1.device_id
        ,   MIN(TT1.event_date) AS first_event_date
    FROM    Activity TT1
    GROUP BY
            TT1.player_id
) T1
LEFT JOIN    Activity T2
    ON  T2.player_id    =   T1.player_id
    AND T2.event_date   =   DATE_ADD(T1.first_event_date, INTERVAL 1 DAY)