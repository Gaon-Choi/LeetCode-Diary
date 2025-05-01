/* Write your T-SQL query statement below */
SELECT  TOP 1
        id
    ,   num =   SUM(num)
FROM    (
    SELECT  id  =   requester_id
        ,   num =   COUNT(*)
    FROM    RequestAccepted T1
    GROUP BY
            T1.requester_id

    UNION ALL

    SELECT  id  =   accepter_id
        ,   num =   COUNT(*)
    FROM    RequestAccepted T1
    GROUP BY
            T1.accepter_id
) T
GROUP BY
        T.id
ORDER BY
        SUM(num)    DESC