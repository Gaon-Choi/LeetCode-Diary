# Write your MySQL query statement below
WITH UNIQUE_TIV_2015 AS (
    SELECT  tiv_2015
    FROM    Insurance
    GROUP BY
            tiv_2015
    HAVING  COUNT(*) > 1
),
UNIQUE_LAT_LON AS
(
    SELECT  lat
        ,   lon
    FROM    Insurance
    GROUP BY
            lat
        ,   lon
    HAVING  COUNT(*) = 1
)

SELECT  ROUND(SUM(T1.tiv_2016), 2)  AS  tiv_2016
FROM    Insurance T1
JOIN    UNIQUE_TIV_2015 T2
    ON  T2.tiv_2015 =   T1.tiv_2015
JOIN    UNIQUE_LAT_LON T3
    ON  T3.lat  =   T1.lat
    AND T3.lon  =   T1.lon