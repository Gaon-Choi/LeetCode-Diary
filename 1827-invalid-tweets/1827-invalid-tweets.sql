# Write your MySQL query statement below
SELECT  tweet_id
FROM    Tweets T1
WHERE   LENGTH(T1.content) > 15