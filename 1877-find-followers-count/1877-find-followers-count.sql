/* Write your T-SQL query statement below */
SELECT  user_id         =   T1.user_id
    ,   followers_count =   COUNT(*)
FROM    Followers T1
GROUP BY
        T1.user_id
ORDER BY
        T1.user_id  ASC