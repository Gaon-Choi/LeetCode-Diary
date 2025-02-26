# Write your MySQL query statement below
SELECT  name
FROM    Customer T1
WHERE   T1.referee_id <> 2
    OR  T1.referee_id IS NULL