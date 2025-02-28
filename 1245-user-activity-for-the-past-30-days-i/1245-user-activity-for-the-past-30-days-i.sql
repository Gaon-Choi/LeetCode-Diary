/* Write your T-SQL query statement below */
SELECT  day             =   T1.activity_date
    ,   active_users    =   COUNT(DISTINCT T1.user_id)
FROM    Activity T1
WHERE   T1.activity_DATE    > DATEADD(DAY, -30, '2019-07-27')
    AND T1.activity_DATE    <= '2019-07-27'
GROUP BY
        T1.activity_date