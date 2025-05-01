/* Write your T-SQL query statement below */
SELECT  day         =   T1.event_day
    ,   emp_id      =   T1.emp_id
    ,   total_time  =   SUM(T1.out_time - T1.in_time)
FROM    Employees T1
GROUP BY
        T1.event_day
    ,   T1.emp_id