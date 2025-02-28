# Write your MySQL query statement below
SELECT  T1.player_id        AS player_id
    ,   MIN(T1.event_date)  AS first_login
FROM    Activity T1
GROUP BY
        T1.player_id