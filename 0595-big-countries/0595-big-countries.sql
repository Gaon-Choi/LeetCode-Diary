# Write your MySQL query statement below
SELECT  name
    ,   population
    ,   area
FROM    World T1
WHERE   T1.area >= 3000000
    OR  T1.population >= 25000000