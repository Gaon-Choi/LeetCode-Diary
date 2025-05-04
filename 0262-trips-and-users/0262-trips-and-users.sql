# Write your MySQL query statement below
SELECT  T1.request_at   AS  'Day'
    ,   ROUND(COUNT(CASE WHEN T1.status LIKE 'cancelled%' THEN 1 END) / COUNT(*), 2)    AS  'Cancellation Rate'
FROM    Trips AS T1
LEFT JOIN   Users AS T2
    ON  T2.users_id =   T1.client_id
    AND T2.role     =   'client'
LEFT JOIN   Users AS T3
    ON  T3.users_id =   T1.driver_id
    AND T3.role     =   'driver'
WHERE   T2.banned   =   'No'
    AND T3.banned   =   'No'
    AND T1.request_at   >=  '2013-10-01'
    AND T1.request_at   <   '2013-10-04'
GROUP BY
        T1.request_at
ORDER BY
        T1.request_at