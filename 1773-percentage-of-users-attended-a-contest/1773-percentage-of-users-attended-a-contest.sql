/* Write your T-SQL query statement below */
DECLARE @v_UserCnt  INT

SELECT  TOP 1
        @v_UserCnt  =   COUNT(*)
FROM    Users

SELECT  contest_id  =   T1.contest_id
    ,   percentage  =   ROUND(COUNT(*) * 100.0 / @v_UserCnt, 2)
FROM    Register T1
GROUP BY
        T1.contest_id
ORDER BY
        ROUND(COUNT(*) * 100.0 / @v_UserCnt, 2) DESC
    ,   T1.contest_id   ASC