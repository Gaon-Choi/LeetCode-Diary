/* Write your T-SQL query statement below */
SELECT  T1.student_id
    ,   T1.student_name
    ,   T2.subject_name
    ,   attended_exams  =   COUNT(T3.student_id)
FROM    Students T1
CROSS JOIN  Subjects T2
LEFT JOIN   Examinations T3
    ON  T3.student_id   =   T1.student_id
    AND T3.subject_name =   T2.subject_name
GROUP BY
        T1.student_id
    ,   T1.student_name
    ,   T2.subject_name
ORDER BY
        T1.student_id   ASC
    ,   T2.subject_name ASC