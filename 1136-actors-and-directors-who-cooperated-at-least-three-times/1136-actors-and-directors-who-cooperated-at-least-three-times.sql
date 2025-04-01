# Write your MySQL query statement below
SELECT  T1.actor_id     AS actor_id
    ,   T1.director_id  AS director_id
FROM    ActorDirector T1
GROUP BY
        T1.actor_id
    ,   T1.director_id
HAVING  COUNT(*) >= 3