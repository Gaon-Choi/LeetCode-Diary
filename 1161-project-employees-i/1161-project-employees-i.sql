/* Write your T-SQL query statement below */
SELECT  project_id      =   T1.project_id
    ,   average_years   =   ROUND(AVG(T2.experience_years * 1.0), 2)
FROM    Project T1
JOIN    Employee T2
    ON  T2.employee_id  =   T1.employee_id
GROUP BY
        T1.project_id