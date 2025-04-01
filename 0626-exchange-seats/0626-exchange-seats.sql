# Write your MySQL query statement below
SELECT  T1.id                           AS id
    ,   IFNULL(T2.student, T1.student)  AS student
FROM    (
    SELECT  TT1.id
        ,   TT1.student
        ,   CASE    WHEN TT1.id % 2 = 0 THEN TT1.id - 1
                    WHEN TT1.id % 2 = 1 THEN TT1.id + 1
            END AS pair_friend
    FROM    Seat TT1
) T1
LEFT JOIN    Seat T2
    ON  T2.id   =   T1.pair_friend
ORDER BY
        T1.id   ASC