CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        # Write your MySQL query statement below.
        SELECT  salary
        FROM    (
            SELECT  salary
                ,   DENSE_RANK() OVER (ORDER BY salary DESC)   AS 'Rank'
            FROM    Employee
        ) T
        WHERE   T.Rank = N
        LIMIT 1
    );
END