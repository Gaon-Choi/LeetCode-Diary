# Write your MySQL query statement below
SELECT  user_id
    ,   time_stamp  AS last_stamp
FROM    (
    SELECT  user_id
        ,   time_stamp
        ,   ROW_NUMBER() OVER (PARTITION BY TT1.user_id ORDER BY TT1.time_stamp DESC) AS rn
    FROM    Logins TT1
    WHERE   YEAR(TT1.time_stamp) = 2020
) T1
WHERE   T1.rn   =   1