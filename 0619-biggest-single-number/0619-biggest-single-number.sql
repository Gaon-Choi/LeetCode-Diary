SELECT  MAX(num)    AS num
FROM    (
    SELECT  num
        ,   COUNT(*)    AS 'count'
        ,   RANK() OVER (ORDER BY T1.num DESC)  AS 'rank'
    FROM    MyNumbers T1
    GROUP BY
            T1.num
) T
WHERE   T.count = 1
