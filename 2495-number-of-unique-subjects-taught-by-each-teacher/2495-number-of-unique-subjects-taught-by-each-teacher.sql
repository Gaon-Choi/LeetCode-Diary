# Write your MySQL query statement below
SELECT  teacher_id
    ,   COUNT(DISTINCT T1.subject_id)    AS 'cnt'
FROM    Teacher T1
GROUP BY
        T1.teacher_id