# Write your MySQL query statement below
SELECT  DISTINCT
        author_id AS 'id'
FROM    Views T1
WHERE   T1.author_id    =   T1.viewer_id
ORDER BY
        T1.author_id