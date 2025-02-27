/* Write your T-SQL query statement below */
SELECT  class   =   T1.class
FROM    Courses T1
GROUP BY
        T1.class
HAVING  COUNT(*) >= 5