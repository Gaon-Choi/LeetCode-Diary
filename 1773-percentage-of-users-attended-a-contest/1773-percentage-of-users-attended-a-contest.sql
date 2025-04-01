SELECT  T1.contest_id AS contest_id
    ,   ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM    Register T1
GROUP BY
        T1.contest_id
ORDER BY
        percentage      DESC
    ,   T1.contest_id   ASC