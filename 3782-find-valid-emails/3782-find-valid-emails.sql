# Write your MySQL query statement below
SELECT  user_id
    ,   email
FROM    Users T1
WHERE   T1.email    REGEXP '^[a-zA-Z0-9_]*@[a-zA-Z]*\.com$'
ORDER BY
        T1.user_id