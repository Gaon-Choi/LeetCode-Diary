# Write your MySQL query statement below
SELECT  id
    ,   movie
    ,   description
    ,   rating
FROM    Cinema T1
WHERE   id % 2 = 1
    AND description NOT LIKE '%boring%'
ORDER BY
        T1.rating DESC