# Write your MySQL query statement below
SELECT  'Low Salary'    AS  category
    ,   SUM(
            CASE
                WHEN T1.income < 20000  THEN 1
                ELSE 0
            END
        )               AS  accounts_count
FROM    Accounts T1

UNION ALL

SELECT  'Average Salary'    AS  category
    ,   SUM(
            CASE
                WHEN 20000 <= T1.income AND T1.income <= 50000 THEN 1
                ELSE 0
            END
        )               AS  accounts_count
FROM    Accounts T1

UNION ALL

SELECT  'High Salary'    AS  category
    ,   SUM(
            CASE
                WHEN T1.income > 50000  THEN 1
                ELSE 0
            END
        )               AS  accounts_count
FROM    Accounts T1